import torch
from tqdm import tqdm
from transformers import (
    AutoTokenizer, AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq
)

MAX_SEQ_LEN = 512
GENERATION_LEN = 512

tokenizer = AutoTokenizer.from_pretrained("vennify/t5-base-grammar-correction")
model = AutoModelForSeq2SeqLM.from_pretrained("vennify/t5-base-grammar-correction")


def t5_predict(noised_sents):
    model.eval()

    # data collator which pads inputs on the go based on max length inside the batch
    collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    tokens = tokenizer(noised_sents, truncation=True, max_length=MAX_SEQ_LEN, return_tensors='pt')
    test_dataloader = DataLoader(tokens, batch_size=8, collate_fn=collator)

    all_preds = []

    with torch.no_grad():
        for batch in tqdm(test_dataloader):
            batch = {k: v.to(DEVICE) for k, v in batch.items()}
            preds = model.generate(**batch, num_beams=3, max_length=GENERATION_LEN)
            decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
            all_preds.extend(decoded_preds)

    return decoded_preds