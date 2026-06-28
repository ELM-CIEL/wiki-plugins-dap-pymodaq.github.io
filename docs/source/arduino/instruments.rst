Instruments
===========

The plugin exposes actuators, 0D viewers and a Dashboard extension. **Arduino (USB)**
instruments use Telemetrix; **ESP32 (WiFi)** instruments use Telemetrix-AIO and take the
board **IP address** as a parameter.

Actuators (DAQ_Move)
--------------------

**FanHeater** — controls a **heater** (GPIO18) and a **fan** (GPIO17) through a XY-MOS PWM
board connected to an **ESP32 over WiFi** (Telemetrix-AIO). It is multi-axis (one axis per
output); the PWM duty cycle ranges from 0 to 255 (8-bit). This is the actuator used by the
DAP thermal bench.

**LED** — controls a multicolor LED through three PWM outputs (Telemetrix). The three
colour channels are driven independently.

**LEDwithLCD** — same as **LED**, but also displays the red / green / blue values on a
standard 16×2 I2C liquid-crystal display.

**Servo** — controls a servo motor (angle in degrees) on an Arduino over USB (Telemetrix);
the COM port is selectable from the parameter tree.

Viewers (DAQ_Viewer 0D)
-----------------------

**Temperature MAX31865** — reads temperature from a PT100 RTD wired to a **MAX31865** amplifier/ADC.
Communication with the MAX31865 is done over SPI by an **ESP32** running the Telemetrix-AIO
WiFi firmware.

**Voltage_ADS1115** — reads analog voltages from an **ADS1115** (16-bit) or ADS1015 (12-bit) I2C
ADC, over WiFi (ESP32 / Telemetrix-AIO). Up to four single-ended channels (AIN0–AIN3) can
be acquired at once; the gain and data rate are configurable.

**Analog** — acquires data from the analog inputs of an Arduino board (Telemetrix).

Extension
---------

**ColorSynthesizer** — a Dashboard extension built on the RGB LED actuators: it lets you
quickly pick an RGB value and apply it to the actuators.

.. note::

   Each Telemetrix instrument needs the matching **sketch / firmware** uploaded on the
   board. For the ESP32 WiFi instruments (FanHeater, PT100, ADS1115) used by the DAP
   bench, see :doc:`firmware`.
