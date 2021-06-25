import serial
import time
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write(bytes("/start/run \r", 'UTF-8'))
 