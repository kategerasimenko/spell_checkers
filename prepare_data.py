import os
import sys
import json
import random
from pathlib import Path

ROOT_DIR = str(Path(__file__).parent)
sys.path.append(os.path.join(ROOT_DIR, 'neuspell_repo'))

from neuspell.noising import ProbabilisticCharacterReplacementNoiser


random.seed(42)

noiser = ProbabilisticCharacterReplacementNoiser(language="english")
noiser.load_resources()

# I have to do it like this because of locale issue with spacy + colab
import spacy

nlp = spacy.load("en_core_web_sm")
tokenizer = nlp.tokenizer


with open(os.path.join('eng_news_2020_10K', 'eng_news_2020_10K-sentences.txt'), encoding='utf-8') as f:
    sents = [line.split('\t', 1)[1].strip() for line in f.readlines()]
    random.shuffle(sents)

noised_sents = noiser.noise(sents)

# leaving out changes that changed the number of tokens
final_clean, final_noised = [], []
for noised_sent, clean_sent in zip(noised_sents, sents):
    noised_toks = tokenizer(noised_sent)
    orig_toks = tokenizer(clean_sent)
    if len(noised_toks) == len(orig_toks):
        final_clean.append({'tokens': [x.text for x in orig_toks], 'text': clean_sent})
        final_noised.append({'tokens': [x.text for x in noised_toks], 'text': noised_sent})

for i in range(5):
    print(final_clean[i], final_noised[i], sep='\n', end='\n\n')

os.makedirs(os.path.join(ROOT_DIR, 'news_synth'), exist_ok=True)

with open(os.path.join(ROOT_DIR, 'news_synth', 'clean.jsonl'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(json.dumps(x, ensure_ascii=False) for x in final_clean))

with open(os.path.join(ROOT_DIR, 'news_synth', 'noised_prob.jsonl'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(json.dumps(x, ensure_ascii=False) for x in final_noised))
