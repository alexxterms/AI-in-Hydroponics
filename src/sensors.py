import smbus
import time

bus = smbus.SMBus(1)  # I2C bus 1
address = 0x48        # Default address for PCF8591

def read_adc(channel):
    if channel < 0 or channel > 3:
        raise ValueError("Channel must be 0-3")
    bus.write_byte(address, 0x40 | channel)
    bus.read_byte(address)  # Dummy read
    return bus.read_byte(address)  # Real data (0–255)

def get_sensor_data():
    ph_raw = read_adc(0)
    ldr_raw = read_adc(1)
    gas_raw = read_adc(2)
    
    return {
        "pH_raw": ph_raw,
        "ldr_raw": ldr_raw,
        "gas_raw": gas_raw
    }

# Example usage
if __name__ == "__main__":
    while True:
        data = get_sensor_data()
        print(data)
        time.sleep(1)
