import nltk
from nltk import word_tokenize
import numpy as np
import utils.POSExtracter as pos
import utils.ReadFilterData as filter

if __name__ == "__main__":
    documents = np.array(filter.get_filter_doc())
    pos_doc=pos.extractPOS(documents)
    possible_key=pos.extract_keyphrases(pos_doc)
    print possible_key.values()[0]


