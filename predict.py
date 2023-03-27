import os

from config import ROOT_DIR
from tools import TOOLS


with open(os.path.join(ROOT_DIR, 'news_synth', 'clean.txt'), encoding='utf-8') as f:
    clean = f.read().strip().split('\n')

with open(os.path.join(ROOT_DIR, 'news_synth', 'noised_prob.txt'), encoding='utf-8') as f:
    noised = f.read().strip().split('\n')

print('Clean', len(clean), f'Noised', len(noised))

os.makedirs(os.path.join(ROOT_DIR, 'preds'), exist_ok=True)

for tool_name, tool_func in TOOLS.items():
    print(tool_name)
    preds = tool_func(noised)
    with open(os.path.join(ROOT_DIR, 'preds', f'{tool_name}.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(preds))
