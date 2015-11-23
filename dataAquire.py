#!C:\Python34\
import sys
import time
import serial

no = 1000
x  = []
y  = []
z  = []

ser = serial.Serial("COM11",38400)
while True:
	while no!=0:
		ser.flushInput()
		tmp = ser.readline()
		if(len(tmp) != 10):
			continue
		else:
			no-=1
			x.append(float(int(tmp[0:3],16)))
			y.append(float(int(tmp[3:6],16)))
			z.append(float(int(tmp[6:9],16)))
	print("x: ")
	print(sum(x)/len(x)*12.0/4096.0-6.0)
	print("y: ")
	print(sum(y)/len(y)*14.0/4096.0-7.0)
	print("z: ")
	print(sum(z)/len(z)*36.0/4096)
	no = 1000
	x = []
	y = []
	z = []
	
		
