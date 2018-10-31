# Sentiment Analysis of product reviews from amazon.com


# Documentation

# Functionality of the project :
-> Find the polarity of the aspect terms using Top 70 most used words concept.
-> Allows you to view the polarity of the specific aspect. (for ex. Battery life)

# Technologies used:
1) NLTK (http://www.nltk.org/)
2) TextBlob (http://textblob.readthedocs.io/en/dev/)
3) Minidom and XmlElementTree (https://wiki.python.org/moin/MiniDom)

# grab_reviews.py
-> It fetches the review from the amazon.com review link and store them in a XML format file names 'reviews.xml'

# major.py
-> It fetches top most used 70 words from the all the reviews. Do POS(part of speech) Tagging and keep all nouns,verbs
  and other appropriate words.

# overall_rating.py
-> It performs sentimental anaylsis on overall reviews. Seperate them in 7 categories, and show the results.


 
