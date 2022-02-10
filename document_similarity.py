# create a chatbot that asks user to upload a documnet
import numpy as nump


def cosine_sim(doc1, doc2):
    d_product = nump.dot(doc1, doc2)
    doc1_norm = nump.linalg.norm(doc1)
    doc2_norm = nump.linalg.norm(doc2)
    # print(doc2_norm)

    return d_product / (doc1_norm * doc2_norm)


def find_similarity(doc1, doc2):
    words_list = []
    for key in doc1:
        words_list.append(key)
    for key in doc2:
        words_list.append(key)

    words_size = len(words_list)

    v1 = nump.zeros(words_size, dtype=int)
    v2 = nump.zeros(words_size, dtype=int)

    i = 0

    for key in words_list:
        v1[i] = doc1.get(key, 0)
        v2[i] = doc2.get(key, 0)
        i = i + 1

    return cosine_sim(v1, v2)


def get_doc_frew(cur_corpus):
    doc_freq = {}

    corpus = open(cur_corpus, "r")

    for word in corpus:
        if word[:-3] in doc_freq:
            doc_freq[word[:-3]] = doc_freq[word[:-3]] + 1

        elif word[:-3] not in doc_freq:
            doc_freq[word[:-3]] = 1

    # for key, value in doc_freq.items():
    #    print([key, value])
    #    print("\n")
    # print(len(doc_freq))

    return doc_freq


'''def term_freq_idf(word_dic, filename):

    tf_idf = {}

    word_list = open(filename, "r")

    N = 0
    words = []

    for line in word_list:
        words.append(line)
        N += 1

    for i in range(N):
        tokes = words[i]
        counter = 0
        for token in word_dic:
            if token in words:

            tf = token
        print("here")'''


def main():

    doc_freq = get_doc_frew("Malay_14.24.01_corpusunique_corpus.csv")
    iban_freq = get_doc_frew("Iban_14.24.01_corpusunique_corpus.csv")
    iban_ids = open("Malay_14.24.01_wordID.csv", "r")
    malay_ids = open("Iban_14.24.01_wordID.csv", "r")

    malay_nonuniq = get_doc_frew("Malay_14.24.01_corpus.csv")
    iban_nonuniq = get_doc_frew("Iban_14.24.01_corpus.csv")

    article_freq = get_doc_frew("article1.txt")
    article2_freq = get_doc_frew("article2.txt")

    print(find_similarity(article_freq, iban_nonuniq))

    #print(find_similarity(doc_freq, article_freq, iban_ids))
    #print(find_similarity(doc_freq, article_freq, malay_ids))
    #print(find_similarity(iban_freq, article2_freq))

    #print(find_similarity(article_freq, iban_freq))
    #print(find_similarity(article2_freq, doc_freq))

    #print(find_similarity(article2_freq, article_freq))

#    tf_idf = term_freq_idf(doc_freq, "Malay_14.24.01.csv")


if __name__ == '__main__':
    main()
