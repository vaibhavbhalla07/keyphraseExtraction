import utils.ReadFilterData as filter
import utils.ExtractWikipediaPage as wiki
import utils.Vocabulary as vocab
import utils.TFIDF as tfidf
import numpy as np
import utils.KeyPhrasesPerDoc as kp
from utils import CreateDictionaries as cd
from utils import ClusteringMethods as clusters
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(4)
import collections








if __name__ == "__main__":

    documents = np.array(filter.get_filter_doc())
    vocabulary,unique_words = vocab.create_vocab_dictionary(documents)
    word_wiki = pool.map(wiki.get_wiki_pages, unique_words)
    super_word_wiki = collections.defaultdict(list)
    for d in word_wiki:
        for k, v in d.iteritems():
            super_word_wiki[k].append(v)
    pool.close()
    pool.join()
    wiki_doc = " ".join(list(super_word_wiki.keys()))
    doc_dictionary = cd.getCountDictFromDoc(wiki_doc)
    bigram_dict = cd.getBigramCounts(wiki_doc)
    tfidf_matrix = tfidf.getTFIDFmatrix(unique_words,super_word_wiki)
    for doc in documents:
        cosine_sim_matrix,euclidean_dist_matrix,pmi_c_matrix = kp.createSimilarityMatrices(doc,vocabulary,super_word_wiki,tfidf_matrix,doc_dictionary,bigram_dict)
        labels_cos,dict_cos = clusters.createClusters(cosine_sim_matrix,unique_words,10,"spectral")
        labels_euc,dict_euc = clusters.createClusters(euclidean_dist_matrix,unique_words,10,"spectral")
        labels_pmi,dict_pmi = clusters.createClusters(pmi_c_matrix,unique_words,10,"spectral")

        labels_cos,centers,dict_cos = clusters.createClusters(cosine_sim_matrix,unique_words,10,"affinity")
        print "end"





