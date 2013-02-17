#!/usr/bin/env python
# encoding: utf-8
"""
lottery.py

Created by Kai-Hsin Liu on 2012-06-01.
"""

import sys
import os
import math

def myfunc(u, x, a, w):	
	for i in range(x):
		a[u-i] += w

def calcu(m, n, p, x):
	a = [ 0 for i in range(1, 1002) ]
	
	myfunc(m, p, a, -1)
	myfunc(n, x, a, 1)
	myfunc(p, x, a, 1)
	myfunc(x, x, a, -1)
	myfunc(m-n, p-x, a, 1)
	
	b = []
	c = []
	
	for i in range(1, 1001):
		while a[i] > 0:
			b.append(i)
			a[i] -= 1
		while a[i] < 0:
			c.append(i)
			a[i] += 1
			
	r = 1.0
	
	for i in range(max(len(b), len(c))):
		if len(b) > i:
			r *= b[i]
		if len(c) > i:
			r /= c[i]
	
	return r

def main():
	#input
	line = sys.stdin.readline().strip()
	
	#split: m, n, t, p
	myset = line.split()
	
	#assign for easier use
	m = int(myset[0])
	n = int(myset[1])
	t = int(myset[2])
	p = int(myset[3])
	
	#minimun people needed to pass
	mini = int(math.ceil(float(p)/float(t)))
	
	#get max member number that can be choosed
	maxi = 0
	if p > n:
		maxi = n
	else:
		maxi = p
	
	#if maxi is still not enough to pass the minimum requirement
	if mini > maxi:
		print "0"
		return
	
	pro = 0.0;
	for x in range(mini, maxi+1):
		if (m-p) < (n-x):
			continue
		nn = calcu(m, n, p, x)
		pro += nn
		
	print "%.12f" % pro


if __name__ == '__main__':
	main()

