# -*- coding: utf-8 -*-
import nltk
from nltk import word_tokenize
import numpy as np
import re





def extractPOS(doc):
    pos_doc=[]
    pos_doc.append(nltk.pos_tag(word_tokenize(doc)))
    return pos_doc


def extract_keyphrases_from_list(pos_doc):
    total_docs_key_phrases = {}
    for i,doc in enumerate(pos_doc):
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
        total_docs_key_phrases[i]=key_phrases_doc
        return total_docs_key_phrases

def extract_keyphrases(doc):
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
    return key_phrases_doc


def extract_words(from_index,to_index,doc):
    return " ".join(word_tokenize(doc)[from_index:to_index])


def extract_matching_keyphrase(centers,keyphrases,unique_words):
    final_key_phrases=[]
    for keyphrase in keyphrases:
        for center in centers:
            if unique_words[center] in keyphrase.split():
                final_key_phrases.append(keyphrase)
    return final_key_phrases

def displayKeyPhrases(keyphrases,type):
    print "keyphrases in ",type
    for word in keyphrases:
        print word
