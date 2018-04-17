from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def fun():
	return render_template('b2.html', msg = '')
	
@app.route('/check/', methods = ['GET', 'POST'])
def check():
	a = checker(request.form['str1'])
	return render_template('b2.html', msg = a)
	
def checker(str1):
	
	a = str1.split()
	f = open('b2.txt', 'r')
	b = f.read()
	b = b.split()
	
	cc = 0
	for i in a:
		if i in b:
			cc+=1
			
	perc = str(float(cc)/len(a)*100.0)+"%"
	return perc
	
if __name__ == '__main__':
	app.run()
