import spacy
import hunspell
from tqdm import tqdm


hobj = hunspell.HunSpell('hunspell_dicts/en_US.dic', 'hunspell_dicts/en_US.aff')
nlp = spacy.load("en_core_web_sm")
tokenizer = nlp.tokenizer

# prevent splitting by apostrophes - Hunspell expects them to be joined with main word
apostrophes = {"'s", "'S", '’s', '’S'}
suffixes = [x for x in nlp.Defaults.suffixes if x not in apostrophes]
suffix_regex = spacy.util.compile_suffix_regex(suffixes)
nlp.tokenizer.suffix_search = suffix_regex.search

# https://stackoverflow.com/a/59582203
tokenizer.rules = {
    key: value
    for key, value in nlp.tokenizer.rules.items()
    if "'" not in key and "’" not in key and "‘" not in key
}


def hunspell_one_sent(sent):
    tokens = tokenizer(sent)
    final = []

    for token in tokens:
        token_text = token.text
        if token.is_punct or token.is_digit:
            final.append(token_text)
        elif not hobj.spell(token_text):
            options = hobj.suggest(token_text)
            new = options[0] if options else token_text
            final.append(new)
        else:
            final.append(token_text)

        if token.whitespace_:
            final.append(token.whitespace_)

    return ''.join(final)


def hunspell_predict(noised_sents):
    preds = [
        hunspell_one_sent(sent)
        for sent in tqdm(noised_sents)
    ]
    return preds
