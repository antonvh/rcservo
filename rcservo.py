"""RC Servo PWM Controller Library

A minimal single-file module providing `Servo` and `scale` utilities.
Supports both standard Python and MicroPython environments.
"""

try:
    from machine import Pin, PWM
except Exception:
    # Import failed. Not on MicroPython or hardware not available.
    Pin = None
    PWM = None


def scale(val, src, dst):
    """Scale a value from range ``src`` to range ``dst``.

    Parameters
    - val: number to scale
    - src: tuple (min, max) source range
    - dst: tuple (min, max) destination range

    Returns the scaled value as float.
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


class Servo:
    """Class to control a hobby servo.

    By default 1500 is neutral (0º), 2000 is far right (90º), 1000 is far left (-90º).

    Args:
        pin (int): IO Pin for the servo data line.
        min_pulse (int): Min pulse width in µs for a 2ms frame. Defaults to 1000.
        max_pulse (int): Max pulse width in µs for a 2ms frame. Defaults to 2000.
        min_angle (int): Minimum angle at min pulse. Defaults to -90.
        max_angle (int): Maximum angle at max pulse. Defaults to 90.
    """

    def __init__(
        self, pin, min_pulse=1000, max_pulse=2000, min_angle=-90, max_angle=90
    ):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        if PWM is None or Pin is None:
            # Running in a non-hardware environment; defer creating PWM object until used
            self.servo = None
            self._pin = pin
        else:
            self.servo = PWM(Pin(pin), freq=50)

    def _ensure_hw(self):
        if self.servo is None and PWM is not None and Pin is not None:
            self.servo = PWM(Pin(self._pin), freq=50)

    def pwm(self, pwm):
        """Set servo pulse width in µs for a 2ms frame.

        The pulse value is clamped between configured min and max pulse widths.
        """
        pwm = min(max(pwm, self.min_pulse), self.max_pulse)
        self._ensure_hw()
        if self.servo is None:
            # No hardware available; nothing to do.
            return
        # Convert microseconds in ~2ms frame to 16-bit duty (Raspberry Pi Pico style)
        self.servo.duty_u16(int(pwm * 3.2768))

    def angle(self, angle: float) -> None:
        """Set servo angle. Values are capped between min_angle and max_angle."""
        angle = min(max(angle, self.min_angle), self.max_angle)
        pwm = scale(
            angle, (self.min_angle, self.max_angle), (self.min_pulse, self.max_pulse)
        )
        self.pwm(pwm)


__version__ = "0.1.0"
__author__ = "Anton Vanhoucke"
__all__ = ["Servo", "scale"]
