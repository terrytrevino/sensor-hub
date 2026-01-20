from dataclasses import dataclass
from typing import Any, Dict, Optional

from sensor_hub.core.base_sensor import BaseSensor


@dataclass
class BME280Config:
    address: int = 0x76


class BME280Sensor(BaseSensor):
    def __init__(self, bus: Any, config: Optional[BME280Config] = None):
        super().__init__("bme280")
        if bus is None:
            raise ValueError("BME280Sensor requires a bus (I2C) object")
        self.bus = bus
        self.config = config or BME280Config()

    def read(self) -> Dict[str, float]:
        # Placeholder until hardware bus + full driver are plugged in
        return {"temperature_c": 0.0, "pressure_pa": 0.0, "humidity_rh": 0.0}
