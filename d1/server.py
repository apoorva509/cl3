import socket

def chunks(ip, n):
	return [ip[i:i+n] for i in range(0,len(ip),n)]
	
def rol(n,b):
	return ((n << b) | (n >> (32-b))) & 0xffffffff
	
def sha1(data):
	bytes = ""
	h0 = 0x67452301
	h1 = 0xEFCDAB89
	h2 = 0x98BADCFE
	h3 = 0x10325476
	h4 = 0xC3D2E1F0
	
	for i in range(len(data)):
		bytes+='{0:08b}'.format(ord(data[i]))
	bits = bytes+"1"
	pBits = bits
	
	while (len(pBits)%512)!=448:
		pBits+="0"
	
	pBits+='{0:064b}'.format(len(bits)-1)
	
	for c in chunks(pBits,512):
		words = chunks(c,32)
		w = [0]*80
		for i in range(0,16):
			w[i] = int(words[i],2)
		for i in range(16,80):
			w[i] = rol(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16],1)
			
		a = h0
		b = h1
		c = h2
		d = h3
		e = h4
	
		for i in range(0,80):
			if 0<=i<=19:
				f = (b&c)|(~b&d)
				k = 0x5A827999
			if 20<=i<=39:
				f = b ^ c ^ d
				k = 0x6ED9EBA1
			if 40<=i<=59:
				f = (b&c) | (b&d) | (c&d)
				k = 0x8F1BBCDC
			if 60<=i<=79:
				f = b ^ c ^ d
				k = 0xCA62C1D6
			
			temp = rol(a,5) + f + e + k + w[i] & 0xffffffff
			e = d
			d = c
			c = rol(b,30)
			b = a
			a = temp
	
		h0 = h0 + a & 0xffffffff
		h1 = h1 + b & 0xffffffff
		h2 = h2 + c & 0xffffffff
		h3 = h3 + d & 0xffffffff
		h4 = h4 + e & 0xffffffff
	
	return "%08x%08x%08x%08x%08x" % (h0,h1,h2,h3,h4)
	
if __name__ == "__main__":

	sock = socket.socket()
	
	server_address = ('127.0.0.1', 10005)
	print 'Starting up on %s port %s' % server_address
	sock.bind(server_address)
	
	sock.listen(1)
	print 'Waiting for a connection...'
	
	connection, client_address = sock.accept()
	
	try:
		print 'Connection from', client_address
		
		recvData = connection.recv(1024)
		recvHash = connection.recv(1024)
		print 'Received Message :: '+str(recvData)
		print 'Received Digest :: '+str(recvHash)
	
	finally:
		connection.close()
		
		calDigest = sha1(recvData)
		
		if(calDigest == recvHash):
			print 'Message Unaltered'
		else:	
			print 'Message Altered'
