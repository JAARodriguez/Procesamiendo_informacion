# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:29:26 2021

@author: Alejandro
"""

#import nltk
import re
import fasttext
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def token(N):
    C = {} 
    for i in range(0,len(N)):
        words = []
        #N[i] = word_tokenize(N[i])
        tokens = re.findall('[^\d\s.$+-/:]+',N[i])
        words.extend(tokens)
        C[i] = words
    return C

def stopw(N,stw):
    F = {}
    for i in range(0,len(N)):
        filtered_sentence = []
        for w in N[i]:
            # print(N[i])
            if w not in stop_words:
                filtered_sentence.append(w)
        F[i] = filtered_sentence
    return F

# --- Extraccion datos de los archivos --- #
m1 = 'C:/Users/Alejandro/Desktop/Proyecto final/data/data/tweets.txt'
m2 = 'C:/Users/Alejandro/Desktop/Proyecto final/data/data/users.txt'
m3 = 'C:/Users/Alejandro/Desktop/Proyecto final/data/data/gender.txt'

s1 = []
with open(m1, 'r', encoding='utf-8') as file:
    for Line in file:
        s1.append(Line)
    
s2 = []
with open(m2, 'r', encoding='utf-8') as file:
    for Line in file:
        s2.extend(Line.split())
        
s3 = []
with open(m3, 'r', encoding='utf-8') as file:
    for Line in file:
        s3.append(Line)

# --- Ordenar los usuarios --- #        
us = list(set(s2))
us = list(map(int, us))
us = sorted(us)
us = list(map(str, us))

# c = []
# for i in range(0,len(us)):
#     c.append(s2.count(us[i]))
    
N = {}
for u in range(0,len(us)):
    A = ''
    for n in range(0,len(s2)):
        if us[u] == s2[n]:
            A += s1[n]
            N[u] = A

stop_words = set(stopwords.words('spanish')) 

# --- Generar Tokens --- #
N = token(N)
#word_tokens = word_tokenize(s1) Esta ya no
  
#filtered_sentence = [w for w in word_tokens if not w in stop_words] 
 
# --- Eliminar stop_words --- #
Fs = stopw(N,stop_words)         
  
# for w in word_tokens: 
#     if w not in stop_words: 
#         filtered_sentence.append(w) 
  
# print(word_tokens) 
# print(filtered_sentence) 

# --- Volver a unir tokens en un string --- #
for i in range(0,len(Fs)):
    x = Fs[i]
    s = ' '.join(x)
    Fs[i] = s

# --- Creacion archivo txt --- #
with open('words.txt', "w", encoding='utf-8') as the_file:
    for i in range(0,len(Fs)):
        a = Fs[i]
        the_file.write(a + "\n")

# --- Modelo FastText --- #
model = fasttext.train_unsupervised('words.txt', "cbow")