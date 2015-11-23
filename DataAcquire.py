#!/usr/bin/python2

import sys
import time
import serial

ser = serial.Serial("/dev/ttyUSB0",38400)

def getData(ser, amount):
	data = []
	while amount != 0:
		ser.flush()
		tmp = ser.readline()
		if(len(tmp) == 10):
			amount -= 1
			data.append(tmp)
	return data

def countXYZ(data):
	x=[]
	y=[]
	z=[]
	for tmp in data:
		x.append(float(int(tmp[0:3],16))*12.0/4096.0)
		y.append(float(int(tmp[3:6],16))*14.0/4096.0)
		z.append(float(int(tmp[6:9],16))*36.0/4096.0)
	return [sum(x)/len(x),sum(y)/len(y),sum(z)/len(z)]

while True:
	data = getData(ser,100)
	print(countXYZ(data))
	time.sleep(0.5)

