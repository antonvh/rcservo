rcservo
======

A minimal Python library to control hobby servo motors using PWM.

Overview
--------

rcservo provides a small, dependency-free API for hobby servos. It exposes:

- ``Servo``: a simple class to control a servo by angle or PWM pulse width.

Installation
------------

Install from PyPI:

.. code-block:: bash

   pip install rcservo

Quick start
-----------

.. code-block:: python

   from rcservo import Servo

   servo = Servo(pin=12)
   servo.angle(45)
   servo.pwm(1500)

Usage and Configuration
-----------------------

Create a servo with custom ranges:

.. code-block:: python

   servo = Servo(
       pin=12,
       min_pulse=800,
       max_pulse=2200,
       min_angle=-120,
       max_angle=120,
   )

The ``angle`` method clamps values to the configured min/max angles. The ``pwm`` method accepts microsecond pulse widths and clamps to the configured min/max pulse widths.

API Reference
-------------

.. automodule:: rcservo
   :members:
   :undoc-members:
   :show-inheritance:


