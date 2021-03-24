
"""
 Import Library
------------------------------------------------------------------------------
"""
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag
import dask.dataframe as ddf
import re
import sys
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import math
import json
import numpy as np
import os


"""
Filtering and Preprocessing function
------------------------------------------------------------------------------
"""

stop_words = set(stopwords.words('english'))
tokenizer = nltk.RegexpTokenizer(r"\w+")

"""
return a string lower
"""
def lower_string(text):
    return text.lower()

"""
Remove stop_words
"""
def  remove_stop_words(text):
    word_tokens = word_tokenize(text)
    clean_stopwords = [w for w in word_tokens if w not in stop_words and w.isalpha() and len(w) > 1]
    return " ".join(clean_stopwords)

"""
Remove punctuation
"""
def remove_punctuation(text):
    text = tokenizer.tokenize(text)
    clean_punctuation = ' '.join(text)
    return clean_punctuation

"""
Remove stemming with ntlk library
"""
def remove_stemming(text):
    ps = PorterStemmer()
    words = word_tokenize(text)
    stem_sentence=[]
    for w in words:
        stem_sentence.append(ps.stem(w))
    text = " ".join(stem_sentence)
    return text

"""
This function has been used to more specifically remove certain things from the text.
This function removes all verbs, in the general form or in the form in ing, it also removes comparatives, major and superlatives,
It also removes all pronouns and possessive pronouns such as "whose" or temporal adverbs such as "when".

"""
def remove_adverbs(text):
    remove = ['TO','JJ', 'FW', 'WDT', 'WP', 'WP$', 'WRB', 'CC', 'IN', 'PRP$', 'PRP', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'UH', 'MD', 'PDT']
    sentence = nltk.word_tokenize(text)
    sent = pos_tag(sentence)
    sent_clean = [x for (x,y) in sent if y not in remove]
    lemma = ' '.join(sent_clean)
    return lemma

"""
We created only one function in order to assolve the whole cleaning process
"""
def global_cleaning(text):
    text = lower_string(text)
    text = remove_punctuation(text)
    text = remove_stop_words(text)
    text = remove_adverbs(text)
    text = remove_stemming(text)
    text = re.sub(r'[^a-zA-z]', ' ', text).strip()
    return text

"""
Try and except has been inserted to take into account the eventuality
that for some reason the dataset encounters nan or numbers that would cause the code to fail.
The nan's and numbers have already been eliminated in the initial filtering, this is just an additional safety measure.
"""
def flat_words(dataframe):
    flat_words = []
    for single_review in tqdm(dataframe.Text):
        try:
            for word in single_review.split(' '):
                flat_words.append(word)

        except:
            print("A number occurred")
            pass
    return flat_words
