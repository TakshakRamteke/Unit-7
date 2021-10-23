from machine import Pin
import time
import network

def toggle(p):
    p.value(not p.value())


led = Pin(2,Pin.OUT) 

ssid = str(input("Please enter your SSID : "))                  
password = str(input("Please enter Password for this SSID : "))    

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected == False :
    print("trying to connect",end="")
    toggle(led)
    time.sleep(1)
    
    if station.isconnected == True :
        led = Pin(2,Pin.OUT)
        station.ifconfig()
        break

    else :
        print(".",end="")
