import nltk
import xml.etree.ElementTree as ET
from lxml import etree
import sys
import codecs
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

def percentage(part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

def rating_calculator(val,count):
	positive = 0
	wpositive = 0
	spositive = 0
	negative = 0
	wnegative = 0
	snegative = 0
	neutral = 0

		
	analysis = TextBlob(str(val))
	if (analysis.sentiment.polarity == 0):
		neutral +=1
	elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
		wpositive +=1
	elif(analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
		positive +=1
	elif(analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
		spositive +=1
	elif(analysis	.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
		wnegative +=1
	elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
		negative +=1
	elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
		snegative +=1
	count+=1
	NoOfTerms = count

	 # finding average of how people are reacting
	positive = percentage(positive, NoOfTerms)
	wpositive = percentage(wpositive, NoOfTerms)
	spositive = percentage(spositive, NoOfTerms)
	negative = percentage(negative, NoOfTerms)
	wnegative = percentage(wnegative, NoOfTerms)
	snegative = percentage(snegative, NoOfTerms)
	neutral = percentage(neutral, NoOfTerms)

	print()
	print("Detailed Report: ")
	print(str(spositive) + "% people thought it was strongly positive")
	print(str(positive) + "% people thought it was positive")
	print(str(wpositive) + "% people thought it was weakly positive")
	print(str(neutral) + "% people thought it was neutral")
	print(str(wnegative) + "% people thought it was weakly negative")
	print(str(negative) + "% people thought it was negative")
	print(str(snegative) + "% people thought it was strongly negative")
