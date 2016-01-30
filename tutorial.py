#Import RPi.GPIO to make use of the GPIO Pins
import RPi.GPIO
#Import Zoltan Szarvas's DHT11 Python library (./dht11.py)
import dht11

#Initialize the GPIO in BCM Mode
RPi.GPIO.setmode(RPi.GPIO.BCM)
#Read data using GPIO pin 4
instance = dht11.DHT11(pin = 4)
result = instance.read()
#Check if result is valid (provided by dht11 library)
if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
#Error handling provided by dht11 library
else:
    print("Error: %d" % result.error_code)
#Cleanup the GPIO pins
RPi.GPIO.cleanup()
