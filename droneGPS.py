from dronekit import connect, VehicleMode, Command
from pymavlink import mavutil
import time

COM = '/dev/ttyACM0'
vehicle = connect(COM, wait_ready=True)

while (True):
    print(vehicle.gps_0)
    print(vehicle.location.global_relative_frame)
    time.sleep(0.5)