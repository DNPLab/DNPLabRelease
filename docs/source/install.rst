.. |dnpLabGitLink| raw:: html

   <a href="https://github.com/DNPLab" target="_blank"> DNPLab </a>


==================
Installing DNPLab
==================

Required Packages
=================
The following packages are required to run DNPLab:

.. list-table::
   :widths: 40 60

   * - **Package**
     - **Version**
   * - NumPy
     - 1.19 or higher
   * - SciPy
     - 1.5 or higher
   * - Matplotlib
     - 3.3 or higher
   * - h5py
     - 2.10 or higher
   * - PyQt5
     - 5.14


.. _installing:

Installing with pip
===================
DNPLab can be easily installed using pip. In a terminal simply type the following command:

.. code-block:: bash

   $ python -m pip install dnplab


If you prefer to install DNPLab from the source code, check out our GitHub repository: |dnpLabGitLink|.

Confirm Successful Installation
===============================
To confirm that your installation of DNPLab was successful type the following command:

.. code-block:: bash

    $ pip show dnplab

The output will look similar to this (not the actual version and path to location depends on the local installation:

.. code-block:: bash

    Name: dnplab
    Version: 1.0.2
    Summary: dnpLab - Bringing the Power of Python to DNP-NMR Spectroscopy
    Home-page: http://dnpLab.net
    Author: DNPLab Team
    Author-email: None
    License: MIT
    Location: /Path/to/Package
    Requires: numpy, scipy, matplotlib, h5py, PyQt5
    Required-by: 

