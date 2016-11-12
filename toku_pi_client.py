import socket
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time

import RPi.GPIO as GPIO

# timer triggers webcam to take image
time.sleep (60)
os.system('fswebcam --no-banner haikucam.jpg')

# save record of image
#time2 = time.time()
#filename = "/Users/rollasoul/densecap/imgs/saved/%sa-image.jpg"%time2
#cv2.imwrite(filename, image)

# send image and light sensor input
s = socket.socket()
host = "YOUR SERVER ADDRESS HERE !!!!"
port = 12345
s.connect((host, port))
time.sleep (2)
f=open ("haikucam.jpg", "rb") 
l = f.read(4096)
while (l):
      s.send(l)
      l = f.read(4096)
time.sleep(3)
print "image sent"   
s.close()                # Close the connection

    # wait for densecap & rnn lib to handwrite haiku and create image
print "done"
time.sleep(6)

s = socket.socket()
host = "YOUR SERVER ADDRESS HERE !!!!"
port = 12345
s.connect((host, port))

print "waiting for image"
os.chdir('/home/pi/toku')

while True:
        i=1
        f = open('haiku'+".png",'wb')
        i=i+1
        while (True):
        # receive and write file
                l = s.recv(1024)
                while (l):
                        f.write(l)
                        l = s.recv(1024)
                        print "file received"
                        s.send("file received")
                s.close()
                f.close()
                break
