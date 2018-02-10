# Emmi Lahtisalo, 014163276

'''Assignment 8.2.'''

###########################

import nltk
import re
import pprint
from nltk.corpus import conll2000
import sys

# defining the chunker

class ConsecutiveNPChunkTagger(nltk.TaggerI):

    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        tagged_sents = [[((w,t),c) for (w,t,c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)

def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i-1]

    if i == len(sentence)-1:
        nextword, nextpos = "<END>", "<END>"
    else:
        nextword, nextpos = sentence[i+1]
    return {"pos": pos,
            "word": word,
            "prevpos": prevpos,
            "nextpos": nextpos,
            "prevpos+pos": "%s+%s" % (prevpos, pos),
            "pos+nextpos": "%s+%s" % (pos, nextpos),
            "tags-since-dt": tags_since_dt(sentence, i)}

def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)
    return '+'.join(sorted(tags))

# preprocessing the text, i.e. tokenizing it into sentences, 
# sentences to words, and tagging words in sentences with POS tags

def ie_preprocess(sents):
    sentences = nltk.sent_tokenize(sents)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences


def main():

# reading the file

    try:
        gs_file = open("bbc-english-text-20170315.txt", "r", encoding="utf-8")
        sents = gs_file.read()
    except OSError:
        print("Error reading file.")
        sys.exit()

# defining the test and train sets

    test_sents = ie_preprocess(sents)
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    chunker = ConsecutiveNPChunker(train_sents)

# chunking the test set with the shiny trained NP chunker

    for sentence in test_sents:
        print(chunker.parse(sentence))

main()


# The chunker works quite well and can chunk correctly simple NPs.
# (NP the/DT election/NN campaign/NN), (NP his/PRP$ tax/NN returns/NNS),  
# (NP a/DT very/RB wealthy/JJ individual/JJ), (NP MSNBC/NNP host/NN Rachel/NNP Maddow/NNP), etc.
# The program doesn't recognise the GBP values in parentheses correctly,
# Based on this I would assume that the accuracy of the tagger is quite high, 
# but not 100% by any means.
