import nltk
from nltk.book import *

ize = list(filter(lambda x: x.endswith('ize'), text6))
containz = list(filter(lambda x: 'z' in x, text6))
containpt = list(filter(lambda x: 'pt' in x, text6))
titlecase = list(filter(lambda x: x[0].isupper() and x[1:].islower(), text6))

print (ize)
print (containz)
print (containpt)
print (titlecase)
