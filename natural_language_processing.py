# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def prediction(text):
    # Importing the dataset
    dataset = pd.read_csv('file:///C:/Users/Rubbal K. Badhan/Downloads/data_final.csv')
    #df = pd.Series('C:/Users/Rubbal K. Badhan/Downloads/7.txt')
    dataset = dataset.append({'Resume': text, 'Score': 0, 'Category': 0}, ignore_index=True)
    
    # Cleaning the texts
    
    nltk.download('stopwords')
    corpus = []
    for i in range(0, len(dataset.index)):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Resume'][i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)
    
    # Creating the Bag of Words model

    cv = CountVectorizer(max_features = 1500)
    X = cv.fit_transform(corpus).toarray()
    y = dataset.iloc[:, 2].values
    
    # Splitting the dataset into the Training set and Test set

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 50, random_state = None, shuffle = False)
    
    # Fitting Naive Bayes to the Training set
    
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    
    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    
    if (y_pred == 0):
        return ("There is a 0% resume match against this job description")
    elif (y_pred == 1):
        return ("There is a 25% resume match against this job description")
    elif (y_pred == 2):
        return ("There is a 50% resume match against this job description")
    elif (y_pred == 3):
        return ("There is a 75% resume match against this job description")
    else:
        return ("There is a 100% resume match against this job description")
