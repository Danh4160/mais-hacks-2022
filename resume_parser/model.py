# %% 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

np.random.seed(1234)

# class KNN:
#     def __init__(self, X, y, k=1):
#         self.model = KNeighborsClassifier(n_neighbors=k)
#         self.X = X
#         self.y = y

#     def fit_data(self):
#         self.model = self.model.fit(self.X, self.y)
    
#     def predict_label(self, xX):
#         return self.model.predict(X)

#     def split_train_test(self, X, y, test_size):
#         return train_test_split(X, y, test_size=test_size, random_state=1, shuffle=True)

    
class modifiedknn:
    def __init__(self, most_common_words_per_category, job_title):
        self.common_words_dataset = most_common_words_per_category
        self.target_category = job_title

    def get_correlation(self, common_words_resume):
        correlation = 0.0

        return correlation

    def set_relative






    

# data features are the frequency of each
# %%
