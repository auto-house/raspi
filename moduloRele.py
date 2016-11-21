import RPi.GPIO as GPIO
import time

def ativar(pino):

	print("LAMPADA LIGADA\n")
	GPIO.output(pino, GPIO.HIGH)
	
def desativar(pino):
	print("LAMPADA DESLIGADA\n")
	GPIO.output(pino, GPIO.LOW)