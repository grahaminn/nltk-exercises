import nltk
from nltk.book import *

print (nltk.Text([w.lower() for w in text5]).collocations()) 
