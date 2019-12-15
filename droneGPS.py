from dronekit import connect, VehicleMode, Command
from pymavlink import mavutil
from bluetooth import *
import time

COM = '/dev/ttyACM0'
vehicle = connect(COM, wait_ready=True)
    
bd_addr = "00:21:13:03:80:B4"
port = 1
sock = BluetoothSocket (RFCOMM)
sock.connect((bd_addr,port))
time.sleep(1)

while 1:
    print("Drone GPS : ")
    print(vehicle.gps_0)
    print(vehicle.location.global_relative_frame)
    
    data = sock.recv(1024)
    latit = data[:9]
    longi = data[10:]
    latit = float(latit)
    longi = float(longi)
    print ("User GPS : ")
    print (latit, longi)
    time.sleep(1)
sock.close()