# Config for homeassi

##cheatsheet
	- journalctl -f -u home-assistant@hass

## Setup

	- sudo apt-get install python3 python3-pip yamllint
	- sudo -H pip3 install --upgrade pip
	- sudo useradd hass
	- su hass
	- sudo -H pip3 install homeassistant
	- sudo -H pip3 install xbee
	- sudo -H pip3 install pyserial
	- sudo -H pip3 install speedtest-cli
		- speedtest-cli https://github.com/sivel/speedtest-cli
	- setup: https://home-assistant.io/getting-started/autostart-systemd/
	- setup git authentication
	- cd ~
	- git clone git@github.com:zimmermannb/homeassi.git .homeassistant
	

