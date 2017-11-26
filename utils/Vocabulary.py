

def create_vocab_dictionary(doc):
    vocabulary={}
    words = list(set(doc.split()))
    for w in words:
        if w not in vocabulary:
            vocabulary[w] = len(vocabulary)
    unique_words = list(vocabulary.keys())
    return vocabulary, unique_words