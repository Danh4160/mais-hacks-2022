
#import tabula as tb
#tb.convert_into(r"C:\Users\Ehsan Ahmed\Python Projects\Hackathon AI\mais-hacks-2022\data\CV.pdf", "demo.csv", pages="all", output_format="csv")

from PyPDF2 import PdfReader

import re


def convert(filename):

    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"


    #text2 = re.split(';|•.:_=-/|\*|\\n', text)

    text2 = re.split('\n', text)

    text2prime = []

    for txt in text2:
        
        txt = re.sub(r'\)', '', txt)
        txt = re.sub(r'\(', '', txt)
        txt = re.sub(', ', '\n', txt)
        txt = re.sub('•', '', txt)
        txt = re.sub('—', '', txt)
        txt = re.sub('-', '', txt)
        txt = re.sub('–', '', txt)
        #txt = re.sub('/', '', txt) #fix
        txt = re.sub(':', '', txt) 
        txt = re.sub('“', '', txt) 
        txt = re.sub('”', '', txt) 
        txt = re.sub('/', '', txt) 
        text2prime.append(txt)

    #text2 = re.sub(',', '', text2)

    #text2 = re.sub(r'\W+', '', text)


    text3 = ""
    for line in text2prime:
        words = line.split(" ")
        for word in words:
            if (word != " " and len(word.strip()) != 0 and word != '\n'):
                text3 += word.strip() + "\n"

    return text3

#words = text.split(" ")

#text2 = ""
#for word in words:
#    text2 += word.strip() + "\n"

#text3 = text2.splitlines()

#for line in text3:
#    if (line.isalnum):
#        print(line)

