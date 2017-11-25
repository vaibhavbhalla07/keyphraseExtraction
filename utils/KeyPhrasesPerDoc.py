import numpy as np
import DistanceMeasures as dm
import utils.TFIDF as tfidf
from collections import Counter
from utils import ClusteringMethods as clusters

calculated_words_for_similarity = list()


def getDistanceMeasuresForWordVector(word, vocabulary,word_wiki, tfidf_matrix,doc_dictionary,bigram_dict):
    cosine_similarity = np.zeros(shape=(len(vocabulary)))
    euclidean_dist = np.zeros(shape=(len(vocabulary)))
    pmi_c= np.zeros(shape=(len(vocabulary)))
    calculated_words_for_similarity.append(word)
    for w in vocabulary:
        pmi_c[vocabulary[w]] = dm.getPMIMeasures(w,word,len(word_wiki),doc_dictionary,bigram_dict)
        if w not in calculated_words_for_similarity:
            cosine_similarity[vocabulary[w]] = dm.cosine_similarity(tfidf_matrix[vocabulary[w]],tfidf_matrix[vocabulary[word]])
            euclidean_dist[vocabulary[w]] = dm.euclidean_distance(tfidf_matrix[vocabulary[w]],tfidf_matrix[vocabulary[word]])

    return cosine_similarity,euclidean_dist,pmi_c


def createSimilarityMatrices(doc,vocabulary, word_wiki,tfidf_matrix,doc_dictionary,bigram_dict):
    unique_words = np.array(list(set(doc.split())))
    cosine_sim_matrix = np.zeros(shape=(len(unique_words),len(unique_words)))
    pmi_c_matrix = np.zeros(shape=(len(unique_words),len(unique_words)))
    euclidean_dist_matrix = np.zeros(shape=(len(unique_words),len(unique_words)))
    for word in vocabulary:
        cosine_sim_matrix[vocabulary[word]],euclidean_dist_matrix[vocabulary[word]],pmi_c_matrix[vocabulary[word]] = getDistanceMeasuresForWordVector(word, vocabulary,word_wiki, tfidf_matrix,doc_dictionary,bigram_dict)

    return cosine_sim_matrix,euclidean_dist_matrix,pmi_c_matrix


 # def getClusterLabels(cosine_sim_matrix,euclidean_dist_matrix,pmi_c_matrix):
 #    spectral_labels_cos = clusters.spectral_cluster(cosine_sim_matrix,15)
 #    # dict_cos = getClustersDictionary(spectral_labels_cos,unique_words,cosine_sim_matrix)
 #    spectral_labels_euc = clusters.spectral_cluster(euclidean_dist_matrix,5)
 #    spectral_labels_pmi = clusters.spectral_cluster(pmi_c_matrix,5)
 #    # dict_pmi= getClustersDictionary(spectral_labels_pmi,unique_words,pmi_c_matrix)
 #


