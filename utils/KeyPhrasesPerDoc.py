import numpy as np
import distanceMeasures as dm
import sklearn.cluster as sk
calculated_words_for_similarity = list()


def createKeyPhrasesFromDoc(doc,wiki_dict,vocabulary,tfidf_matrix):
    unique_words = np.array(list(set(doc.split())))
    similarity_matrix = np.zeros(shape=(len(unique_words),len(unique_words)))
    for word in vocabulary:
        similarity_matrix[vocabulary[word]] = getCosineSimilarity(word,vocabulary,tfidf_matrix)
    spectral = sk.SpectralClustering()
    spectral.fit(similarity_matrix)

def getCosineSimilarity(word,vocabulary,tfidf_matrix):
    vector_similarity = np.zeros(shape=(len(vocabulary)))
    calculated_words_for_similarity.append(word)
    for w in vocabulary:
        if w not in calculated_words_for_similarity:
            vector_similarity[vocabulary[w]] = dm.cosine_similarity(tfidf_matrix[vocabulary[w]],tfidf_matrix[vocabulary[word]])
    return vector_similarity