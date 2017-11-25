import numpy as np
import math


def euclidean_distance(vector1, vector2):
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist


def cosine_similarity(vector1,vector2):
    vector_product = np.dot(vector1,vector2)
    norm_vector1 = math.sqrt(np.sum(np.square(vector1)))
    norm_vector2 = math.sqrt(np.sum(np.square(vector2)))
    return vector_product/(norm_vector1*norm_vector2)


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


# def PMI_3(word1_article_counter,word2_article_counter,word1_2_article_adj_counter,no_wiki_articles):
# 	l1 = no_wiki_articles * word1_2_article_adj_counter
# 	l2 = word1_article_counter * word2_article_counter
# 	pmic_distance = math.log(l1/l2,2)
# 	return pmic_distance


# def normalized_google_distance(word1_counter , word2_counter ,word1_2_counter, no_wiki_articles)
# 	l1 = max(math.log10(word1_counter),math.log10(word2_counter))-math.log10(word1_2_counter)
# 	l2 = math.log10(no_wiki_articles)-min(math.log10(word1_counter),math.log10(word1_counter))
# 	normalized_google_distance = l1/l2
# 	return normalized_google_distance
