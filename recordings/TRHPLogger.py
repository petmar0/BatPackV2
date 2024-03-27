import time
import datetime
import bme280
import smbus2
from time import sleep

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
#VIN to pin 17 (3V3), GND to pin 6 (GND), SDA to pin 3 (SDA), and SCL to pin 5 (SCL)
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)
print("t (YYYYMMDD_HH:MM:SS),T (°C),RH (%RH),P (kPa)")

while True:
    now = datetime.datetime.now()
    bme280_data = bme280.sample(bus,address)
    RH  = bme280_data.humidity
    P  = bme280_data.pressure
    T = bme280_data.temperature
    print(now.strftime('%Y%m%d_%H%M00'), ",", T, ",", RH, ",", P)
    sleep(60)