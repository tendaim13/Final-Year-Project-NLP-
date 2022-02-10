
import math
import pandas as panda
import numpy as nump
from collections.abc import Iterable
import glob
import os
import pathlib
import string

from pandas.core.algorithms import isin


def term_freq(doc1, doc2):

    word_dict = dict.fromkeys(set(doc1), 0)
    word_dict2 = dict. fromkeys(set(doc2), 0)

    for token in doc1:
        word_dict[token] += 1

    for token in doc2:
        word_dict2[token] += 1

    df1 = panda.DataFrame([word_dict])
    df2 = panda.DataFrame([word_dict2])

    idx = 0

    new_col = ["Term Frequency"]

    df1.insert(loc=idx, column="Document", value=new_col)
    df2.insert(loc=idx, column="Document", value=new_col)

    # print(df1)
    # print(df2)


def term_frequency(article, corpus):
    normaliseDoc = corpus
    return normaliseDoc.count(article) / float(len(normaliseDoc))


def compute_normalisedtf(article):
    tf_art = []
    #tf_cor = []

    # article_list = article
    # corpus_list = corpus
    # print(article_list)

    # corp_norm_tf = dict.fromkeys(set(corpus), 0)
    # print(art_norm_tf)
    for doc in article:
        art_norm_tf = dict.fromkeys(set(doc), 0)
        for word in doc:
            art_norm_tf[word] = term_frequency(word, doc)

        # print(art_norm_tf)
        tf_art.append(art_norm_tf)

        idx = 0
        new_col = ["Normalised TF"]
        art_df = panda.DataFrame([art_norm_tf])
        art_df.insert(loc=idx, column='Document', value=new_col)
        # print(art_df)

    # for word in corpus:
    #    corp_norm_tf[word] = term_frequency(word, corpus)
    #    print("got past panda")
    # tf_cor.append(corp_norm_tf)

    # cor_tf = panda.DataFrame([corp_norm_tf])

    # cor_tf.insert(loc=idx, column='Document', value=new_col)

    # print(cor_tf)

    return tf_art


def idf(term, docs):
    term_in_docs = 0
    # print(len(docs))

    for doc in range(0, len(docs)):
        if term in docs[doc]:
            term_in_docs = term_in_docs + 1

    if term_in_docs > 0:
        return 1.0 + math.log(float(len(docs)) / term_in_docs)
    else:
        return 1.0


def compute_idf(docs):
    idf_dict = {}
    for document in docs:
        for term in document:
            idf_dict[term] = idf(term, docs)

    return idf_dict


def get_tfidf(documents, article, tf_doc, idf_dict):
    tf_idf = []
    index = 0
    df = panda.DataFrame(columns=['doc'] + article)
    for doc in documents:
        df['doc'] = nump.arange(0, len(documents))
        doc_num = tf_doc[index]
        for word in doc:
            for text in article:
                if(text == word):
                    idx = doc.index(word)
                    tf_idf_score = doc_num[word] * idf_dict[word]
                    tf_idf.append(tf_idf_score)
                    df.iloc[index, df.columns.get_loc(word)] = tf_idf_score

        index += 1
    df = df.loc[:, ~df.columns.duplicated()]
    df.fillna(0, axis=1, inplace=True)

    return tf_idf, df


def get_article_tf(article):
    article_tf = {}

    for word in article:
        article_tf[word] = term_frequency(word, article)

    return article_tf


def get_artice_idf(article, documents):
    idf_dict_art = {}
    for word in article:
        idf_dict_art[word] = idf(word, documents)

    return idf_dict_art


def get_articel_tfidf(article, art_tf, art_idf):
    tfidf_dict_art = {}
    for word in article:
        tfidf_dict_art[word] = art_tf[word] * art_idf[word]

    return tfidf_dict_art


def cos_sim(tfidf, df, article, doc_num):
    dtp = 0
    art_mod = 0
    doc_mod = 0
    # print(tfidf)
    # print(article)
    # print(doc_num)
    print(df)

    # df = df.loc[:,~df.index.duplicated()]
    for word in article:
        # print(word)
        # print(df[df.index.duplicated()])
        dtp += tfidf[word] * df[word][df['doc'] == doc_num]
        #print("dtp "+str(dtp)+"\n")
        art_mod += tfidf[word] * tfidf[word]
        #print("art_mod "+str(art_mod))
        doc_mod += df[word][df['doc'] == doc_num] * \
            df[word][df['doc'] == doc_num]
        #print("doc_mod "+str(doc_mod))

    art_mod = nump.sqrt(art_mod)
    doc_mod = nump.sqrt(doc_mod)

    denom = art_mod * doc_mod
    # print(denom)
    # print()
    similarity = dtp/denom
    # print(similarity)

    return similarity


def flat(listener):
    for item in listener:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flat(item):
                yield x
        else:
            yield item


def rank_sim(data, tfidf, df, article):
    sim = []
    for doc_num in range(0, len(data)):
        sim.append(cos_sim(tfidf, df, article, doc_num).tolist())

    return sim


def unique_words(doc):

    article_list = []
    for line in doc:
        line = line.translate(str.maketrans('', '', string.punctuation))
        article_list.append(line.lower())

    open_file = open("Similar_words.csv", "r")
    similar_list = []
    for line in open_file:
        similar_list.append(line.lower())

    open_file.close()

    dict_len = len(article_list)
    resulting_words = []

    for i in range(dict_len):
        if article_list[i][:-1] not in similar_list:
            # print(article_list[i][:-1])
            resulting_words.append(article_list[i])

    '''final_corpus = open(filename[:-10] + "unique_corpus.csv", "w")

    for item in final_dict1:
        final_corpus.write(item)

    final_corpus2 = open(filename2[:-10] + "unique_corpus.csv", "w")

    for item in final_dict:
        final_corpus2.write(item)

    similar_corpus = open("Similar_words.csv", "w")
    for item in similar_words:
        similar_corpus.write(item)'''

    return resulting_words


def main():

    #path = '/Malay_21.11.59/'
    save_path = 'Other_texts'
    for path in pathlib.Path('Iban_').iterdir():
        if path.is_file():
            with open(path, 'r') as open_file:
                temp = []
                line = open_file.readline()
                while line:
                    text = line.split()
                    for item in text:
                        temp.append(item)
                    line = open_file.readline()
                    #print(line)
                doc1_list = unique_words(temp)

                # for line in file:
                # print(line)
                #    doc1_list.append(line[:-1].lower())

                doc2 = open("Malay__unique_corpus.csv", "r")
                doc3 = open("Iban__unique_corpus.csv", "r")

                doc3_list = []
                for line in doc3:
                    doc3_list.append(line[:-2])
                doc2_list = []
                for line in doc2:
                    doc2_list.append(line[:-2])

                tf_doc = term_freq(doc1_list, doc2_list)

                final_cor = compute_normalisedtf(
                    [doc1_list, doc2_list, doc3_list])

                idf_dict = compute_idf([doc1_list, doc2_list, doc3_list])

                tf_idf, df = get_tfidf([doc1_list, doc2_list, doc3_list],
                                       doc1_list, final_cor, idf_dict)

                article_tf = get_article_tf(doc1_list)

                idf_dict_art = get_artice_idf(
                    doc1_list, [doc1_list, doc2_list, doc3_list])

                tfidf_art = get_articel_tfidf(
                    doc1_list, article_tf, idf_dict_art)

                similarity = rank_sim(
                    [doc1_list, doc2_list, doc3_list], tfidf_art, df, doc1_list)

            # print(tfidf_art)
            # print(article_tf)
            # print(idf_dict)
                print(list(flat(similarity)))
                save_file = "Malay_results.txt"
                complete_path = os.path.join(save_path, save_file)
                result = open("Iban_corpus_results.txt", "a")
                result.write(str(open_file) + " => " +
                             str(list(flat(similarity))) + "\n")
                result.close()


if __name__ == '__main__':
    main()
