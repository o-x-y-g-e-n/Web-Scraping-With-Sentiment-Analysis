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


total_count = 0
positive_tweets = []
negative_tweets = []
neutral_tweets = []
major_terms = []
positive =0
negative =0
neutral = 0
stri = input("Enter the string")
major_terms.append(stri)
doc = etree.XMLParser(recover=True)
tree = etree.parse('reviews.xml',doc)
for df in tree.xpath('//review'):
		subfields = df.getchildren()
		sentences = nltk.sent_tokenize(str(subfields[0].text))
		for term in major_terms:
			for sentence in sentences:
				words = nltk.word_tokenize(sentence)
				# print("--WORDS--\n")
				# print(words)
				if term in words:
					analysis = TextBlob(sentence)
					if(analysis.sentiment.polarity == 0):
						neutral +=1
						neutral_tweets.append(sentence)
					elif(analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <=1):
						positive +=1
						positive_tweets.append(sentence)
					elif(analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <=0):
						negative+=1
						negative_tweets.append(sentence)
					total_count +=1

			

print("------------"+str(stri)+"-------------\n")
if(total_count != 0):
	negativea = percentage(negative, total_count)
if(total_count != 0):
	neutrala = percentage(neutral, total_count)
if(total_count != 0):
	positivea = percentage(positive, total_count)
		
print()
print(str(positivea) + "% people thought it was positive")
print(str(neutrala) + "% people thought it was neutral")
print(str(negativea) + "% people thought it was negative")
#print("--------------------------------------------\n")
print("---------neutral tweets-------------\n")
for sr in positive_tweets:
	print(str(sr) + "\n")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print()

	