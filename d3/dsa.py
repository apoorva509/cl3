import hashlib
import random

def isprime(num):
	num = abs(num)
	if num < 2 or num%2 == 0:
		return False
	if num == 2 or num == 3:
		return True
	for i in range(3,int(pow(num,0.5)+1)):
		if num % i == 0:
			return False
	return True

def check_tuple(p, q):
	if not isprime(p):
		print "p is not prime!"
		return False
	if not isprime(q):
		print "q is not prime!"
		return False
	if (p-1)%q != 0:
		print "q is not prime divisor of (p-1)!"
		return False
	return True
	
def get_g(p, q, h):
	for i in range(1,p):
		if pow(i,q)%p==1 and i == pow(h,((p-1)/q))%p:
			return i
	return -1
		

while True:
	print "Enter the parameter tuple <p, q> :"
	p = int(raw_input("p : "))
	q = int(raw_input("q : "))
	
	if not check_tuple(p, q):
		print "Invalid parameter tuple... Try again!"
	else:
		break
		
msg = raw_input("Enter message : ")
m = hashlib.sha1(msg).hexdigest()
print "hash =",m
h = int(m, 16)
print "h =",h

g = get_g(p, q, h)
print "g :",g

while True:
	x = int(raw_input("Enter private key(x) such that 1<x<q : "))
	if x<1 or x>q:
		print "Invalid x! Please try again..."
	else:
		break
		
y = pow(g,x)%p
print "Private key :",[p,q,g,x]
print "Public key :",[p,q,g,y]

k = random.randint(1,q)

#Signature generation
r = (pow(g,k)%p)%q
i=0
while True:
	if(k*i)%q == 1:
		break
	i+=1
s = (i*(h+x*r))%q
	
#Signature Verification
w = 0
while True:
	if(s*w)%q == 1:
		break
	w+=1
u1 = (h*w)%q
u2 = (r*w)%q
v = ((pow(g,u1)*pow(y,u2))%p)%q

if v==r:
	print "Verified : r =",r,"s =",s
else:
	print "Not verified!"
