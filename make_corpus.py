def corpus_unique(filename):

    open_file = open(filename, "r")
    final_dict1 = []
    for line in open_file:
        if line.lower() not in final_dict1:
            final_dict1.append(line.lower())

    open_file.close()

    final_corpus = open(filename[:-10] + "revised_corpus.csv", "w")

    for item in final_dict1:
        final_corpus.write(item)


def main():
    corpus_unique("Malay_14.24.01_corpus.csv")
    corpus_unique("Iban_14.24.01_corpus.csv")


if __name__ == '__main__':
    main()
