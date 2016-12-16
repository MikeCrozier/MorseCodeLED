from time import sleep
import RPi.GPIO as GPIO
alphabet = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
            'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
            'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
            't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..', ' ': ' '}
            
led = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)

def Morse(char):
    for c in char:
        if c == ' ':
            sleep(.75)
        elif c == '.':
            GPIO.output(led,GPIO.HIGH)
            sleep(0.25)
            GPIO.output(led,GPIO.LOW)
        else:
            GPIO.output(led,GPIO.HIGH)
            sleep(0.75)
            GPIO.output(led,GPIO.LOW)
        sleep(.25)

string = raw_input("Enter a String: ")

for c in string:
    char = alphabet[c.lower()]
    print(c + ' ' + char)
    Morse(char)
    sleep(.75)

print('Message Completed')
    

