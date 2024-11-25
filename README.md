# LTR390 UV and Ambient Light Sensor ☀️

This project demonstrates how to set up and use the **LTR390 UV and ambient light sensor** on a Raspberry Pi. It covers hardware setup, sensor initialization, and reading data (UV index and ambient light intensity).

## Features
- Measure **UV Index** and **Ambient Light Intensity**.
- Easy-to-use Python scripts for communication via I2C.
- Comprehensive setup and usage instructions.

## Hardware Requirements
- Raspberry Pi 3 B+
- LTR390 UV/ALS sensor module
- Jumper wires for I2C connection

## Software Requirements
- Python 3.11+
- Libraries: `smbus2`, `RPi.GPIO`

If you want to keep your project isolated, install the required Python libraries in the virtual environment:
```
sudo apt-get update
sudo apt-get install -y python3 python3-pip
pip3 install smbus2 RPi.GPIO
```

## Sensor Setup
1. Connect the LTR390 sensor to the Raspberry Pi:
```
| LTR390 Pin | Raspberry Pi Pin |
|------------|------------------|
| VCC        | 3.3V            |
| GND        | GND             |
| SCL        | GPIO3 (Pin 5)   |
| SDA        | GPIO2 (Pin 3)   |
```
2. Enable I2C on the Raspberry Pi:
  `sudo raspi-config`
  Go to Interfacing Options > I2C and enable it.
  Reboot if prompted.
3. Test the I2C connection:
  `sudo i2cdetect -y 1`
  The LTR390 should show up as an address, typically 0x53.

## Code Usage
1. Clone this repository: `git clone git@github.com:Ssofi1a/LTR390.git
cd LTR390`
2. Run the example Python script to measure UV index and ambient light intensity:
  `python3 ltr390.py`
