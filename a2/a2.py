import xml.etree.ElementTree as ET
import threading
import unittest

def getInput(filename):
	tree = ET.parse(filename)
	root = tree.getroot()
	ip = root.text.split()
	a = [int(x) for x in ip]
	print a
	return a
	
def partition(a, l, r):
	i = l+1
	j = r
	pivot = a[l]
	done = False
	while not done:
		while (i<=j and a[i]<=pivot):
			i+=1
		while (j>=i and a[j]>=pivot):
			j-=1
		if(j<i):
			done = True
		else:
			a[i],a[j] = a[j],a[i]
	a[j],a[l] = a[l],a[j]
	return j
	
def qsort(a, l, r):
	if(l<r):
		mid = partition(a, l, r)
		t1 = threading.Thread(qsort(a,l,mid-1))
		t2 = threading.Thread(qsort(a,mid+1,r))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		print t1.getName(),t2.getName()
		
def main():
	a = getInput('input.xml')
	qsort(a, 0, len(a)-1)
	print a
	
main()
