import re, uuid 
import time
from omron_2jcie_bu01 import Omron2JCIE_BU01
import ble

def main():
	sensors = []
	sensors.append("C7:B5:C6:68:E3:B2")
	sensor = Omron2JCIE_BU01.ble(sensors[0])
	
	while True:
		print("start of scan")
		sensor.scan(on_scan, scantime=60, active=False)
		print("end of scan")
	
def on_scan(data):
    print("SCAN", data)


if __name__ == "__main__":
	main()
