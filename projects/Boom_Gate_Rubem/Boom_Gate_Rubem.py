# ---------------------------------------------------------------------- Imports

import time

from fischertechnik.controller.Motor import Motor  # type: ignore

from lib.controller import *
from lib.display import *

# ------------------------------------------------------------------- Initialize

speed = 200
vehicle_counter = 0
half_brightness = 256
green_led_interval = 0.4

display.set_attr("vehicles.text", "Vehicles: none")

# -------------------------------------------------------------------- Main loop

gate_led.set_brightness(512)

while True:

    # Close gate if open
    gate_motor.set_speed(int(speed), Motor.CW)
    gate_motor.start_sync()
    while not home_switch.is_closed():
        time.sleep(0.01)
    gate_motor.stop_sync()
    red_led.set_brightness(0)

    # Wait for garage button

    green_led.set_brightness(half_brightness)
    while not garage_button.is_closed():
        time.sleep(0.01)
    green_led.set_brightness(0)

    # Open gate and count until stop

    gate_motor.set_speed(speed, Motor.CCW)
    gate_motor.set_distance(64)
    while gate_motor.is_running():
        time.sleep(0.01)

    # Wait for vehicle

    brightness = half_brightness
    green_led.set_brightness(brightness)
    now = time.time()
    while photo_transistor.is_bright():
        # Blink green LED
        if time.time() - now > green_led_interval:
            brightness = half_brightness - brightness
            green_led.set_brightness(brightness)
            now = time.time()
        time.sleep(0.01)
    red_led.set_brightness(half_brightness)
    green_led.set_brightness(0)

    # Increment counter

    vehicle_counter = (vehicle_counter if isinstance(vehicle_counter, (int, float)) else 0) + 1
    display.set_attr("vehicles.text", str("Vehicles: " + str(vehicle_counter)))

    # Vehicle passed

    while photo_transistor.is_dark():
        time.sleep(0.01)
    time.sleep(2)

# -------------------------------------------------------------------------- End
