# Emmi Lahtisalo

'''Raw Data Processing'''

import csv, json
import string
import pandas as pd
import nltk

df = pd.read_json("Automotive_5.json", lines=True)

# lowercasing the texts in reviewText column
df['reviewText'] = df['reviewText'].str.lower()

# removing punctuation...
def del_punct(x):
    try:
        x = ''.join(ch for ch in x if ch not in set(string.punctuation))
    except:
        pass
    return x
df['reviewText'] = df['reviewText'].apply(del_punct)

# ... and stopwords
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
df['reviewText'] = df['reviewText'].str.split()
df['reviewText'] = df['reviewText'].apply(lambda x: [item for item in x if item not in stopwords])

# stemming
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')

df['reviewText'] = df["reviewText"].apply(lambda x: [stemmer.stem(y) for y in x])

# filtering data
pos = df.loc[df['overall'] == 4, 'reviewText']
fives = df.loc[df['overall'] == 5, 'reviewText']

pos = pos.append(fives)
pos.to_csv('pos.txt', header=None, index=None)

neg = df.loc[df['overall'] == 1, 'reviewText']
twos = df.loc[df['overall'] == 2, 'reviewText']

neg = neg.append(twos)
neg.to_csv('neg.txt', header=None, index=None)
