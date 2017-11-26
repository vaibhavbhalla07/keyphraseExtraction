import utils.ReadFilterData as filter
import utils.ExtractWikipediaPage as wiki
import utils.Vocabulary as vocab
import utils.TFIDF as tfidf
import numpy as np
import utils.KeyPhrasesPerDoc as kp
from utils import CreateDictionaries as cd
from utils import ClusteringMethods as clusters

# pool = ThreadPool(4)
import collections


if __name__ == "__main__":

    documents = np.array(filter.get_filter_doc())

    # pool.map(wiki.get_wiki_pages, unique_words)
    # word_wiki = wiki.word_wiki_dict
    # pool.close()
    # pool.join()
    word_wiki = wiki.getAllWikiPages()
    wiki_doc = " ".join(list(word_wiki.values()))
    doc_dictionary = cd.getCountDictFromDoc(wiki_doc)
    bigram_dict = cd.getBigramCounts(wiki_doc)

    for doc in documents:
        vocabulary, unique_words = vocab.create_vocab_dictionary(doc)
        tfidf_matrix = tfidf.getTFIDFmatrix(unique_words, word_wiki)
        cosine_sim_matrix,euclidean_dist_matrix,pmi_c_matrix = kp.createSimilarityMatrices(doc,vocabulary,word_wiki,tfidf_matrix,doc_dictionary,bigram_dict)
        labels_cos,dict_cos = clusters.createClusters(cosine_sim_matrix,unique_words,10,"spectral")
        # labels_euc,dict_euc = clusters.createClusters(euclidean_dist_matrix,unique_words,10,"spectral")
        labels_pmi,dict_pmi = clusters.createClusters(pmi_c_matrix,unique_words,10,"spectral")

        labels_euc,centers_euc,dict_euc = clusters.createClusters(euclidean_dist_matrix,unique_words,10,"affinity")
        labels_pmi, centers_pmi, dict_pmi = clusters.createClusters(pmi_c_matrix, unique_words, 10, "affinity")
        print "end"





