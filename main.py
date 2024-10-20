from machine import Pin, PWM
import time
from irrecvdata import irGetCMD

ledPin = PWM(Pin(14))
ledPin.freq(10000)
ledPin.duty_u16(512)
buzzerPin = Pin(16, Pin.OUT)

recvPin = irGetCMD(15)

def mycontroller(value):
    buzzerPin.value(1)
    time.sleep_ms(100)
    buzzerPin.value(0)

    if value == '0xff6897':
        ledPin.duty_u16(1)
    elif value == '0xff30cf':
        ledPin.duty_u16(1023)
    elif value == '0xff18e7':
        ledPin.duty_u16(4096)
    elif value == '0xff7a85':
        ledPin.duty_u16(10000)
    else:
        print("Unknown button pressed:", value)
        return

try:
    while True:
        irValue = recvPin.ir_read()
        if irValue:
            print("Received IR value:", irValue)
            mycontroller(irValue)
except KeyboardInterrupt:
    ledPin.deinit()

