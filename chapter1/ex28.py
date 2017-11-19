import nltk
from nltk.book import *

def percent(word, text): 
	wordlist = list(filter(lambda x:word.lower() == x.lower(),text))
	return (len(wordlist) / len(text)) * 100.0

print (percent('lord', text3))
