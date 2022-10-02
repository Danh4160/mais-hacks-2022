import numpy as np
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
    def __init__(self, resume_dataset, processed_pdf_text, job_titles):
        self.dataset = resume_dataset
        self.X = processed_pdf_text
        self.y = job_titles
        self.correlations = {}  # Dictionary

    def calculate_correlations(self):
        
        

        # Compare the the common_words_dataset from the knn with the common_words_resume
        return self.correlations

    
