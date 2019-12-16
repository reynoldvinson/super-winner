#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2015-2016, 3D Robotics.
Full documentation is provided at http://python.dronekit.io/examples/simple_goto.html
"""

from __future__ import print_function
from bluetooth import *
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

COMPORT = '/dev/ttyACM0'

vehicle = connect(COMPORT, wait_ready=True)
print('Connected to Drone at port ' + COMPORT)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    #while not vehicle.is_armable:
    #    print(" Waiting for vehicle to initialise...")
    #    time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


arm_and_takeoff(3)

print("Set default/target airspeed to 0.5")
vehicle.airspeed = 0.5

bd_addr = "00:21:13:03:80:B4"
port = 1
sock = BluetoothSocket (RFCOMM)
sock.connect((bd_addr,port))
time.sleep(1)
while 1:
    if vehicle.mode.name != "GUIDED":
        continue
    altitude = 3
    data = sock.recv(1024)
    latitude = data[:9]
    longitude = data[10:]
    latitude = float(latitude)
    longitude = float(longitude)
    print (latitude, longitude)
    #print("Going to user") 
    #user = LocationGlobalRelative(latitude, longitude, altitude)
    #vehicle.simple_goto(user)
    time.sleep(1)
sock.close()

print("Close vehicle object")
vehicle.close()