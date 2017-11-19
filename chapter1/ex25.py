import nltk

sent = ['she','sells','sea','shells','by','the','sea','shore']
sh = list(filter(lambda x: x.startswith('sh'), sent))
overfour = list(filter(lambda x: len(x) > 4, sent))

print (sh)
print (overfour)
