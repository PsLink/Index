#!/usr/bin/env python

# filter of cTree

import fileinput
import math


errBound = 10
score = 0
candidate = set([])

def transback(k): #need to reverse back
	ans = []
	order = 1728
	while order >= 1:
		ans.insert(0,k/order)
		k = k % order
		order = order / 12
	return ans

def SDist(x,y):
	ans = 0
	for i in xrange(4):
		ans = ans + abs(x[i] - y[i])
	return ans

def search(k, table, query):
	print k, table, query



def main():
	query = [4,6,4,5,4,4,8,6,4,4,7,5,4,6,5,5,4,3,4,8,7,7,4,2]

	qHead = query[0:4]

	insID = 0
	for i in fileinput.input("tree0.txt"):
		table = i.split()

		k = int(table[0])

		score = SDist(transback(int(table[0])),qHead)

		if (score<=errBound):
			tmpCan = search(k, table[1:],query[4:])
			break


		insID = insID+1









if __name__ == '__main__':
	main()
