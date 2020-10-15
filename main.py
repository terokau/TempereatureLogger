import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
import gpiozero as pi
from omron_2jcie_bu01 import Omron2JCIE_BU01

def main():
	getTemperatures = []
	getSensorTemp = []
	getLight = []
	setMeasureMaxLength = 10 #hours
	setInterVal = 10 #seconds
	setArrayLength =  setMeasureMaxLength*60*60/setInterVal

	cpu = pi.CPUTemperature()
	sensor = Omron2JCIE_BU01.serial("/dev/ttyUSB0")
	devinfo = sensor.info()
	
	plt.ion()
	
	print(devinfo)
	print("start of program ")
	print("length: " , setMeasureMaxLength,"h , Interval: " , setInterVal, "s array length:" , setArrayLength)
	
	
	while True:
		#Read data from 2JCIE-BU01
		data = sensor.latest_data_long()
		
		#Generate log string
		text= str(cpu.temperature) + ";" + str(data.temperature) + ";" + str(data.light)
		now = datetime.now()
		text = text+ ";"+ now.strftime("%d/%m/%Y %H:%M:%S")
		
		log("tmp.log",text)
		
		#update arrays.
		getTemperatures = controlList(cpu.temperature,getTemperatures,setArrayLength)
		getSensorTemp = controlList(data.temperature,getSensorTemp,setArrayLength)
		getLight = controlList(data.light,getLight,setArrayLength)
		
		#Make plot 
		plt.plot(getTemperatures)
		plt.plot(getSensorTemp)
		plt.plot(getLight)
		plt.draw()
		plt.pause(0.0001)
		plt.clf()


		time.sleep(setInterVal)
		
def log(filename,text):
	f = open(filename, "a")
	f.write(text+"\r\n")
	f.close()


def controlList(addVal,inList,maxLength):
	
	inList.append(addVal)
	if len(inList) >=maxLength:
		inList.pop(0)
	return inList

				

if __name__ == "__main__":
	main()
