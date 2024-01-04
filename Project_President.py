# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:03:18 2021

@author: manya
"""
import nltk
from nltk.corpus import inaugural
inaugural.fileids()
from nltk.corpus import stopwords
stopwords.words("english")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
def remove_stopwords(text):
    text=text.lower()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
 
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    #print(word_tokens)
    return (filtered_sentence)

def remove_Punc(text):
    words = [word for word in text if word.isalpha()]
    return(words)

def count_sentence(text):
    sentences= nltk.sent_tokenize(text)
    return(len(sentences))

def count_words(text):
    return(len(text))

def count_characters(text):
     return(len(text))

def frequency(text):
    Frequency=nltk.FreqDist(text)
    print(Frequency)
    most=Frequency.most_common(3)
    return(most)

print("Details of President Roosevelt")
File1=inaugural.raw('1941-Roosevelt.txt')
File2=remove_stopwords(File1)
print("\nContent of File after reomoving Stopwords\n")
print(File2)
File3=remove_Punc(File2)
print("\nContent of File after reomoving Punctuations\n")
print(File3)
print("\nNumber of characters=",count_characters(File1))
print("Number of words=",count_words(File3))
print("Number of sentences=",count_sentence(File1))
freq=frequency(File3)
print("Top three words  : ",freq)

print("\nDetails of President Kennedy")
File1=inaugural.raw('1961-Kennedy.txt')
File2=remove_stopwords(File1)
print("\nContent of File after reomoving Stopwords\n")
print(File2)
File3=remove_Punc(File2)
print("\nContent of File after reomoving Punctuations\n")
print(File3)
print("\nNumber of characters=",count_characters(File1))
print("Number of words=",count_words(File3))
print("Number of sentences=",count_sentence(File1))
freq=frequency(File3)
print("Top three words  : ",freq)

print("\nDetails of President Nixon")          
File1=inaugural.raw('1973-Nixon.txt')
File2=remove_stopwords(File1)
print("\nContent of File after reomoving Stopwords\n")
print(File2)
File3=remove_Punc(File2)
print("\nContent of File after reomoving Punctuations\n")
print(File3)
print("\nNumber of characters=",count_characters(File1))
print("Number of words=",count_words(File3))
print("Number of sentences=",count_sentence(File1))
freq=frequency(File3)
print("Top three words  : ",freq)
