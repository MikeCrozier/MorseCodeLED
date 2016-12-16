from time import sleep
import RPi.GPIO as GPIO

led = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)


for i in range(10):
    GPIO.output(led,GPIO.HIGH)
    sleep(0.25)
    GPIO.output(led,GPIO.LOW)
    sleep(0.25)

