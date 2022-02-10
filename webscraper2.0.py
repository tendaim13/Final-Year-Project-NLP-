#import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge
from msedge.selenium_tools import EdgeOptions
import string
import os
from datetime import datetime
import requests


def syntax_remover(original_text):

    final_list = []
    # print(original_text)
    for word in original_text:
        if word is string.punctuation or word.isdigit():
            print(word)
        else:
            final_list.append(word)
    '''for i in range(len(original_text)):

        if original_text[i] is string.punctuation or original_text[i].isdigit():
            # print(original_text[i])
            del original_text[i]
        else:
            final_list.append(original_text[i])
        elif len(original_text[i].split(" ")) > 1:

            for word in original_text[i]:
                if not (word is string.punctuation or word.isdigit()):
                    final_list.append(word)'''

    return final_list


def web_extract(filename, folder):

    corpus = open(filename, "r")

    print("\n\n\n\n\nGot past\n\n\n")

    if "Iban" in folder:
        start_point = 0
    else:
        start_point = 3

    i = 1
    # file structure requires it
    for line in corpus:
        '''options = EdgeOptions()
        options.use_chromium = True
        driver = Edge("C:\Windows\msedgedriver.exe")'''

        print(line)
        # driver.get(line[3:])
        driver = requests.get(line[start_point:-1])
        #contents = driver.page_source
        # print(contents)
        soup = BeautifulSoup(driver.content, 'lxml').text
        # print(soup)
        new_text = []
        new_text = soup.split()
        print(new_text)

        final_list = syntax_remover(new_text)
        # print(final_list)

        final_file = folder+"\\article"+str(i)+".txt"
        writing_file = open(final_file, "w")
        # print(final_list)

        for item in final_list:
            # print(item)
            writing_file.write(item)
            writing_file.write('\n')
        writing_file.close()
        # driver.quit()
        start_point = 0

        i = i + 1
    print("done")


def main():
    print("starting")

    now = datetime.now()

    curTime = now.strftime("%H.%M.%S")

    # Due to the nature of the files, we will create various folders to save the final text from the website
    # this is in case we run another corpus throughh the program.
    # Each folder will be saved in the format:  Iban_<Current Time> and Malay_<Current Time>
    ibanDir = "Iban_" + str(curTime)
    malayDir = "Malay_" + str(curTime)
    os.mkdir(ibanDir)
    os.mkdir(malayDir)

    os.mkdir

    web_extract("references.txt", malayDir)
    web_extract("iban_references.txt", ibanDir)


if __name__ == "__main__":
    main()
