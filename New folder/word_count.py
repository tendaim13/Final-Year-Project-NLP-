import os
import csv

#Outputs the total number of words in each corpus
# saves them to a file called: <Filename>_words_count.csv


def word_count(filename):

    words_counted = {}

    open_file = open(filename, "r")
    for line in open_file:
        if line[:-1] not in words_counted:
            words_counted[line[:-1]] = 1
        else:
            words_counted[line[:-1]] = words_counted[line[:-1]] + 1

    word_count_file = open(filename[:-4]+"words_count.csv", "w")
    writer = csv.writer(word_count_file)
    for key, value in words_counted.items():
        writer.writerow([key, value])

    word_count_file.close()
    print(words_counted)


def main():

    word_count("Malay_corpus.csv")
    word_count("Iban_corpus.csv")


if __name__ == "__main__":
    main()
# References
# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory (opening folder in python)
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary (checking existence of item in dictionary)
# Malay words sourced from https://www.101languages.net/malay/most-common-malay-words/
# https://medium.com/analytics-vidhya/text-preprocessing-for-nlp-natural-language-processing-beginners-to-master-fd82dfecf95
