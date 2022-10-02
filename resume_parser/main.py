
import pandas as pd
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
from model import modifiedknn
import os
import pandas as pd
import matplotlib.pyplot as plt
import math
# nltk.download()

def ProperNounExtractor(text):
    frequencies = {}
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word.lower() not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NN': # If the word is a proper noun
                if word in frequencies.keys():
                    frequencies[word]+=1
                else:
                    frequencies[word]=1
    return frequencies
    
def Relative_Frequencies(frequency):
    total=sum(frequency.values())
    new={}
    for word, frequencies in frequency.items():
        new_frequencies = frequencies/total
        new[word] = new_frequencies
    return new
        
def set_resume_dataset():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "./data/UpdatedResumeDataSet.csv"))
    df = df.groupby(['Category'])['Resume'].apply(lambda x: ','.join(x)).reset_index()
    df = df.replace(r'[^\w\s]|_', '', regex=True)
    df['Frequencies'] = df['Resume'].apply(ProperNounExtractor)
    df['Frequencies Relative'] = df['Frequencies'].apply(Relative_Frequencies)
    return df

def main(pdf_text):
    df_resume = set_resume_dataset()
    knn = modifiedknn(df_resume, pdf_text)
    dict_corr = knn.calculate_correlations()
    dict_corr.update((key, value*100) for key, value in dict_corr.items())
    create_graph(dict_corr)
    
def create_graph(dict_corr):
    keys = dict_corr.keys()
    keys_list = list(keys)
    values = dict_corr.values()
    values_list = list(values)

    plt.barh(keys_list, values_list)
    plt.title("Correlation between your Resume and different positions.")
    plt.xlabel('Correlation (%)')
    plt.ylabel('Position')
    plt.show()

