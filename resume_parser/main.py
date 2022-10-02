# %%
import pandas as pd
import nltk
# Importing the required libraries
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
from model import modifiedknn
# nltk.download()
# %%
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
    df = pd.read_csv("./UpdatedResumeDataSet.csv")
    df = df.groupby(['Category'])['Resume'].apply(lambda x: ','.join(x)).reset_index()
    df = df.replace(r'[^\w\s]|_', '', regex=True)
    df['Frequencies'] = df['Resume'].apply(ProperNounExtractor)
    df['Frequencies Relative'] = df['Frequencies'].apply(Relative_Frequencies)
    return df

# %%
def main():
    df_resume = set_resume_dataset()
    sampleText = df_resume.iloc[[1]]['Frequencies Relative'][1].keys() # output of pdf should be list
    knn = modifiedknn(df_resume, sampleText)
    dict_corr = knn.calculate_correlations()
    return dict_corr

# %%
if __name__ == "__main__":
    main()
