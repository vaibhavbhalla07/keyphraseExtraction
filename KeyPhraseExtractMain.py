import utils.ReadFilterData as filter
import utils.ExtractWikipediaPage as wiki
import utils.Vocabulary as vocab
import utils.TFIDF as tfidf
import numpy as np
import utils.KeyPhrasesPerDoc as kp
from multiprocessing.dummy import Pool as ThreadPool
# string_regex = r'''(?x) ([A-Z])(\.[A-Z])+\.? | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\.| [][.,;"'?():-_`]'''


if __name__ == "__main__":
    documents = np.array(filter.get_filter_doc())
    vocabulary,unique_words = vocab.create_vocab_dictionary(documents)
    pool = ThreadPool(4)
    word_wiki = pool.map(wiki.get_wiki_pages, unique_words)
    pool.close()
    pool.join()
    tfidf_matrix = np.zeros(shape=(len(vocabulary),len(word_wiki)))
    for i,doc in enumerate(word_wiki):
        for j,word in enumerate(unique_words):
            tfidf_matrix[j][i] = tfidf.tf_idf(word,word_wiki[doc],list(word_wiki.values()))
    for doc in documents:
        kp.createKeyPhrasesFromDoc(doc,word_wiki,vocabulary,tfidf_matrix)
    print("end")