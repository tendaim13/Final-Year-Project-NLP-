import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime 

# This program creates a list of words obtained from the Utusan Borneo website.
# An active internet connection is required to access the websites.
# The references.txt file in the folder contains the links to the articles.
# Ensure the BeautifulSoup4 library is installed on the python version 


corpus = open("references.txt", "r")
j =1 #used to keep track of the current line beig read form the references.txt

now = datetime.now()

curTime = now.strftime("%H.%M.%S")

#Due to the nature of the files, we will create various folders to save the final text from the website
# this is in case we run another corpus throughh the program.
# Each folder will be saved in the format:  Iban_<Current Time> and Malay_<Current Time>
ibanDir = "Iban_" + str(curTime)
malayDir = "Malay_" + str(curTime)
os.mkdir(ibanDir)
os.mkdir(malayDir)

os.mkdir


for line in corpus:
    if( j % 2 == 1):

        if(j == 1):
            page = requests.get(line[3:-1])
        else:
            page = requests.get(line[:-1])

        soup = BeautifulSoup(page.content, 'lxml')
        soup.findAll('article', class_='node node-article node-top_story clearfix')

        stuff = soup.select("p span span span")

        temp = str(j)+"iban.txt" #temporary file used to store unedited text from website

        f = open(temp,'w') 
        for i in range(len(stuff)):
            if(stuff[i] != "\n"):
                f.write(str(stuff[i]))
                f.write("\n")


        f.close()
        #print("i got here")
        #tempFile = str(j) + "iban.txt" 

        edit= open(temp,'r')
        edited = "editedIban" +str(j) +".txt"
        t = open(edited,'w')

        for line in edit:
            liner = edit.readline()
            #print(liner)
            #print(liner[6:-8])
            t.write(liner[6:-9])
            t.write("\n")

        t.close()
        edit.close()
       

        #split the words usingthe space
        sentence = open(edited, "r")
        finalIbanFile = ibanDir+"\\iban"+ str(j) +".txt"
        finalCheck = open(finalIbanFile, "w")

        for line in sentence:
            sent = sentence.readline()
            liner = sent.split(" ")
            for word in liner:
                #print >>finalCheck, word
                finalCheck.write(word)
                finalCheck.write('\n')
            
        sentence.close()
        os.remove(edited)
        os.remove(temp)
        finalCheck.close()
        j= j +1

    
    elif(j % 2 ==0):
      
        page = requests.get(line[:-1])

        soup = BeautifulSoup(page.content, 'lxml')
        soup.findAll('article', class_='node node-article node-top_story clearfix')

        stuff = soup.select("p span span span")

        tempMalay = str(j-1) + "malay.txt"

        f = open(tempMalay,'w') 
        for i in range(len(stuff)):
            f.write(str(stuff[i]))
            f.write("\n")
            #print(stuff[i])

        f.close()

        edit= open(tempMalay,'r')
        edited = "malayEdited" +str(j-1) +".txt"
        t = open(edited,'w')

        for line in edit:
            liner = edit.readline()
            print(liner)
            #print(liner[6:-8])
            t.write(liner[6:-9])
            t.write("\n")

        t.close()
        edit.close()

        #split the words usingthe space
        sentence = open(edited, "r")
        finalMalayFile = malayDir + "\\malaytxt"+ str(j-1) +".txt"
        finalCheck = open(finalMalayFile, "w")

        for line in sentence:
            sent = sentence.readline()
            liner = sent.split(" ")
            for word in liner:
                #print >>finalCheck, word
                finalCheck.write(word)
                finalCheck.write('\n')
            
        sentence.close()
        os.remove(edited)
        os.remove(tempMalay)
        finalCheck.close()
        j= j +1
        



#print(stuff)

#References
''' 
1. https://www.geeksforgeeks.org/python-spilt-a-sentence-into-list-of-words/
2. https://www.crummy.com/software/BeautifulSoup/bs4/doc/
3. https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/#:~:text=Reading%20line%20by%20line,-Using%20readlines()&text=readlines()%20is%20used%20to,split%20it%20into%20separate%20lines.
4. https://stackoverflow.com/questions/743806/how-to-split-a-string-into-a-list

'''
