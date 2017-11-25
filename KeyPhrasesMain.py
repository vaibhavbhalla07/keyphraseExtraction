import utils.ReadFilterData as filter
import utils.ExtractWikipediaPage as wiki
import utils.Vocabulary as vocab
import utils.TFIDF as tfidf
import numpy as np
import utils.KeyPhrasesPerDoc as kp
from utils import CreateDictionaries as cd
from utils import ClusteringMethods as clusters


if __name__ == "__main__":

    documents = np.array(filter.get_filter_doc())
    vocabulary,unique_words = vocab.create_vocab_dictionary(documents)
    word_wiki = wiki.get_wiki_pages(unique_words)
    wiki_doc = " ".join(list(word_wiki.values()))
    doc_dictionary = cd.getCountDictFromDoc(wiki_doc)
    bigram_dict = cd.getBigramCounts(wiki_doc)
    tfidf_matrix = tfidf.getTFIDFmatrix(unique_words,word_wiki)
    for doc in documents:
        cosine_sim_matrix,euclidean_dist_matrix,pmi_c_matrix = kp.createSimilarityMatrices(doc,vocabulary,word_wiki,tfidf_matrix,doc_dictionary,bigram_dict)
        labels_cos,dict_cos = clusters.createClusters(cosine_sim_matrix,unique_words,10,"affinity")

        labels_euc,dict_euc = clusters.createClusters(euclidean_dist_matrix,unique_words,10,"affinity")
        labels_pmi,dict_pmi = clusters.createClusters(pmi_c_matrix,unique_words,10,"affinity")




