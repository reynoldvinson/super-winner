from bluetooth import *
import time
bd_addr = "00:21:13:03:80:B4"
port = 1
sock = BluetoothSocket (RFCOMM)
sock.connect((bd_addr,port))
data = sock.recv(1024)
data = data.decode()
time.sleep(60)
#print ('waiting')
while 1:
    #data = sock.recv(1024)
    #data = data.decode()
    print (data)    
    time.sleep(1)
sock.close()