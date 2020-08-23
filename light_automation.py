import conf
from boltiot import Bolt
import json, time 
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
def convert(sensor_value):
	led_intensity= 255-(sensor_value*255/1024)
	return led_intensity
while True: 
    print ("Reading Sensor Value")
    response_ldr = mybolt.analogRead('A0') 
    data = json.loads(response)    
    print("Sensor value is: " + str(data['value'])) 
    try: 
        sensor_value = int(data['value'])
        print("Calculating required Light Intensity for LED")
        led_value_float=convert(sensor_value)  
        led_value= int(led_value_float)           
        print(led_value)
        mybolt.analogWrite('1', led_value)                                                   
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(5)
