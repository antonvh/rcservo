Usage Guide
===========

Installation
------------

Install rcservo using pip:

.. code-block:: bash

   pip install rcservo

Basic Usage
-----------

Import the Servo class:

.. code-block:: python

   from servo import Servo

Create a servo instance on a GPIO pin:

.. code-block:: python

   servo = Servo(pin=12)

Control the servo angle:

.. code-block:: python

   servo.angle(45)    # Move to 45 degrees
   servo.angle(0)     # Move to center (neutral)
   servo.angle(-90)   # Move to far left

Custom Configuration
--------------------

You can customize the servo for different types of hardware:

.. code-block:: python

   servo = Servo(
       pin=12,
       min_pulse=800,      # Minimum pulse width in microseconds
       max_pulse=2200,     # Maximum pulse width in microseconds
       min_angle=-120,     # Minimum angle
       max_angle=120       # Maximum angle
   )

Direct PWM Control
-------------------

For advanced use cases, you can control the servo using PWM pulse width directly:

.. code-block:: python

   servo.pwm(1500)  # Set to 1500 microseconds
   servo.pwm(1000)  # Set to 1000 microseconds (far left)
   servo.pwm(2000)  # Set to 2000 microseconds (far right)

Utility Functions
-----------------

The ``scale`` function allows you to scale values between ranges:

.. code-block:: python

   from servo import scale

   # Scale 50 from range 0-100 to range 0-1
   result = scale(50, (0, 100), (0, 1))  # Returns 0.5

Notes
-----

- Angles are automatically clamped to the configured min/max range
- Pulse widths are automatically clamped to the configured min/max range
- Standard hobby servo: 1000-2000 µs for -90 to +90 degrees
- 1500 µs is neutral (0 degrees) by default
