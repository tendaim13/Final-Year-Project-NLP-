import os
import csv
import nltk
import re

from nltk.tokenize import word_tokenize  # text cleaning


def clean_data(data_set):
    # removes any numbers or punctuation marks as we do not need them for this analysis
    return re.sub('[^a-zA-Z]', ' ', data_set)


def word_ids(data_Set):
    # make sure the word is unique

    revised_set = {}
    i = 0
    for word in data_Set:
        if word.lower() not in revised_set and word.lower() != '':
            revised_set[word.lower()] = i
            i += 1
    # print(revised_set)
    return revised_set


def word_freq(data_set):
    # Calculates word frequency in given document

    revised_freq = {'': 0}

    for word in data_set:
        if word.lower() in revised_freq and word.lower() != '':
            # print(word.lower())
            revised_freq[word.lower()] = revised_freq[word.lower()] + 1
        else:
            revised_freq[word.lower()] = 1

    return revised_freq


def word_cleaning(language_folder):
    # opens all documents formed,
    # counts number of words
    # counts the frequency of each word
    # tallies total to dictionary of words
    # creates our new corpus

    language_dict = []

    words = set(nltk.corpus.words.words())

    list_of_words = {}

    # we need to remove all english words

    unwanted_words = ['Online', 'Advertisement', 'Toggle',
                      'navigation', '�', 'Facebook', 'Twitter', 'Email', 'Print', 'Google+', 'Google']

# adds all words to one list to prep for processing
    for filename in os.listdir(language_folder):
        new_path = language_folder+"\\"+filename
        if filename.endswith(".txt"):
            open_file = open(new_path, "r")
            for line in open_file:
                if line not in language_dict and line not in unwanted_words:
                    language_dict.append(line[:-1])
            print(len(language_dict))
            list_of_words[filename] = len(language_dict)

            language_dict = []

            open_file.close()

    b_o_w_file = open(language_folder+"_unique.csv", "w")
    writer = csv.writer(b_o_w_file)
    for key, value in list_of_words.items():
        writer.writerow([key, value])
    # should i have a list of words specific to malay or iban only?
    # iban is preferred as it has the lower number of resources


def main():
    word_cleaning("Iban_14.24.01")
    word_cleaning("Malay_14.24.01")


if __name__ == "__main__":
    main()
# References
# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory (opening folder in python)
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary (checking existence of item in dictionary)
# Malay words sourced from https://www.101languages.net/malay/most-common-malay-words/
# https://medium.com/analytics-vidhya/text-preprocessing-for-nlp-natural-language-processing-beginners-to-master-fd82dfecf95
