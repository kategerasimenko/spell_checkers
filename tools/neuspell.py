import os
import sys
import random

import torch
import numpy as np

from config import ROOT_DIR
sys.path.append(os.path.join(ROOT_DIR, 'neuspell_repo'))

from neuspell import BertChecker


SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

checker = BertChecker()
checker._from_pretrained(ckpt_path=os.path.join(ROOT_DIR, 'neuspell-subwordbert-probwordnoise'))


def neuspell_predict(noised_sents):
    preds = checker.correct_strings(noised_sents)
    return preds
