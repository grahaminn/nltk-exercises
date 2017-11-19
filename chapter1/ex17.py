import nltk
from nltk.book import text9

def findsentenceslicefrompost(text, begin,end):
	if ((begin == 0 or '.' in text[begin]) and (end==len(text) or '.' in text[end])):
		return text[begin:end]

	if not (begin == 0 or '.' in text[begin]): 
		begin -= 1
	if not (end == len(text) or '.' in text[end]):
		end += 1
	return findsentenceslicefrompost(text, begin, end)

sunsetidx = text9.index('sunset')

print (findsentenceslicefrompost(text9, sunsetidx, sunsetidx+1))
