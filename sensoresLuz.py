import RPi.GPIO as GPIO
import time
# retorna um nivel de luminosidade, 1- ALTA -> 12- BAIXA
def rc_time (pino):
    count = 0
    resp = 0
  
    #Output on the pin for 
    GPIO.setup(pino, GPIO.OUT)
    GPIO.output(pino, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pino, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pino) == GPIO.LOW):
        count += 1

    if count < 300:
        resp = 1
    elif count >= 300 and count < 500:
        resp = 2
    elif count >= 500 and count < 1000:
        resp = 3
    elif count >= 1000 and count < 2500:
        resp = 4
    elif count >= 2500 and count < 4000:
        resp = 5
    elif count >= 4000 and count < 6000:
        resp = 6
    elif count >= 6000 and count < 8000:
        resp = 7
    elif count >= 8000 and count < 10000:
        resp = 8
    elif count >= 10000 and count < 12000:
        resp = 9
    elif count >= 12000 and count < 14000:
        resp = 10
    elif count >= 14000 and count < 16000:
        resp = 11
    elif count >= 16000:
        resp = 12

    return resp