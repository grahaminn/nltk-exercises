import nltk
from nltk.book import *

def index_recursion(stringlistin,searchstr,offset):
	idx = stringlistin.index(searchstr)
	print (idx+offset)
	return index_recursion(stringlistin[(idx+1):],searchstr,offset+idx+1)

index_recursion(sent3, 'the',0)
	
