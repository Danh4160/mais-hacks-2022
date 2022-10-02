# %%
import pandas as pd
import nltk
# Importing the required libraries
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
#nltk.download()
from textblob import TextBlob


def ProperNounExtractor(text):
    
    frequencies = {}
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
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
        

df = pd.read_csv("./UpdatedResumeDataSet.csv")

original = df
##print(df.head)

# df.loc[-1] = ['HI', 'SHEESH']  # adding a row
# df.index = df.index + 1  # shifting index

# df.loc[-1] = ['HI', 'HOHOHOHO, i am good at this maybe?????']  # adding a row
# df.index = df.index + 1  # shifting index

df = df.groupby(['Category'])['Resume'].apply(lambda x: ','.join(x)).reset_index()



df = df.replace(r'[^\w\s]|_', '', regex=True)

df['Frequencies'] = df['Resume'].apply(ProperNounExtractor)

df['Frequencies Relative'] = df['Frequencies'].apply(Relative_Frequencies)





# %%