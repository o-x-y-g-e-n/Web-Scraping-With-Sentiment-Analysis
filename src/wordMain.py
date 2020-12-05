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
def word_maini(stri,f_name):
	total_count = 0
	positive_tweets = []
	negative_tweets = []
	neutral_tweets = []
	major_terms = []
	positive =0
	negative =0
	neutral = 0
	major_terms.append(stri)
	doc = etree.XMLParser(recover=True)
	tree = etree.parse(f_name,doc)
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
	print("coount iis "+str(total_count))
	return negative_tweets,positive_tweets,neutral_tweets