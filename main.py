#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import sensoresLuz
import moduloRele

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pino_sensor_interno = 7
pino_sensor_externo = 11
pino_rele = 13
GPIO.setup(13, GPIO.OUT)

cond_loop = True
menu = 0

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while cond_loop:

    	menu = int(raw_input("1- Sensor Interno\n2- Sensor Externo\n3- Ligar Rele\n4- Desligar Rele\nQual opcao: "))
        
    	if menu == 1:
			print ("Nivel Sensor Interno: " + str(sensoresLuz.rc_time(pino_sensor_interno)))
    	elif menu == 2:
			print ("Nivel Sensor Externo " + str(sensoresLuz.rc_time(pino_sensor_externo)))
    	elif menu == 3:
			moduloRele.ativar(pino_rele)
    	elif menu == 4:
        	moduloRele.desativar(pino_rele)
    	else:
    		cond_loop = False

finally:
    GPIO.cleanup()