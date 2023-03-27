import os

from config import ROOT_DIR


filename_to_fix = os.path.join(ROOT_DIR, 'neuspell_repo', 'neuspell', 'off_the_shelf', '__init__.py')

with open(filename_to_fix) as f:
    raw_init = f.read()
    raw_init = raw_init.replace('if is_module_available("jamspell"):', 'if False:')

with open(filename_to_fix, 'w') as f:
    f.write(raw_init)
