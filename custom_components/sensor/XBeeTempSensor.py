from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
from xbee import XBee,ZigBee
import serial

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([XBeeTempSensor(config['device'])])

class XBeeTempSensor(Entity):
    def __init__(self, device):
        self.device=device


    @property
    def name(self):
        return 'XBeeTempSensor'

    @property
    def state(self):
        ser = serial.Serial(self.device, 9600)
        xbee = ZigBee(ser)
        response = xbee.wait_read_frame()
        adcValue = response['samples'][0]['adc-1']
        voltage = adcValue*(1200/1024)
        tempC = (voltage-500)/10
        return round(tempC,0)
    
    @property
    def unit_of_measurement(self):
        return TEMP_CELSIUS
