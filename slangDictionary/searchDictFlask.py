from flask import Flask,render_template,redirect, url_for, request
from DictionarySearch import searchDict
#import json
app = Flask(__name__)

@app.route('/',methods=("POST","GET"))
def searchQuery():
	error = None
	if request.method == 'POST':
		if len(request.form['searchbox']) == 0:
			error = 'Search initiated on empty field! Please try again.'
		else:
			return redirect(url_for('resultFunc',slang = request.form['searchbox']))
	return render_template('search.html', error=error)

@app.route('/result<slang>',methods=("POST", "GET"))
def resultFunc(slang):
	#slang = input("Enter muhavara/slang:")
	result = searchDict(slang) 
	print(result)
	return 	render_template('searchDisplay.html',  tables=[result.to_html(classes='data')], titles=result.columns.values) 

#if __name__ == '__main__':
#	app.run()
