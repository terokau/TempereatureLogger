import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess as sp
import multiprocessing as mp
import time
from datetime import datetime
import nmap
import gpiozero as pi
from omron_2jcie_bu01 import Omron2JCIE_BU01

def main():
	manager = mp.Manager()
	
	getTemperatures = []
	getSensorTemp = []
	getLight = []
	setMeasureMaxLength = 10 #hours
	setInterVal = 10 #seconds
	setArrayLength =  setMeasureMaxLength*60*60/setInterVal

	cpu = pi.CPUTemperature()
	sensor = Omron2JCIE_BU01.serial("/dev/ttyUSB0")
	devinfo = sensor.info()
	
	
	print(devinfo)
	print("start of program ")
	print("length: " , setMeasureMaxLength,"h , Interval: " , setInterVal, "s array length:" , setArrayLength)
	plt.ion()
	while True:
		data = sensor.latest_data_long()
		text= str(cpu.temperature) + ";" + str(data.temperature) + ";" + str(data.light)
		now = datetime.now()
		text = text+ ";"+ now.strftime("%d/%m/%Y %H:%M:%S")
		log("tmp.log",text)
		getTemperatures = controlList(cpu.temperature,getTemperatures,setArrayLength)
		getSensorTemp = controlList(data.temperature,getSensorTemp,setArrayLength)
		getLight = controlList(data.light,getLight,setArrayLength)
		plt.plot(getTemperatures)
		plt.plot(getSensorTemp)
		plt.plot(getLight)
		plt.draw()
		plt.pause(0.0001)
		plt.clf()
		#print(data)
		#print(getTemperatures)

		time.sleep(10)
		
def log(filename,text):
	f = open(filename, "a")
	f.write(text+"\r\n")
	f.close()
	

	
def ControlFan(pin,treshold,currentTemperature):
	fan = pi.LED(pin)
	if currentTemperature>treshold:
		print("current temperature:",currentTemperature, " fan: On", fan.pin)
		fan.on()
	else:
		print("current temperature:",currentTemperature, " fan: Off")
		fan.off()
	

def controlList(addVal,inList,maxLength):
	
	inList.append(addVal)
	if len(inList) >=maxLength:
		inList.pop(0)
	return inList

def checkJobs(jobs):
	allrun = False
	for i in jobs:
		if i.is_alive():
			allrun = True
			
	return allrun
				

if __name__ == "__main__":
	main()
