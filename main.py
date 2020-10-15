import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess as sp
import multiprocessing as mp

def main():
	print("start of program")
	a = np.array([])
	jobs = []
	for i in range(1,254):
		p = mp.Process(target=pinger(i))
		jobs.append(p)
		p.start()
			
	print(a)
	
def pinger(i):
	address = "192.168.1."+ str(i)
	res = sp.call(["ping" , "-c" , "1" , address])
	if res==0:
		np.append(a,i)
		print ("ping ok: " ,address)
	elif res==2:
		print("No response from " , address)
	else:
		print("Ping failed " , address)


	



if __name__ == "__main__":
	main()
