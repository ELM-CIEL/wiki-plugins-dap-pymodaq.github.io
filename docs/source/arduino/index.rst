Arduino plugin
==============

``pymodaq_plugins_arduino`` groups a set of instruments built around an **Arduino** or
**ESP32** board. Most instruments use the `Telemetrix
<https://mryslab.github.io/telemetrix-esp32/>`_ library to drive an Arduino over USB; the ESP32
instruments use **Telemetrix-AIO** to talk to the board over **WiFi**. No firmware change
is needed to change the behaviour — a fixed sketch is flashed once, and everything is then
driven from Python.

In the DAP project, the plugin is used on a **thermal test bench** built around an
**Arduino Nano ESP32**: a fan and a heater are driven in PWM and the temperature is read
from a PT100 probe, for the physics lab sessions (*TP*) of the BTS CIEL at Lycée Édouard
Branly.

.. toctree::
   :maxdepth: 2
   :caption: Arduino plugin

   instruments
   hardware
   firmware
   installation
   usage

The plugin requires PyMoDAQ **> 4.1**.
