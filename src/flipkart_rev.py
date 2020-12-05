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
from selenium.webdriver.support import expected_conditions as EC
from contextlib import closing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Firefox
from src.majority import find_majority_terms
from src.percentage import percentage
from src.remove_non_ascii import remove_non_ascii_1
def flipkart_rev(url_info):
	try:
		with closing(Firefox()) as browser:
			site = url_info
			browser.get(site)
			id=1
			root = minidom.Document()
			xml = root.createElement('reviews') #root
			root.appendChild(xml)
			for count in range(1, 20):
				nav_btns = browser.find_elements_by_class_name('_33m_Yg')

				button = ""

				for btn in nav_btns:
					number = int(btn.text)
					if(number==count):
						button = btn
						break

				button.send_keys(Keys.RETURN)
				WebDriverWait(browser, timeout=10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_2xg6Ul")))

				read_more_btns = browser.find_elements_by_class_name('_1EPkIx')
				

				for rm in read_more_btns:
					browser.execute_script("return arguments[0].scrollIntoView();", rm)
					browser.execute_script("window.scrollBy(0, -150);")
					rm.click()

				page_source = browser.page_source

				soup = BeautifulSoup(page_source, "lxml")
				ans = soup.find_all("div", class_="_3DCdKt")
				for tag in ans:
					title = (tag.find("p", class_="_2xg6Ul").string)
					content = tag.find("div", class_="qwjRop").text
					content = content[15:-7]
					votes = tag.find_all("span", class_="_1_BQL8")
					upvotes = int(votes[0].string)
					downvotes = int(votes[1].string)	
					reviewschild = root.createElement('review') #product
					reviewschild.setAttribute('id',str(id))
					xml.appendChild(reviewschild)
					childofreview = root.createElement('review-text')
					#-------
					# grab the review text
					texti = content		
					childofreview.appendChild(root.createTextNode(texti))
					reviewschild.appendChild(childofreview)
					#print(texti)
					# grab the review date
					id=id+1	
					#creating XML file
					xml_str = root.toprettyxml(indent="\t")
					save_path_file = "flipkart_reviews.xml"
					with open(save_path_file,"w",encoding='utf8') as f:
						f.write(xml_str)
	except Exception as e:
		print(e)
		return
