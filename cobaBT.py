from bluetooth import *
import time
bd_addr = "00:21:13:03:80:B4"
port = 1
sock = BluetoothSocket (RFCOMM)
sock.connect((bd_addr,port))
print ('waiting')
while 1:
    data = sock.recv(1024)
    if len(data) == 0:
        break
    data = str(data)
    print (data)    
    time.sleep(0.5)
sock.close()