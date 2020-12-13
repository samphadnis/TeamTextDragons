import json
import string
import sys

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean(x):

    tokens = word_tokenize(x)
    
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    
    # remove punctuation
    table  = str.maketrans('', '', string.punctuation)
    words  = [w.translate(table) for w in tokens]
    
    # remove remaining tokens that are not alphabetic
    #words = [word for word in words if word.isalpha()]
    
    # filter out stop words
    #stop_words  = set(stopwords.words('english'))
    #words       = [w for w in words if not w in stop_words]
    
    # stemming of words
    #from nltk.stem.porter import PorterStemmer
    #porter  = PorterStemmer()
    #stemmed = [porter.stem(word) for word in tokens]
    y = ' '.join(words)

    return y

with open(sys.argv[1], encoding="utf8") as json_file:
    json_list = list(json_file)

out = open(sys.argv[1]+'-cleaned', "w", encoding="utf8")

for json_str in json_list:

    result = json.loads(json_str)
    result['context']  = [clean(x) for x in result['context']]
    result['response'] = clean(result['response'])
    
    json.dump(result, out)
    out.write("\n")

out.close()
