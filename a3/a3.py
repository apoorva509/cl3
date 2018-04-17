from flask import Flask, render_template, request
from bitstring import BitArray

app = Flask(__name__)

@app.route('/')
def fun():
	return render_template('a3.html', msg1 = '', msg2 = '')
	
@app.route('/check/', methods = ['GET', 'POST'])
def check():
	
	a = int(request.form['str1'])
	b = int(request.form['str2'])
	i,bi = booth(a,b,8,8)
	return render_template('a3.html', msg1 = str(i), msg2 = str(bi))
	
def booth(m, q, x, y):
	
	tlen = x+y+1
	
	mA = BitArray(int = m, length = tlen)
	A = mA << (y+1)
	mA1 = BitArray(int = -m, length = tlen)
	S = mA1 << (y+1)
	
	P1 = BitArray(int = q, length = x)
	P1.prepend(BitArray(int = 0, length = y))
	P = P1 << 1
	
	for i in range(1,y+1):
		if(P[-2:]=='0b01'):
			P = BitArray(int = P.int + A.int, length = tlen)
		elif( P[-2:] == '0b10' ):
			P = BitArray(int = P.int + S.int, length = tlen)
		P = BitArray(int = (P.int >> 1), length = P.len)
		
	P = P[:-1]
	return P.int, P.bin
	
	
if __name__ == '__main__':
	app.run()
