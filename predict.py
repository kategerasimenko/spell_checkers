import os
import json
from pathlib import Path

from tools import TOOLS


ROOT_DIR = str(Path(__file__).parent)

with open(os.path.join(ROOT_DIR, 'news_synth', 'noised_prob.jsonl'), encoding='utf-8') as f:
    noised = [json.loads(x)['text'] for x in f.read().strip().split('\n')]

os.makedirs(os.path.join(ROOT_DIR, 'preds'), exist_ok=True)

for tool_name, tool_func in TOOLS.items():
    print(tool_name)
    preds = tool_func(noised)
    with open(os.path.join(ROOT_DIR, 'preds', f'{tool_name}.jsonl'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(json.dumps(x, ensure_ascii=False) for x in preds))
