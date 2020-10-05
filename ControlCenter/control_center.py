import serial
import time

S = serial.Serial('com27', 9600, timeout=2)

while True:
    data = S.readline().decode().rstrip()
    print(data)
    time.sleep(1)    
