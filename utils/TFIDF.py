import math


def term_frequency(term, document):
    frequency = 0
    if term in document.split():
        for word in document.split():
            if term == word:
                frequency = +1
    return frequency / len(document.split())


def inverse_doc_freq(term, documents):
    doc_freq = 0
    for doc in documents:
        if term in doc.split():
            doc_freq += 1
    return math.log(len(documents) / (doc_freq+1))


def tf_idf(word, document, document_list):
    return term_frequency(word, document) * inverse_doc_freq(word, document_list)
