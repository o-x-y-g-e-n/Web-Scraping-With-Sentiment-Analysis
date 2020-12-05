# Web Scraping with Sentiment Analysis
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://bitbucket.org/lbesson/ansi-colors) [![GitHub license](https://img.shields.io/github/license/o-x-y-g-e-n/Web-Scraping-With-Sentiment-Analysis)](https://github.com/o-x-y-g-e-n/Web-Scraping-With-Sentiment-Analysis/blob/master/LICENSE) [![GitHub contributors](https://img.shields.io/github/contributors/o-x-y-g-e-n/Web-Scraping-With-Sentiment-Analysis)](https://GitHub.com/o-x-y-g-e-n/Facebook-AutoReply-Bot/graphs/contributors/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/o-x-y-g-e-n/badges/)
![alt text](https://i.ibb.co/NLN8f4X/undraw-sentiment-analysis-jp6w.png)
The program helps scrape reviews from websites like
* amazon.com
* flipkart.com
* imdb.com
identify the `aspect terms` from the fetch reviews and then classify the reviews w.r.t to aspect terms and their `polarity` (positive, negative & netural) 

### Tech

The software uses a number of open source projects to work properly:

* [Python3] - Python is an interpreted, high-level and general-purpose programming language.
* [Selenium] - Selenium automates browsers. 
* [Natural Language Toolkit (NLTK)] - NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English 
* [TextBlob] - library for processing textual data
* [Flask] - Flask is a micro web framework written in Python.
* [Chart.js] - Simple yet flexible JavaScript charting for designers & developers
* [Requests] - Requests is an elegant and simple HTTP library for Python, built for human beings.

### Installation

It requires [Python3](https://www.python.org/downloads/release/python-377/) v3+ to run.

```sh
$ cd Web-Scraping-With-Sentiment-Analysis
$ pip3 install -r requirements.txt 
```
You need to install the below softwares / libraries manually.
Download the following dependencies
- BeautifulSoup4 - [Download](https://pypi.org/project/beautifulsoup4/)
- NLTK with all data [Download](https://www.nltk.org/install.html)

### Execution
1. Download `chromedriver` from here according to your Chrome Version & Operating System.
2. Setup the absolute path of the driver in `config.ini` file using your favourite text editor. Something like this.
    ```
    [selenium]
    chromedriver = /home/shivam/Desktop/chromedriver
    ```
3. From the root directory, execute the following command
    ```sh
    $ python index.py
    ```
    Now, Navigate to `localhost:5000` to open the GUI.
4. Select the website for which you want to fetch the reviews
-[ ] Amazon
-[ ] Flipkart
-[ ] Imdb
5. Make sure you enter the `review` page URL for the link. 

### Images
![alt text](https://i.ibb.co/2v9C35N/Screenshot-from-2020-12-05-16-35-28.png)
![alt text](https://i.ibb.co/0VHdjXP/Screenshot-from-2020-12-05-16-35-42.png)
![alt text](https://i.ibb.co/qDFPjWQ/Screenshot-from-2020-12-05-16-36-01.png)

### Demo
[![Video](https://img.youtube.com/vi/I39z1mXaer8/0.jpg)](https://www.youtube.com/watch?v=I39z1mXaer8)

### Improvements
-[ ] Add more websites
-[ ] Update Scrapers 


License
----

MIT
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/o-x-y-g-e-n/)

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Python3]: <https://www.python.org/downloads/>
   [Selenium]: <https://www.selenium.dev/>
   [Natural Language Toolkit (NLTK)]: <https://www.selenium.dev/>
   [TextBlob]: <https://textblob.readthedocs.io/en/dev/>
   [Flask]: <https://flask.palletsprojects.com/en/1.1.x/>
   [Chart.js]: <https://www.chartjs.org/>
   [Requests]: <https://requests.readthedocs.io/en/master/>
   