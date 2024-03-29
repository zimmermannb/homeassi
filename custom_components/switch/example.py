import os
from homeassistant.helpers.entity import ToggleEntity

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([FileSwitch(config['file_path'])])

class FileSwitch(ToggleEntity):
    def __init__(self, path):
        self.path = path
        self.update()

    @property
    def name(self):
        return os.path.basename(self.path)

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        open(self.path, 'a').close()

    def turn_off(self, **kwargs):
        os.remove(self.path)

    def update(self):
        self._state = os.path.isfile(self.path)

