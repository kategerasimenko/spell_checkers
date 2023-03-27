#!/usr/bin/env bash

# TOOLS

# NeuSpell
git clone https://github.com/neuspell/neuspell.git neuspell_repo
git clone https://huggingface.co/pszemraj/neuspell-subwordbert-probwordnoise
python utils/fix_neuspell.py
cd neuspell_repo
pip install -e .
cd ..

# JamSpell
sudo apt-get install swig3.0
pip install jamspell
mkdir jamspell
wget https://github.com/bakwc/JamSpell-models/raw/master/en.tar.gz
tar -xzf en.tar.gz -C jamspell

# Hunspell
sudo apt-get install python-dev libhunspell-dev
pip install hunspell spacy==3.5.1
mkdir hunspell_dicts
wget -O hunspell_dicts/en_US.aff  https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.aff
wget -O hunspell_dicts/en_US.dic https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.dic


# DATA

# News 2020 - 10K sentences
# from https://downloads.wortschatz-leipzig.de/corpora/eng_news_2020_10K.tar.gz , not working in Colab
gdown 1SUAquRUHiZ5dQWQNyINBxl4ZRupw2aa0
tar -xzf eng_news_2020_10K.tar.gz
