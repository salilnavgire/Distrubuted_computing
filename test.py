import sys
import random
import os
import time
from multiprocessing import Pool

def ddd(oldlist):
  print(os.getpid(), len(oldlist))
	newlist=[]
	newlist.append(os.getpid())
	newlist.append([x*x for x in oldlist])
	time.sleep(0.001)
	return newlist

if __name__== '__main__':
	longlist = []
	for i in range(1,11):
		longlist.append([i]*i)

	num = 1

	for i in range(1,5):
		t_start = time.time()
		pool = Pool(num)
		result = pool.map(ddd,longlist)

#		for x in result:
#			print(x)

		t_end = time.time()
		print(num, "time used: ", t_end-t_start)
		num *= 2
	
