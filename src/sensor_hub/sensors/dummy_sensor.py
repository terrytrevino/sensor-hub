import random
from sensor_hub.core.base_sensor import BaseSensor

class DummyTemperatureSensor(BaseSensor):
    def __init__(self):
        super().__init__("dummy_temperature")

    def read(self):
        return {"temperature_c": round(20 + random.random() * 5, 2)}
