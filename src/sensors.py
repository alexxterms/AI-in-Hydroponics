import grovepi
import time

# Port configuration
ph_pin = 0
ldr_pin = 1
gas_pin = 2
dht_pin = 4

while True:
    try:
        ph_raw = grovepi.analogRead(ph_pin)
        ldr_raw = grovepi.analogRead(ldr_pin)
        gas_raw = grovepi.analogRead(gas_pin)
        [temp, hum] = grovepi.dht(dht_pin, 0)

        print(f"pH: {ph_raw}, LDR: {ldr_raw}, Gas: {gas_raw}, Temp: {temp}, Humidity: {hum}")
        time.sleep(1)
    except Exception as e:
        print("Error:", e)
