import math
import numpy as np
from collections import Counter


def term_frequency(term, document):
    frequency = 0
    if term in document.split():
        for word in document.split():
            if term == word:
                frequency = +1
    return float(frequency)


def inverse_doc_freq(term, documents):
    doc_freq = 0
    for doc in documents:
        if term in doc.split():
            doc_freq += 1
    return float(math.log(len(documents) / (doc_freq+1)))


def tf_idf(word, document, document_list):
    return float(term_frequency(word, document) * inverse_doc_freq(word, document_list))


def getTFIDFmatrix(unique_words,word_wiki):
    tfidf_matrix = np.zeros(shape=(len(unique_words), len(word_wiki)))
    wiki_docs = list(word_wiki.values())
    for i, doc_idx in enumerate(word_wiki):
        for j, word in enumerate(unique_words):
            val = tf_idf(word, word_wiki[doc_idx],wiki_docs)
            tfidf_matrix[j][i] = val
    return tfidf_matrix
