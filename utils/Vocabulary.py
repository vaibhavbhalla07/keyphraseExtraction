

def create_vocab_dictionary(documents):
    vocabulary={}
    for doc in documents:
        words = list(set(doc.split()))
        for w in words:
            if w not in vocabulary:
                vocabulary[w] = len(vocabulary)
    unique_words = list(vocabulary.keys())
    return vocabulary, unique_words