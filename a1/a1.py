import unittest

class Test(unittest.TestCase):
	def test_positive(self):
		bSearchObj = BinarySearch([11,22,33,44,55],55)
		self.assertEqual(bSearchObj.binarySearch(0,4),4)
		
	def test_negative(self):
		bSearchObj = BinarySearch([11,22,33,44,55],66)
		self.assertEqual(bSearchObj.binarySearch(0,4),-1)
		

class BinarySearch():

	def __init__(self, a, key):
		self.a = a
		self.key = key
		self.sort_for_bSearch()
		print "Searching for",key
		
	def sort_for_bSearch(self):
		self.a.sort()
		print "Sorted list is",self.a
		
	def binarySearch(self, l, r):
		
		while(l<=r):
			mid = (l+r)/2
			
			if(self.a[mid]==self.key):
				return mid
			elif (self.a[mid]<self.key):
				return self.binarySearch(mid+1,r)
			elif (self.a[mid]>self.key):
				return self.binarySearch(l,mid-1)
		return -1
	

def main():
	f = open('mem.txt','r')
	data = f.read()
	a = [int(x) for x in data.split()]
	print "Input list is",a
	key = int(raw_input("Enter key : "))
	bSearchObj = BinarySearch(a, key)
	index = bSearchObj.binarySearch(0,len(a)-1)
	if (index == -1):
		print "Not Found!"
	else:
		print "Element found at position",index+1
		
main()

unittest.main()
		
