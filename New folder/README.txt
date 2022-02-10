Low Resource Natural Language Identification -Using Malay and Iban.
===================================================================================================================================================
Dependencies:
    Python 
    numpy
    pandas
    BeautifulSopu4
    Collections
    math
    string
    pathlib

To install Dependencies:
        pip install <dependency>
        or
        npm -i <dependency>

==================================================================================================================================================

To run pyhton programs:
    python <NameOfFile>


1. The Main Program is the similarity_calc.py 
2. The rest of the files can be used to rebuild the corpus from scratch using the following order:
            webscraper2.0.py => gets the words from the websites and saves them to a folder named under the <Language>_<Current_time>
            |
            wordcleaning.py =>  cleans the raw data to produce the needed corpora
            |
            word_unique.py =>(optional) creates csv file with article size
            |
            corpus_unique.py => creates the 2 other corpora required for the 2 approach
            |
            optional - tfidf.py => runs through the folders to establish simlarities of the original documents to the corpora

======================================================================================================================================================
