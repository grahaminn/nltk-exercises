import nltk
from nltk.book import *

fl_words = filter(lambda w: len(w)==4, text5)
fl_frqdist = FreqDist(fl_words)
print (fl_frqdist.most_common(len(fl_frqdist)))
