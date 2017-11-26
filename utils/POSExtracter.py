# -*- coding: utf-8 -*-
import nltk
from nltk import word_tokenize
import numpy as np
import re





def extractPOS(docs):
    pos_doc=[]
    for doc in docs:
        pos_doc.append(nltk.pos_tag(word_tokenize(doc)))
        print("keyphrases are")
        for phrase in extract_keyphrases(pos_doc):
            print phrase
    return pos_doc


def extract_keyphrases(pos_doc):
    total_docs_key_phrases = {}
    for doc in pos_doc:
        pos = []
        word = []
        key_phrases_doc=[]
        for word_tuple in doc:
            word.append(word_tuple[0])
            pos.append(word_tuple[1])
        pos_string=" ".join(pos)
        word_string=" ".join(word)
        p=re.compile('JJ∗NN+|NNS+|NNP+')
        iterator = p.finditer(pos_string)
        for each_match in iterator:
            key_phrases_doc.append(extract_words(each_match.span()[0],each_match.span()[1],word_string))
        total_docs_key_phrases[doc]=key_phrases_doc
        return total_docs_key_phrases

def extract_words(from_index,to_index,doc):
    return " ".join(word_tokenize(doc)[from_index:to_index])
