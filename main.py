import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess as sp
import multiprocessing as mp
import time

def main():
	manager = mp.Manager()
	
	a = manager.list()
	print("start of program")
	
	jobs = []
	for i in range(1,10):
		p = mp.Process(target=pinger, args=[i,a])
		jobs.append(p)
		p.start()
		p.join()
		
	while checkJobs(jobs):
		time.sleep(1)
	
	print(a)

def pinger(i,a):
	address = "192.168.1." + str(i)
	try :
		sp.check_output(["ping" , "-c" , "1" , address])
		print("response from: " , address)
		a.append(i)
	except sp.CalledProcessError:
		print("failed of ping " , address )
	
def checkJobs(jobs):
	allrun = False
	for i in jobs:
		if i.is_alive():
			allrun = True
			
	return allrun
				

	
def test(i,a):
	print("hello from test:" , i)
	a.append(i)


	



if __name__ == "__main__":
	main()
