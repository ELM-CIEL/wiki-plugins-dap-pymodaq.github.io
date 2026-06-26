Downloads
=========

Ready-to-use files for the DAP PyMoDAQ plugins: example plugin configurations, the
conda environment, and a standalone HDF5 → CSV conversion tool.

.. note::

   The configuration files are provided as **working examples**. The IP addresses are
   placeholders — replace them with the values matching your own hardware before use.

Example configurations
----------------------

Example plugin configuration files (``.toml``). On Windows they go in
``%USERPROFILE%\.pymodaq``.

Arduino
~~~~~~~

.. literalinclude:: /_files/configs/config_arduino.toml
   :language: toml

:download:`Download config_arduino.toml </_files/configs/config_arduino.toml>`

Raspberry Pi 3
~~~~~~~~~~~~~~

.. literalinclude:: /_files/configs/config_raspberrypi3.toml
   :language: toml

:download:`Download config_raspberrypi3.toml </_files/configs/config_raspberrypi3.toml>`

Raspberry Pi Zero
~~~~~~~~~~~~~~~~~

.. literalinclude:: /_files/configs/config_raspberrypizero.toml
   :language: toml

:download:`Download config_raspberrypizero.toml </_files/configs/config_raspberrypizero.toml>`

Conda environment
-----------------

The conda environment used for the project. Recreate it with:

.. code-block:: bash

   conda env create -f Py26env.yml
   conda activate Py26

* :download:`Py26env.yml </_files/Py26env.yml>`

HDF5 → CSV converter (tool)
---------------------------

``h5_to_csv_gui.py`` is a small **standalone** PyQt6 tool that converts a PyMoDAQ
*Log Data* ``.h5`` file into a spreadsheet-friendly **CSV**:

* a single common *time* column (timestamp converted to a readable
  ``DD/MM/YYYY HH:MM:SS``);
* one column per signal, named after its ``label``;
* gaps filled with the previous value; French decimal comma and ``;`` column separator.

**Dependencies**: ``pip install PyQt6 h5py numpy``

**Easiest way** — keep ``H5_To_CSV.bat`` and ``h5_to_csv_gui.py`` in the **same folder**
and simply **double-click** ``H5_To_CSV.bat``: it activates the ``Py26`` conda environment
and launches the tool (it works from any location).

Alternatively, run the script yourself from a terminal:

.. code-block:: bash

   python h5_to_csv_gui.py

Downloads:

* :download:`h5_to_csv_gui.py </_files/tools/h5_to_csv_gui.py>`
* :download:`H5_To_CSV.bat </_files/tools/H5_To_CSV.bat>`
