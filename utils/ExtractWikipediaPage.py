import requests
import os
import wikipedia
import ReadFilterData as filter
words = []
word_wiki_dict = {}
wiki_path="documents/wiki/"


def get_wikipedia_content(title):
    resp = requests.get(
        "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext=&titles={0}".format(
            title))
    json = resp.json
    return json


def get_wiki_pages(unique_words):
    count=0
    wiki_files = os.listdir(wiki_path)
    for w in unique_words:
        word_file = w+".txt"
        if word_file in wiki_files:
        #     get_wiki(w)
        # else:
            with open(wiki_path + word_file) as wf:
                word_wiki_dict[w] = wf.read()
    # unk = ", ".join(words)
    # write_unk_wiki_words(unk)
    return word_wiki_dict


def get_wiki(title):
    try:
        doc = wikipedia.page(title=title).summary.encode('ascii','ignore').lower()
        doc = filter.remove_special_chars(doc)
        doc = filter.remove_stopwords(doc)
        word_wiki_dict[doc] = len(word_wiki_dict)
        write_file(word_wiki_dict[title], title)
    except:
        words.append(title)


def write_file(document,word):
    with open(wiki_path+word+".txt", 'w') as f:
        f.write(document)
        f.close()


def write_unk_wiki_words(unk):
    with open(wiki_path + "UNKNOWN.txt", 'w') as f:
        f.write(unk)
        f.close()

