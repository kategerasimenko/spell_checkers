import os
import sys
import random

import torch
import spacy
import numpy as np
from transformers import BertTokenizer

from .config import ROOT_DIR
sys.path.append(os.path.join(ROOT_DIR, 'neuspell_repo'))

from neuspell import BertChecker


SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

checker = BertChecker()
checker._from_pretrained(ckpt_path=os.path.join(ROOT_DIR, 'neuspell-subwordbert-probwordnoise'))
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')

nlp = spacy.load("en_core_web_sm")
spacy_tokenizer = nlp.tokenizer


def neuspell_predict(noised_sents):
    fixed = checker.correct_strings(noised_sents)
    tok = tokenizer(fixed, truncation=False, padding=False)
    detok = tokenizer.batch_decode(tok['input_ids'], skip_special_tokens=True)
    preds = [
        {'tokens': [x.text for x in spacy_tokenizer(pred)], 'text': pred}
        for pred in detok
    ]
    return preds
