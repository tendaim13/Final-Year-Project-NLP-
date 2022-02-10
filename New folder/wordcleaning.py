import os
import csv
import re

#Porduces all corpora needed for the program to run

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

    
    # we need to remove all english words

    unwanted_words = ['online', 'advertisement', 'toggle',
                      'navigation', '�', 'facebook', 'twitter', 'email', 'print', 'google+', 'google']

# adds all words to one list to prep for processing
    for filename in os.listdir(language_folder):
        new_path = language_folder+"\\"+filename
        if filename.endswith(".txt"):
            open_file = open(new_path, "r")
            for line in open_file:
                if line not in language_dict and line not in unwanted_words:
                    language_dict.append(line[:-1])

            #print(language_dict)

            open_file.close()

            list_of_words = []

            # Removing numbers and punctuation marks from source data

            language_string = ""


            clean_text = []
            for element in language_dict:
                clean_text.append(clean_data(element))

            # print(language_string)

            
            #print(clean_text)
            for word in clean_text:
                # print(word)
                if word.lower() not in unwanted_words:
                    list_of_words.append(word.lower())

            print(list_of_words)

            # create a dictionary with word frequencies
            # this information will be used in the bag of words approach
            '''word_frequency = {language_folder.lower(): 0}
            word_frequency.update(word_freq(list_of_words))

            # creating ids for specific words
            word_id = {language_folder.lower(): 0}
            word_id.update(word_ids(word_frequency))

            dict_file = open(language_folder+"_wordID.csv", "a")
            writer = csv.writer(dict_file)
            for key, value in word_id.items():
                writer.writerow([key, value])

            dict_file.close()

            bag_of_words = {}
            for key, value in word_id.items():
                freq = word_frequency[key]
                bag_of_words[value] = freq

            b_o_w_file = open(language_folder+"_bow_matrix.csv", "a")
            writer = csv.writer(b_o_w_file)
            for key, value in bag_of_words.items():
                writer.writerow([key, value])

            b_o_w_file.close()'''

            open_file = open(language_folder+"_corpus.csv", "a")
            # word_writer = csv.writer(open_file)
            for element in list_of_words:
                # print(element)
                if(len(element) > 1):
                    # word_writer.writerows(element)
                    open_file.write(element)
                    open_file.write(",\n")
            # word_writer.writerow(list_of_words)
            open_file.close()

        # should i have a list of words specific to malay or iban only?
        # iban is preferred as it has the lower number of resources


def main():
    word_cleaning("Iban_")
    word_cleaning("Malay_")


if __name__ == "__main__":
    main()
# References
# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory (opening folder in python)
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary (checking existence of item in dictionary)
# Malay words sourced from https://www.101languages.net/malay/most-common-malay-words/
# https://medium.com/analytics-vidhya/text-preprocessing-for-nlp-natural-language-processing-beginners-to-master-fd82dfecf95
