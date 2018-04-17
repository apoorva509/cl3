import threading
import sys
import time


class sema(object):
	
	def __init__(self,initial):
		self.lock=threading.Condition(threading.Lock())
		self.value = initial
		
	def up(self):
		with self.lock:
			self.value+=1
			self.lock.notify()
			
	def down(self):
		with self.lock:
			while self.value==0:
				self.lock.wait()
			self.value-=1
		
class chop(object):

	def __init__(self,number):
		self.lock = threading.Condition(threading.Lock())
		self.number=number
		self.user=-1
		self.taken=False
		
	def take(self,user):
		with self.lock:
			while self.taken == True:
				self.lock.wait()
			self.user=user
			self.taken=True
			print("p[%s] took c[%s]\n" % (user, self.number))
			self.lock.notifyAll()
			
	def drop(self,user):
		with self.lock:
			while self.taken == False:
				self.lock.wait()
			self.user=-1
			self.taken=False
			("p[%s] dropped c[%s]\n" % (user, self.number))
			self.lock.notifyAll()
				
		
class phil(threading.Thread):
	
	def __init__(self,number,left,right,butler):
		threading.Thread.__init__(self)
		self.left=left
		self.right=right
		self.butler=butler
		self.number=number
		
		
	def run(self):
	
		for i in range(20):
			self.butler.down()
			time.sleep(0.1)
			self.right.take(self.number)
			time.sleep(0.1)
			self.left.take(self.number)
			time.sleep(0.1)
			self.right.drop(self.number)
			self.left.drop(self.number)
			self.butler.up()
			
		print("p[%s] finished thinking and eating\n" % self.number)
		
		
def main():
    # number of philosophers / chop sticks
    n = 3

    # butler for deadlock avoidance (n-1 available)
    butler = sema(n-1)

    # list of chopsticks
    c = [chop(i) for i in range(n)]

    # list of philsophers
    p = [phil(i, c[i], c[(i+1)%n], butler) for i in range(n)]

    for i in range(n):
        p[i].start()


if __name__ == "__main__":
    main()

