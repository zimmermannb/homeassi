from homeassistant.helpers.event import (track_state_change)
from homeassistant.components import is_on, toggle
DOMAIN = 'xor_automation'

def setup(hass, config):
	entity_1 = config[DOMAIN]['entity_1']
	entity_2 = config[DOMAIN]['entity_2']
	
	def state_changed(entity_id, old_state, new_state):
		if entity_id == entity_1:
			other = entity_2
		else:
			other = entity_1
		
		if is_on(hass, entity_id) == is_on(hass, other):
			toggle(hass, other)
		return True

	#ensure current state is oposite
	if is_on(hass, entity_1) == is_on(hass, entity_2):
		toggle(hass, entity_2)
	return True
