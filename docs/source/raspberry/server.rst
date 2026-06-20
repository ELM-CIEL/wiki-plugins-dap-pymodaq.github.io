Raspberry-side server
=====================

The code that must run on the Raspberry Pi lives in the ``src_raspberry/`` folder at the
root of the plugin repository. It makes the bridge between the hardware (I2C sensors,
GPIO actuators) and the network.

.. note::

   This folder is an **addition** to the plugin and is *not packaged*: it is not part of
   the Python distribution of the PyMoDAQ plugin and does not modify it.

Layered architecture
--------------------

The server is split into independent layers, each behind an interface; only ``main.py``
is not interchangeable, as it assembles the others.

.. code-block:: text

   ZmqServer  ──►  JsonRequestHandler  ──►  HardwareBackend
  (transport)       (request routing)       (component comm.)
        ▲                  ▲                       ▲
   ITransport       IRequestHandler         IHardwareBackend

* **transport/** — communication with the PyMoDAQ client. ``zmq_server.py`` implements
  ``ZmqServer`` (ZeroMQ ROUTER); it only handles networking and framing.
* **handlers/** — request handling. ``json_handler.py`` implements
  ``JsonRequestHandler`` (JSON decoding + routing). It performs **no hardware access**:
  everything is delegated to the backend.
* **hardware/** — communication with the components. ``backend.py`` implements
  ``HardwareBackend`` (sensors + actuators); ``sensors.py`` holds the sensor drivers and
  the ``SENSOR_DRIVER_REGISTRY`` (``AHT10``, ``TMP102``, ``EMC2101``, ``PT-100``,
  ``SIMULE``); ``actuators.py`` holds the actuator drivers and the
  ``ACTUATOR_DRIVER_REGISTRY`` (``PWM``, ``DIGITAL``); ``scanner.py`` detects I2C
  addresses.
* **config.py** — the description of the bench (pins, sensors, actuators). The **only**
  file to adapt from one bench to another (see :doc:`configuration`).
* **main.py** — entry point: instantiates and wires the three layers
  (``HardwareBackend`` → ``JsonRequestHandler`` → ``ZmqServer`` on port 5555).

Requirements and installation
-----------------------------

#. **OS Installation** — Flash **Raspberry Pi OS (64-bit)** on a micro-SD card (8 GB min.). Connect via SSH and update the system: ``sudo apt update && sudo apt upgrade -y``.
#. **Enable I2C** — ``sudo raspi-config`` → *Interfacing Options* → *I2C*.
#. **pigpio daemon** (hardware GPIO control):

   .. code-block:: bash

      sudo apt-get update
      sudo apt-get install pigpio python3-pigpio
      sudo systemctl enable pigpiod
      sudo systemctl start pigpiod

#. **Python dependencies**:

   .. code-block:: bash

      python3 -m venv .venv
      source .venv/bin/activate
      pip install -r requirements.txt
      
   .. note::

      If the ``requirements.txt`` file is missing, you can create it with the following content:

      .. code-block:: text

         Adafruit-Blinka>=8.69.0
         adafruit-circuitpython-busdevice>=5.2.15
         adafruit-circuitpython-connectionmanager>=3.1.6
         adafruit-circuitpython-emc2101>=1.2.12
         adafruit-circuitpython-register>=1.11.1
         adafruit-circuitpython-requests>=4.1.15
         adafruit-circuitpython-typing>=1.12.3
         Adafruit-PlatformDetect>=3.86.0
         Adafruit-PureIO>=1.1.11
         binho-host-adapter>=0.1.6
         board>=1.0
         pigpio>=1.78
         pyftdi>=0.57.1
         pyserial>=3.5
         pyusb>=1.3.1
         pyzmq>=27.1.0
         RPi.GPIO>=0.7.1
         smbus2>=0.6.0
         sysv_ipc>=1.2.0
         typing_extensions>=4.15.0

Running and Auto-start (systemd)
--------------------------------

**Manual test:**

.. code-block:: bash

   python main.py

.. note::

   **Automatic simulation mode** — if the I2C bus or the ``pigpio`` daemon are unreachable (for
   instance when running on a regular PC), the server automatically falls back to
   simulated objects (``MagicMock`` / ``SIMULE`` drivers), so the network communication can be tested without
   a real Raspberry Pi.

**In production:** create a systemd service file at ``/etc/systemd/system/pilotage.service``:

.. code-block:: ini

   [Unit]
   Description=Thermal control ZeroMQ Server
   After=network.target pigpiod.service

   [Service]
   ExecStart=/home/admin/PYMODAQ_PLUGIN_RASPPI3/PY_ENV/bin/python /home/admin/PYMODAQ_PLUGIN_RASPPI3/main.py
   WorkingDirectory=/home/admin/PYMODAQ_PLUGIN_RASPPI3
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=admin

   [Install]
   WantedBy=multi-user.target

.. warning::

   Make sure to put a space between the python binary and the path to ``main.py`` in ``ExecStart`` (two separate paths separated by a space).

Then, reload the daemon and start the service:

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl enable pilotage.service
   sudo systemctl start pilotage.service

**Troubleshooting:**
* Check service status: ``sudo systemctl status pilotage.service`` (should be ``active (running)``).
* Check I2C devices on the bus: ``sudo i2cdetect -y 1``.

Hardware Configuration (config.py)
----------------------------------

The entire topology is centralized in ``src_raspberry/config.py``:

.. code-block:: python

   I2C_BUS_ID      = 1
   VENTILATEUR_PIN = 18     # PWM 25000 Hz
   RESISTANCE_PIN  = 23     # PWM 100 Hz (via MOSFET)

   CAPTEUR_AHT10   = 0x38   # rh_sortie
   CAPTEUR_TMP102  = 0x48   # t_resistance
   # 0x49 t_dissipateur, 0x4A t_entree, 0x4B t_sortie (TMP102)
   CAPTEUR_EMC2101 = 0x4C   # T_emc

To change a pin or an address, modify ``ACTUATORS_CONFIG`` (actuators) or ``SENSORS_CONFIG`` (sensors) in this single file.
