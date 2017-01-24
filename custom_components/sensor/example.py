from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([ExampleSensor()])


class ExampleSensor(Entity):
    @property 
    def name(self):
        return 'Temperature'

    @property
    def state(self):
        return 25

    @property
    def unit_of_measurement(self):
        return TEMP_CELSIUS
