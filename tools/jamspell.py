import os

import jamspell
from tqdm import tqdm

from config import ROOT_DIR


corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel(os.path.join(ROOT_DIR, 'jamspell', 'en.bin'))


def jamspell_predict(noised_sents):
    preds = [
        corrector.FixFragment(sent)
        for sent in tqdm(noised_sents)
    ]
    return preds
