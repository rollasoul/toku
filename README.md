# T O K U

Script for handwriting haiku-poems to camera input powered by two neural networks (densecap and rnnlib) - and printing them on a mini-thermal printer. Should be run on remote server and local-client, optimised for raspberry-pi. Both networks come ready to go and trained as a docker-image for the server, the git-repo is mainly for the client side (with the main server-script as read-me/edit-me backup). 

# prerequisites
- ubuntu 16.04 server running intel xeon processors (or newer) otherwise openBLAS/torch will give you a core dumped error
- raspberry pi zero or 3 running [raspbian jessie 2016-05-31 or older](http://downloads.raspberrypi.org/raspbian/images/) - Pixel is not supported yet
- usb camera and adafruit mini-thermal printer

# server setup

- install docker on remote server
```
sudo apt-get install docker.io
```

- start docker machine
```
service docker start
```

- pull image for densecap and rnnlib as a package (including trained models and server scripts) from docker-cloud repository:
```
docker pull rollasoul/toku

```

- run docker image with port forwarding for port 12345
```
docker run -it -p 12345:12345 rollasoul/toku
```

# client setup

- download or clone git-repo on client (raspberry pi or mac)
```
git clone https://github.com/rollasoul/toku/
```

- download and install fswebcam for the usb-camera
```
sudo apt-get install fswebcam
```

- open the toku_pi_client.py file and replace the server address with the the address of your server (line 29 and 48)

- check both script_pi and toku_pi_client.py for correct file addresses as they are set up for /home/pi/toku - structure

- follow the installation instructions on adafruit for the [adafruit mini-thermal printer](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/overview), in case you encounter problems with the printer setup

  disable serial-port for console
  ```
  sudo systemctl disable serial-getty@ttyAMA0.service
  ```
  remove the reference to tty0 or tty1 in the /boot/cmdline.txt file
  ```
  nano /home/pi/boot/cmdline.txt
  ```
  enable_uart=1 in the /boot/config.txt file
  ```
  nano /home/pi/boot/config.txt
  ```
  and make sure the data cables are properly connected, a loose data connection will make the printer print gibberish, now test it with 
  ```
  echo "ready" | lpr
  ```  
 You can play with the printer settings to get a better haiku (set Gamma to 1, resize the image to 50 %)
  
# hardware setup

- check all cables and connections (camera, raspberry pi, mini-thermal printer)
- raspberry pi needs proper wifi-connectivity to run this script

# run toku

now comes the fun part! 

- on server run
```
script_pi
```

- on client run 
```
script_pi
```

Both scripts are endless loops, the client script waits for 1 minute after it was started before it takes a picture with the webcam, the server script waits for the image of the client. Once the webcam takes the image and sends it off to the server, densecap will generate 83 captions for the image. The script selects captions with 5 and 7 syllables. By random a 5 syllables caption, a 7 syllables caption and a 5 syllable caption will be selected and taken as 3 lines of the haiku. Rnnlib runs each line through its network and predicts a possible handwriting for them. This handwriting is plotted with an Octave-script and an image of the full handwritten haiku gets sent back to the client and printed on the thermal printer. The whole process takes about 1 minute on a 3.4 GHz/32 GB RAM server. 

And here you go! Your own TOKU handwriting and printing poems about its surroundings.   
