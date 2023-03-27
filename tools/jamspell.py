import os

import spacy
import jamspell
from tqdm import tqdm

from .config import ROOT_DIR


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel(os.path.join(ROOT_DIR, 'jamspell', 'en.bin'))

nlp = spacy.load("en_core_web_sm")
tokenizer = nlp.tokenizer


def jamspell_predict(noised_sents):
    preds = []
    for sent in tqdm(noised_sents):
        fixed = corrector.FixFragment(sent)
        tokens = tokenizer(fixed)
        preds.append({'tokens': [x.text for x in tokens], 'text': fixed})
    return preds
