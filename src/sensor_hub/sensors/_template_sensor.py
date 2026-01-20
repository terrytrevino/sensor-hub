"""
Sensor Template

How to use:
- Copy this file to a new name, e.g. bme280.py, mpu6050.py, gps_nmea.py
- Rename the class to match the sensor
- Implement read() to return a dict of measurements

Rules:
- One sensor driver per file
- Keep read() fast; no long sleeps
- Return values in SI units where possible
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from sensor_hub.core.base_sensor import BaseSensor


@dataclass
class SensorConfig:
    """Optional config block for a sensor."""
    sample_hz: float = 1.0
    address: Optional[int] = None  # e.g., I2C address if relevant


class TemplateSensor(BaseSensor):
    """
    Example sensor driver skeleton.
    Replace this with a real sensor class, e.g. BME280Sensor.
    """

    def __init__(self, config: Optional[SensorConfig] = None, bus: Any = None):
        super().__init__(name="template_sensor")
        self.config = config or SensorConfig()
        self.bus = bus  # could be I2CBus / SPIBus / UARTPort later

        # TODO: initialize device here (read chip ID, set modes, etc.)
        # Keep it lightweight; avoid long sleeps in __init__.

    def read(self) -> Dict[str, Any]:
        """
        Return a dict of measurements.
        Example keys:
          - temperature_c
          - pressure_pa
          - humidity_rh
          - accel_m_s2 (as tuple)
        """
        # TODO: replace with real sensor read
        return {
            "ok": True,
            "sensor": self.name,
            "note": "template - no real readings yet",
        }

    def health_check(self) -> bool:
        # Optional: do a cheap sanity check (chip id read, status register, etc.)
        return True
