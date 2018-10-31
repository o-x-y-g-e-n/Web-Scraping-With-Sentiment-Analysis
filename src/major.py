
import nltk
import xml.etree.ElementTree as ET
from lxml import etree
import sys
import codecs
import nltk
from nltk.corpus import stopwords

def find_majority_terms(name):

	default_stopwords = set(nltk.corpus.stopwords.words('english'))
	stemmer = nltk.stem.snowball.SnowballStemmer('english')

	doc = etree.XMLParser(recover=True)
	tree = etree.parse(str(name) + ".xml",doc)

	final_data = []
	words = []

	for df in tree.xpath('//review'):
		subfields = df.getchildren()
		words = nltk.word_tokenize(str(subfields[0].text))
		words = [word for word in words if len(word) > 1]
		words = [word for word in words if not word.isnumeric()]
		words = [word.lower() for word in words]
	#	words = [stemmer.stem(word) for word in words]
		words = [word for word in words if word not in default_stopwords]
		final_data.append(words)

	full_final_words = []

	for w in final_data:
		for x in w:
			full_final_words.append(x)
	#print(full_final_words)

	top_70 = []

	fdist = nltk.FreqDist(full_final_words)
	for word, frequency in fdist.most_common(70):
	 	top_70.append(word)

	remove_tags = ['MD','IN','VBG','VBN','VBZ','RB','JJ','JJS','JJR','RBS','RBR','NNP','NNPS','POS','PRP','PRP$','RP','WP','WP$','WRB','EX','FW','NNS','CD',"''","'","``",":"]

	tagged = nltk.pos_tag(top_70)
	#print(tagged)
	final_list = []

	for i in range(0,len(tagged)):
		if tagged[i][1] not in remove_tags:
			final_list.append(tagged[i][0])
	return final_list