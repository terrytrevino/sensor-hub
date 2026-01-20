from sensor_hub.core.fake_i2c import FakeI2CBus
from sensor_hub.sensors.bme280 import BME280Sensor, BME280Config

# Minimal BME280 register setup for demo purposes:
# - Chip ID at 0xD0 = 0x60
# - Calibration + raw data blocks are filled with non-zero bytes so driver runs
# NOTE: This is not "accurate environment data", it's a runnable dev harness.

def main():
    addr = 0x76
    bus = FakeI2CBus()

    # chip id
    bus.set_bytes(addr, 0xD0, bytes([0x60]))

    # calibration blocks (fill with deterministic bytes)
    bus.set_bytes(addr, 0x88, bytes(range(1, 27)))  # 26 bytes
    bus.set_bytes(addr, 0xE1, bytes(range(50, 57))) # 7 bytes

    # raw burst data at 0xF7 length 8 (pressure/temp/humidity ADC)
    # put some non-zero-ish values
    bus.set_bytes(addr, 0xF7, bytes([0x64, 0x00, 0x00, 0x80, 0x00, 0x00, 0x40, 0x00]))

    sensor = BME280Sensor(bus=bus, config=BME280Config(address=addr))
    print(sensor.read())

if __name__ == "__main__":
    main()
