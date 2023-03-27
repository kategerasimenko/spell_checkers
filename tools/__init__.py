from tools.hunspell import hunspell_predict
from tools.jamspell import jamspell_predict
from tools.neuspell import neuspell_predict


TOOLS = {
    'hunspell': hunspell_predict,
    'jamspell': jamspell_predict,
    'neuspell': neuspell_predict
}