import time
import machine
from servo import Servo

servo_config = [
    #{ "pin" : 16, "reverse" : False},
    #{ "pin" : 16, "reverse" : False},
    { "pin" : 16, "reverse" : False}]

pins = [machine.Pin(cfg["pin"]) for cfg in servo_config]
print(pins)


# Create servo for each configuration
servos = [Servo(machine.Pin(cfg["pin"])) for cfg in servo_config]

delay = 0.01


# Quick demo
for cycle in range(10):
    for angle in range(180):
        for servo in servos:
            servo.write_angle(angle)
        time.sleep(delay)
