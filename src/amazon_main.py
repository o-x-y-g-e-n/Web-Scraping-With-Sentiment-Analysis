import nltk,re,time,sys	,codecs,os,requests
import xml.etree.ElementTree as ET
from lxml import etree
from nltk.corpus import stopwords
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom
from tqdm import tqdm
import pandas as pd
from pandas import ExcelWriter
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from contextlib import closing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from src.majority import find_majority_terms
from src.percentage import percentage
from src.remove_non_ascii import remove_non_ascii_1
def percentage(part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

def amazon_main():
	major_terms = find_majority_terms('reviews')
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
	return total_tweets,positive,negative,neutral,major_terms	