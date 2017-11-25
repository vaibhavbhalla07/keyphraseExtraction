from collections import Counter

def getCountDictFromDoc(doc):
    doc_dict={}
    word_list=doc.split()
    for w in word_list:
        if w not in doc_dict:
            doc_dict[w] =1
        else:
            doc_dict[w]+=1
    return doc_dict


def getBigramCounts(doc):
    words=doc.split()
    return Counter(zip(words, words[1:]))


def getClustersDictionary(labels, unique_words, matrix):
    dictionary={}
    if len(labels)!=0:
        for i, clus in enumerate(labels):
            if sum(matrix[i])==0:
                clus = -1
            if clus not in dictionary:
                dictionary[clus] = [unique_words[i]]
            else:
                dictionary[clus].append(unique_words[i])
    return dictionary
