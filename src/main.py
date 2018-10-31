import nltk
import xml.etree.ElementTree as ET
from lxml import etree
import sys
import codecs
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom
from tqdm import tqdm
import os
from overall_rating import *
from major import *

def percentage(part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

major_terms = find_majority_terms("reviews")
print(major_terms)

total_count = [0]*len(major_terms)

positive = [0]*len(major_terms)
negative = [0]*len(major_terms)
neutral = [0]*len(major_terms)
positive_tweet = []
negative_tweet = []
neutral_tweet = []
total_tweets=[]

for i in range(0,len(major_terms)):
	total_tweets.append([])
	for z in total_tweets:
		z.append([])
		z.append([])
		z.append([])

doc = etree.XMLParser(recover=True)
tree = etree.parse('reviews.xml',doc)
for df in tree.xpath('//review'):
		subfields = df.getchildren()
		i=0
		sentences = nltk.sent_tokenize(str(subfields[0].text))
		for term in major_terms:
			for sentence in sentences:
				words = nltk.word_tokenize(sentence)
				if term in words:
					analysis = TextBlob(sentence)
					if(analysis.sentiment.polarity == 0):
						neutral[i] +=1
						total_tweets[i][0].append(sentence)
					elif(analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <=1):
						positive[i] +=1
						total_tweets[i][1].append(sentence)
					elif(analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <=0):
						negative[i]+=1
						total_tweets[i][2].append(sentence)
					total_count[i] +=1

			i+=1
for i in range(0,len(major_terms)):
	print("------------"+major_terms[i]+"-------------\n")
	if(total_count[i] != 0):
		negativea = percentage(negative[i], total_count[i])
	if(total_count[i] != 0):
		neutrala = percentage(neutral[i], total_count[i])
	if(total_count[i] != 0):
		positivea = percentage(positive[i], total_count[i])
	
	print()
	print(str(positivea) + "% people thought it was positive")
	print(str(neutrala) + "% people thought it was neutral")
	print(str(negativea) + "% people thought it was negative")
	#print("--------------------------------------------\n")
	print("---------neutral tweets-------------\n")
	for sr in total_tweets[i][1]:
		print(str(sr) + "\n")
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
	print()

	# total_tweets[i][0] --> neutral
	# total_tweets[i][1] --> positive
	# total_tweets[i][2] --> negative