from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

COMPORT = '/dev/ttyACM0'

vehicle = connect(COMPORT, wait_ready=True)
print('Connected to Drone at port ' + COMPORT)

while(True):
    print(vehicle.gps_0)
    print(vehicle.location.global_relative_frame)
    time.sleep(0.5)
