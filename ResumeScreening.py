"""
Name: Rubbal Kumar
Description: This program takes a word as input, and outputs a ranked list 
             of the closest words to those words (i.e.  words whose vectors 
             have thehighest cosine similarity compared with the input word). 
             It also outputs the top 10 words, and includes both the word 
             and the cosine similarity between the input word and a 
             given word on the top 10 list.
"""

import nltk
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import time
start_time = time.time()
print('start')




def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
      
    # check length  
    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return("no common elements")
        
        
def similarity(remain):
    text_input = remain

    
    #data = open("glove.6B.50d.txt",  encoding="utf8").readlines()
    
    
    
    lines = {}
    # Reading the text file and processing it
    with open("glove.6B.50d.txt",  encoding="utf8") as f:
        for line in f:
            sent = line.split()
            lines[sent[0]] = sent[1:]
    
    
    results = []
    target = lines[text_input]
    target = [float(i) for i in target]
    target = np.asarray(target)
    
    # Calculating the cosine similarity
    for keys in lines:
        value = lines[keys]
        value = [float(i) for i in value]
        value = np.asarray(value)
        # manually compute cosine similarity
        dot = np.dot(target, value)
        norma = np.linalg.norm(value)
        normb = np.linalg.norm(target)
        cos = dot / (norma * normb)
        
        results.append([cos, keys])
    
    most_similar = sorted(results, reverse = True)[1:110]
    relevent_words = [most_similar[i][1] for i in range(len(most_similar))]
    
    #print('hi')
    return set(relevent_words) 


def read_file():
    stop_words = set(stopwords.words('english'))
    
    file = pd.read_csv('file:///C:/Users/Techno/Desktop/Resume Dataset.csv', encoding = 'ISO-8859-1')
    
    for i in range(0, len(file)):
        read_data = file.iloc[i, 0]
        #print(read_data)
        '''
        with open("Resume7.txt", "r+", encoding="utf8") as file:
        read_data = file.read()'''
        read_data = read_data.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        word_tokens = tokenizer.tokenize(read_data) 
        stemmer = PorterStemmer()
        stem = [stemmer.stem(word_tokens[i]) for i in range(len(word_tokens))]
        lemmatizer=WordNetLemmatizer()
        lemma = [lemmatizer.lemmatize(word_tokens[i]) for i in range(len(word_tokens))]
        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
        filtered_sentence = set(filtered_sentence)
    

        job_keywords = {"b.sc", "javascript", "agile", "css", "html", "mysql", "internship", "json", "python", "communication", "node", "visualization"}
        
        #print ("job_keywords")
        #print(job_keywords)
        
        common = common_member(filtered_sentence, job_keywords)
        common = set(common)
        score = len(common)
        #print(score)
        
        #print ("common len")
        #print(common)
        
        remaining1 = filtered_sentence - common
        remaining = job_keywords - common


        for word in sorted(remaining):
            similar_words = similarity(word)
            #print(similar_words)
            #print(word)
            if similar_words.intersection(remaining1):
                #print('true')
                score += .5
        file.iloc[i, 1] = score
    
    
    file.to_csv('data_final.csv', index=False)
        
    

#print ("remaining len")
#print(remaining)



read_file()


print("--- %s seconds ---" % (time.time() - start_time))