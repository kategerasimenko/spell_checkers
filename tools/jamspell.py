import os

import jamspell
from tqdm import tqdm

from config import ROOT_DIR


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel(os.path.join(ROOT_DIR, 'jamspell', 'en.bin'))


def jamspell_predict(noised_sents):
    for sent in tqdm(noised_sents):
        fixed = corrector.FixFragment(sent)
        tokens = tokenizer(fixed)
        preds.append({'tokens': [x.text for x in tokens], 'text': fixed})
    return preds
