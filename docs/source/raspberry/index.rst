Raspberry plugin
================

``pymodaq_plugins_raspberry`` lets PyMoDAQ control an experimental device (or test
bench) through a **Raspberry Pi**.

A small **server runs on the Raspberry Pi** and drives the components of the bench
(I2C sensors, GPIO actuators); **PyMoDAQ talks to that server over the network**. From
PyMoDAQ you then get a *detector* (to read the sensors) and an *actuator* (to drive the
outputs), as if they were local instruments.

.. note::

   This single plugin **replaces** the former *Raspberry Pi 3* and *Raspberry Pi Zero*
   plugins. A given bench (PWM or all-or-nothing actuators, different sensors…) is now
   simply a **configuration** of the same code base — see :doc:`configuration`.

Architecture at a glance
------------------------

.. code-block:: text

   ┌──────────── Control computer ─────────────┐         ┌──────── Raspberry Pi ────────┐
   │  PyMoDAQ                                  │   ZMQ   │  server (src_raspberry/)     │
   │   ├─ DAQ_Move   MoveRasp                  │  <───>  │   transport → handler →      │
   │   ├─ DAQ_Viewer ViewRasp  ── ZMQLink ──── │   JSON  │   hardware backend           │
   │   └─ DAQ_Viewer PiCamera                  │         │   (I2C sensors, GPIO out)    │
   └───────────────────────────────────────────┘         └──────────────────────────────┘

The control computer hosts the three PyMoDAQ instruments and the communication layer
(``ZMQLink``); the Raspberry Pi hosts the server that actually reads the sensors and
drives the outputs.

.. toctree::
   :maxdepth: 2
   :caption: Raspberry plugin

   instruments
   communication
   server
   configuration

Installation (control computer)
-------------------------------

* PyMoDAQ **>= 5**.
* On a Windows / macOS control machine the plugin installs as is; the ``picamera2``
  dependency (Linux-only) is automatically skipped, so only the PiCamera viewer is
  unavailable there.
* The Raspberry-side server has its own requirements (I2C bus + ``pigpio`` daemon) —
  see :doc:`server`.

Resources and Downloads
--------------------------

These documents contain the step-by-step guide including all screenshots (PyMoDAQ interface, Raspberry Pi Imager configuration, etc.).
* :download:`Download the Installation Guide (PDF) <Manuel/RaspPi3B_ 01_Notice_d_installation.pdf>`
* :download:`Download the User Manual (PDF) <Manuel/RaspPi3B_02_Manuel_d_utilisation.pdf>`
* :download:`Download the Maintenance Guide (PDF) <Manuel/RaspPi3B_03_Notice_de_maintenance.pdf>`

