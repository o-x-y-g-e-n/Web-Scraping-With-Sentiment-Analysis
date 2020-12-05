from index import *
from src.amazon_main import amazon_main
from src.amazon_rev import amazon_rev
from src.flipkartMain import flipkart_main
from src.flipkart_rev import flipkart_rev
from src.majority import find_majority_terms
from src.movieMain import movie_main
from src.movie_rev import movie_rev
from src.percentage import percentage
from src.remove_non_ascii import remove_non_ascii_1
from src.wordMain import word_maini
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/results",methods=['POST','GET'])
def results():
	# grabbing amazon reviews
	global ftotal_tweets
	global fpositive
	global fnegative
	global fmajor_terms
	global fnetural
	global f_name
	url_info = str(request.args.get('url'))
	if(request.args.get('amazon') == 'on'):
		amazon_rev(url_info)
		ftotal_tweets,fpositive,fnegative,fnetural,fmajor_terms = amazon_main()
		f_name = "reviews.xml"
	elif(request.args.get('imdb') == 'on'):
		movie_rev(url_info)
		f_name = "movie_reviews.xml"
		ftotal_tweets,fpositive,fnegative,fnetural,fmajor_terms = movie_main()
	elif(request.args.get('flipkart') == 'on'):
		print("I am into flipkart page")		
		flipkart_rev(url_info)
		f_name = "flipkart_reviews.xml"
		ftotal_tweets,fpositive,fnegative,fnetural,fmajor_terms = flipkart_main()
		print(len(ftotal_tweets[0]))
	return redirect(url_for('eachValue',id=1))

@app.route('/results/<id>')
def eachValue(id):
	print(ftotal_tweets)
	id1 = int(id)
	major_term = str(fmajor_terms[id1-1])
	positive_temp = ftotal_tweets[id1-1][1]
	negative_temp = ftotal_tweets[id1-1][2]
	netural_temp = ftotal_tweets[id1-1][0]
	total = len(positive_temp) + len(negative_temp) + len(netural_temp)
	print("total ==> " + str(total) +"\n")	
	labels=[]
	labels.append('positive')
	labels.append('negative')
	labels.append('neutral')
	values = []
	values.append(100* len(positive_temp)/total)
	values.append(100* len(negative_temp)/total)
	values.append(100* len(netural_temp)/total)
	return render_template('anaylse.html',values=values,labels=labels,id=id1,major_terms=fmajor_terms,major_term=major_term,negative=negative_temp,positive=positive_temp,neutral=netural_temp)

@app.route('/word_main')
def word_main():
	global negativeA
	global positiveA
	global neutralA
	val = str(request.args.get('search_word'))
	if(len(val) == 0):	
		pass
	negativeA,positiveA,neutralA = word_maini(val,f_name)
	print(negativeA)
	labels=[]
	labels.append('positive')
	labels.append('negative')
	labels.append('neutral')
	values = []
	total = len(positiveA) + len(negativeA) + len(neutralA)
	values.append(100* len(positiveA)/total)
	values.append(100* len(negativeA)/total)
	values.append(100* len(neutralA)/total)
	print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
	return render_template('word_main.html',values=values,labels=labels,val=val,major_terms=fmajor_terms,negative=negativeA,positive=positiveA,neutral=neutralA)
