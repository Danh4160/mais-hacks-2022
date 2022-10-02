import numpy as np

class modifiedknn:
    def __init__(self, resume_dataset, processed_pdf_text):
        self.dataset = resume_dataset
        self.text = processed_pdf_text
        self.labels = self.dataset['Category'].values
        self.correlations = {label: 0.0 for label in self.labels}  

    def calculate_correlations(self):
        for i in range(0, len(self.labels)):
            dict_rel_freq = self.dataset.iloc[[i]]['Frequencies Relative'][i]
            label = self.labels[i]
            for word in self.text:
                if word in dict_rel_freq.keys():
                    self.correlations[label] += dict_rel_freq[word]
        return self.correlations

    
