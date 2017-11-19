import nltk
from nltk.book import text5

twords = filter(lambda e: e.lower().startswith('b'), text5)

print (sorted(set(twords)))

