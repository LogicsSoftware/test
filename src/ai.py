# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def sieve1(n):
	import math
	top = int(math.sqrt(n))
	nums = range(2, n + 1)
	for i in range(2, top + 1):
		#print i, nums
		nums = filter(lambda x: x == i or x % i, nums)
	return nums
#print sieve1(10)
def sieve2(n):
	import math
	top = int(math.sqrt(n))
	nums = range(2, n + 1)
	prims = []
	while nums[0] <= top:
		# filter next prim
		p = nums[0]
		#print p, prims, nums
		nums = filter(lambda x: x == p or x % p, nums)
		# update
		prims += [nums[0]]
		nums = nums[1:]
	else:
		# rest must be primes
		prims += nums
	return prims
#print sieve2(10)
def sieve3(n):
	import math
	top = int(math.sqrt(n))
	nums = range(2, n + 1)
	ix = 0
	while nums[ix] <= top:
		# filter next prim
		p = nums[ix]
		#print ix, p, nums
		nums = filter(lambda x: x == p or x % p, nums)
		# advance
		ix += 1
	return nums
#print sieve3(100)
def sieves(n):
#	p1 = sieve1(n)
#	print p1
#	p2 = sieve3(n)
#	print p2
#	print n, p1 == p2, len(p2)	# , p1 == p2
	import time
	i = 10
	while i <= n:
		start = time.time()
		prims = sieve3(i)
		stop = time.time()
		print "there are", len(prims), "primes <=", i, " -- time:", stop - start
		i *= 10
#sieves(10000000)	#4, 25, 168, 1229, 9592, 78498/5.67(5.58)-5.19(5.39), 664579/128.43(125.48)-117.34(113.11)

def exec_cmd(cmd):
	import subprocess
	string = subprocess.check_output(["cmd", "/c", cmd])
	lines = string.splitlines()
	words = [line.split() for line in lines]
	return {"string": string, "lines": lines, "words": words}
print exec_cmd("dir")
#print exec_cmd("http://logics.de")

