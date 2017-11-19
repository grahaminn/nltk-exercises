import nltk
from nltk.book import *

def vocab_size(text):
	lowertxt = nltk.Text([w.lower() for w in text])
	return len(set(lowertxt))

print (vocab_size(text1))

print (vocab_size(text2))

print (vocab_size(text3))

print (vocab_size(text5))

print (vocab_size(text8)) 
