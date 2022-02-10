
def corpus_unique(filename, filename2):

    open_file = open(filename, "r")
    final_dict1 = []
    for line in open_file:
        if line.lower() not in final_dict1:
            final_dict1.append(line.lower())

    open_file.close()

    pen_file = open(filename2, "r")
    final_dict = []
    for line in pen_file:
        if line.lower() not in final_dict:
            final_dict.append(line.lower())

    open_file.close()

    similar_file1 = open(filename[:-10] + "with_similar.csv", "w")

    for item in final_dict1:
        similar_file1.write(item)

    similar_file2 = open(filename2[:-10] + "with_similar.csv", "w")

    for item in final_dict:
        similar_file2.write(item)

    similar_file1.close()
    similar_file2.close()


    dict1_len = len(final_dict1)
    dict_len = len(final_dict)
    similar_words = []

    for i in range(dict1_len):
        for y in range(dict_len):
            if i < dict1_len and y < dict_len:
                if final_dict1[i] == final_dict[y]:
                    #similar_words.append(final_dict[i])
                    del final_dict[y]
                    dict_len -= 1
                    del final_dict1[i]
                    dict1_len -= 1

    final_corpus = open(filename[:-10] + "unique_corpus.csv", "w")

    for item in final_dict1:
        final_corpus.write(item)

    final_corpus2 = open(filename2[:-10] + "unique_corpus.csv", "w")

    for item in final_dict:
        final_corpus2.write(item.lower())

    similar_corpus = open("Similar_words.csv", "w")
    for item in similar_words:
        similar_corpus.write(item.lower())


def main():
    corpus_unique("Malay_14.24.01_corpus.csv",
                  "Iban_14.24.01_corpus.csv")


if __name__ == '__main__':
    main()
