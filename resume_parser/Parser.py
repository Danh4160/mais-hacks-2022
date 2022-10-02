# Importing required modules
from genericpath import isfile
import PyPDF2


import docx as wd
import os
import pandas as pd






#def pdf_data(filepath):

    # Creating a word file object
    #wordObj = wd.Document(filepath)


    # Creating a word reader object
    

    # Getting number of pages in pdf file
    #pages = wordReader.numPages

    # Loop for reading all the Pages
    #for i in range(pages):

            # Creating a page object
     #       pageObj = wordReader.getPage(i)

            # Extracting text from page
            # And splitting it into chunks of lines
      #      text = pageObj.extractText()

            # Finally the lines are stored into list
            # For iterating over list a loop is used
       #     for word in text:

                    # Printing the line
                    # Lines are seprated using "\n"
        #            print(word,end="\n\n")

            # For Seprating the Pages
         #   print()

    # closing the pdf file object
    #wordReader.close()

#def printAllWords(directory = r"C:\Users\Ehsan Ahmed\Python Projects\Hackathon AI\mais-hacks-2022\data\word"):

 #   text = ""

  #  for filename in os.listdir():
   #     if filename.endswith(".docx"):
    #        f = os.path.join(directory,filename)
     #       if os.path.isfile(f):
      #          text += pdf_data(f)
          

    #return text


#printAllWords()





    