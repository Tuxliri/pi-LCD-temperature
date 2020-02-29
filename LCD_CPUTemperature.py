from gpiozero import CPUTemperature
from time import sleep, strftime, time
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
sleep(1)
cpu = CPUTemperature()

while True:
        temp = cpu.temperature
        ser.write(b'CPU Temp: ' + str('{:3.1f}'.format(temp)).encode() + b' C')
        sleep(0.7)