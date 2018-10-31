
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from xml.dom import minidom
from tqdm import tqdm
import os

#joining connection

browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")

page_no = []
s = "https://www.amazon.com/SanDisk-Cruzer-Frustration-Free-Packaging-SDCZ50-032G-AFFP/product-reviews/B007KFAG8Y/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1"
browser.get(s)

#find total no of pages of reviews
btn =browser.find_elements_by_xpath("//li[contains(@class,'page-button')]/a")
for ele in btn:
	fs = int(ele.text)
	page_no.append(fs)
max_page_no = max(page_no)
					
#fetching all data and storing them into a xml file
#-----
root = minidom.Document()
xml = root.createElement('reviews') #root
root.appendChild(xml)
#-----
id = 1
for i in tqdm(range(1,max_page_no)):
	s = "https://www.amazon.com/SanDisk-Cruzer-Frustration-Free-Packaging-SDCZ50-032G-AFFP/product-reviews/B007KFAG8Y/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(i)
	browser.get(s)
	review_ele = []
	review_ele = browser.find_elements_by_class_name("review")
	for ele in review_ele:
		#-------
		reviewschild = root.createElement('review') #product
		reviewschild.setAttribute('id',str(id))
		xml.appendChild(reviewschild)
		childofreview = root.createElement('review-text')
		#-------
		review_element = ele.find_element_by_class_name("review-text")
		star_element = ele.find_element_by_class_name("review-date")
		# grab the review text
		texti = review_element.text
		childofreview.appendChild(root.createTextNode(texti))
		reviewschild.appendChild(childofreview)
		#print(texti)
		# grab the review date
		tee = star_element.	text
		tee = tee[3:]
		data = tee.split()
		tee = data[2]
		childofreview = root.createElement('review-year')
		childofreview.appendChild(root.createTextNode(tee))
		reviewschild.appendChild(childofreview)
		#print(tee)
		#print("-----")
		id=id+1	
		#creating XML file
		xml_str = root.toprettyxml(indent="\t")
		save_path_file = "reviews.xml"
		with open(save_path_file,"w",encoding='utf8') as f:
			f.write(xml_str)


		


