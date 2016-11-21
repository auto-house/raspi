#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import sensoresLuz
import moduloRele

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pino_sensor_interno = 7
pino_sensor_externo = 11
pino_rele = 12
GPIO.setup(12, GPIO.OUT)

cond_loop = True

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while cond_loop:
        
        print ("Nivel Sensor Interno: " + sensoresLuz.rc_time(pino_sensor_interno))
        print ("Nivel Sensor Externo " + sensoresLuz.rc_time(pino_sensor_externo))

        moduloRele.ativer(pino_rele)
        time.sleep(2)
        moduloRele.desativar(pino_rele)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()