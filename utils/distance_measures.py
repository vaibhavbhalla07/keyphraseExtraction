import numpy as np
import math


def euclidean_distance(vector1, vector2):
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    return math.sqrt(sum(dist))


def cosine_similarity(vector1,vector2):
    vector_product = np.dot(vector1,vector2)
    norm_vector1 = math.sqrt(np.sum(np.square(vector1)))
    norm_vector2 = math.sqrt(np.sum(np.square(vector2)))
    if norm_vector1*norm_vector2!=0:
        return vector_product/(norm_vector1*norm_vector2)
    return 0.0


def PMI_3(word1_article_counter,word2_article_counter,word1_2_article_adj_counter,no_wiki_articles):
    l1 = no_wiki_articles * word1_2_article_adj_counter
    l2 = word1_article_counter * word2_article_counter
    pmic_distance = math.log(1+(l1/(l2+1)),2)
    return pmic_distance


def getPMIMeasures(w1,w2,total_wiki_docs,doc_dictionary,bigram_dict):
    w1_count=0
    w2_count=0
    w1_w2_adj_count=0
    if w1 in doc_dictionary:
        w1_count = doc_dictionary[w1]
    if w2 in doc_dictionary:
        w2_count = doc_dictionary[w2]
    if (w1,w2) in bigram_dict:
        w1_w2_adj_count = bigram_dict[(w1,w2)]
    return PMI_3(w1_count,w2_count,w1_w2_adj_count,total_wiki_docs)

# def PMI_1(word1_article_counter , word2_article_counter ,word1_2_article_counter, no_wiki_articles):
# 	l1 = no_wiki_articles * word1_2_article_counter
# 	l2 = word1_article_counter * word2_article_counter
# 	pmin_distance = math.log(l1/l2,2)
# 	return pmin_distance


# def PMI_2(word1_counter,word2_counter ,word1_2_adj_counter,no_of_terms):
# 	l1 = no_of_terms * word1_2_counter
# 	l2 = word1_counter * word2_counter
# 	pmit_distance = math.log(l1/l2,2)
# 	return pmic_distance



# def normalized_google_distance(word1_counter , word2_counter ,word1_2_counter, no_wiki_articles)
# 	l1 = max(math.log10(word1_counter),math.log10(word2_counter))-math.log10(word1_2_counter)
# 	l2 = math.log10(no_wiki_articles)-min(math.log10(word1_counter),math.log10(word1_counter))
# 	normalized_google_distance = l1/l2
# 	return normalized_google_distance
