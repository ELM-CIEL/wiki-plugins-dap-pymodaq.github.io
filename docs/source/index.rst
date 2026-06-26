Welcome to the DAP Pymodaq plugins wiki
=======================================

This is the documentation wiki of the **DAP** PyMoDAQ plugins, developed for the
BTS CIEL project at *Lycée Edouard Branly* (Lyon), in partnership with the **CETHIL**.

The goal of the project is to migrate thermal test benches from the proprietary
**LabVIEW** software to **PyMoDAQ**, a free and open-source data-acquisition framework.

Two plugins are documented here:

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Arduino plugin
      :link: arduino/index
      :link-type: doc

      Instruments built around **Arduino / ESP32** boards using Telemetrix: multicolor
      LED, fan & heater, analog and PT100 / ADS1115 acquisition, plus a dashboard
      extension.

   .. grid-item-card:: Raspberry plugin
      :link: raspberry/index
      :link-type: doc

      Control an experimental bench through a **Raspberry Pi**: a PyMoDAQ actuator and
      detector talking to an on-Pi server over ZeroMQ.

Downloads
---------

.. grid:: 1

   .. grid-item-card:: Downloads ⬇
      :link: downloads
      :link-type: doc

      Ready-to-use PyMoDAQ presets, example plugin configurations, the conda environment
      and a standalone HDF5 → CSV conversion tool.

.. toctree::
   :hidden:
   :maxdepth: 2

   arduino/index
   raspberry/index
   downloads
