import os
import re

regex = "[~`\,\[\]\(\)\";\{\}:<>?\\\\\/$#@=!^%&*\'\d\.\-_]"
stopwords_path = "documents/stopwords.txt"
documents_path = "documents/input_test/"
output_path = "documents/output/"
stopwords = open(stopwords_path).read().lower().split(",")


def remove_stopwords(data):
    return " ".join([w.strip() for w in data.split() if w not in stopwords])


def read_documents(path):
    docs=[]
    file_list = os.listdir(path)
    for f in file_list:
        with open(path + f) as y:
            docs.append(y.read().lower())
    return docs


def remove_special_chars(doc):
    doc = re.sub(regex," ",doc)
    doc = re.sub("[\s+]"," ",doc).strip()
    return doc


def get_filter_doc():
    docs = read_documents(documents_path)
    docs = [remove_special_chars(doc) for doc in docs]
    docs = [remove_stopwords(doc) for doc in docs]
    return docs

