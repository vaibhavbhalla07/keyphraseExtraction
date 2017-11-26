from multiprocessing.dummy import Pool as ThreadPool
import requests
import os
import wikipedia
import ReadFilterData as filter
words = []
word_wiki_dict = {}
wiki_path="documents/wiki/"
count=0

def get_wikipedia_content(title):
    resp = requests.get(
        "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext=&titles={0}".format(
            title))
    json = resp.json
    return json


def get_wiki_pages(word):
    global count
    wiki_files = os.listdir(wiki_path)
    word_file = word+".txt"
    if word_file not in wiki_files:
        get_wiki(word)
        count += 1
        print count
    else:
        with open(wiki_path + word_file) as wf:
            word_wiki_dict[word] = wf.read()
    unk = ", ".join(words)
    write_unk_wiki_words(unk)


def getAllWikiPages():
    pool = ThreadPool(4)
    wiki_files = os.listdir(wiki_path)
    pool.map(getWikiFile,wiki_files)
    pool.close()
    pool.join()
    return word_wiki_dict


def getWikiFile(word_file):
    with open(wiki_path + word_file) as wf:
        word_wiki_dict[word_file] = wf.read()


def get_wiki(title):
    try:
        doc = wikipedia.page(title=title).summary.encode('ascii','ignore').lower()
        doc = filter.remove_special_chars(doc)
        doc = filter.remove_stopwords(doc)
        word_wiki_dict[title] = doc
        write_file(word_wiki_dict[title], title)
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            #taking the first option as word
            doc=wikipedia.page(e.options[0]).summary.encode('ascii','ignore').lower()
            doc = filter.remove_special_chars(doc)
            doc = filter.remove_stopwords(doc)
            word_wiki_dict[title] = doc
            write_file(word_wiki_dict[title], title)
        except BaseException as ex:
            words.append(title)
    except BaseException as ex:
        words.append(title)


def write_file(document,word):
    with open(wiki_path+word+".txt", 'w') as f:
        f.seek(0)
        f.write(document)
        f.close()


def write_unk_wiki_words(unk):
    with open(wiki_path + "UNKNOWN.txt", 'w') as f:
        f.write(unk)
        f.close()

