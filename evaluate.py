import os
import json
import random
from pathlib import Path


ROOT_DIR = str(Path(__file__).parent)
random.seed(42)


def calc_sequence_acc(clean, preds):
    n_correct = sum(c['text'] == p['text'] for c, p in zip(clean, preds))
    return round(n_correct / len(clean), 3)


def print_random_errors(noised, preds, clean):
    errors = [(n, p, c) for n, p, c in zip(noised, preds, clean) if c['text'] != p['text']]
    sample = random.sample(errors, k=50)
    for n, p, c in sample:
        print(n['text'])
        print(p['text'])
        print(c['text'])
        print()


with open(os.path.join(ROOT_DIR, 'news_synth', 'clean.jsonl')) as f:
    clean = [json.loads(l) for l in f.readlines()]

with open(os.path.join(ROOT_DIR, 'news_synth', 'noised_prob.jsonl')) as f:
    noised = [json.loads(l) for l in f.readlines()]

accs = []
for tool_pred in os.listdir(os.path.join(ROOT_DIR, 'preds')):
    tool = tool_pred.rsplit('.', 1)[0]
    print('===', tool, '===')

    with open(os.path.join(ROOT_DIR, 'preds', tool_pred)) as f:
        preds = [json.loads(l) for l in f.readlines()]

    print_random_errors(noised, preds, clean)
    acc = calc_sequence_acc(clean, preds)
    accs.append((tool, acc))


for tool, acc in accs:
    print(tool, acc)
