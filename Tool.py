#we are integrate everything into one giant file of python code..
# there are three templates that have been created.
import RPi.GPIO as gpio
import subprocess
import pyAesCrypt
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
t=0
# initially we must show ready for encryption
def encrypt(channel) :
	 #encryption button
	proc = subprocess.Popen(['ls','/media/pi'],stdout=subprocess.PIPE)
	output = proc.stdout.read()
	str=output.decode()
	for ele in str:
		if(ele!='\n'):
			uuid+=ele
		else :
			break
	try: 
	 f = open("/media/pi/"+uuid+"/secret/rawtext.txt","rb")
	except: 
	 draw.text((x,top + 16), "but the pen-drive", font=font, fill=255)
	 draw.text((x,top + 25), "is not connected", font=font, fill=255)
	else:
	 t=1	
RST = None
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
eb=12
gpio.setmode(gpio.BOARD)
gpio.setup(eb, gpio.IN, pull_up_down=gpio.PUD_DOWN) #initially we have a low input.
#gpio.setup(y, gpio.IN, pull_up_down=gpio.PUD_DOWN) #similiarly for the other input.
#encryption button
# db= ? decryption button.
uuid=""
font = ImageFont.load_default()
while t==0:

    # Draw a black filled box to clear the image.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.text((x, top),  "The device is ready"     ,  font=font, fill=255)
	draw.text((x, top+8),  "for encryption"   , font=font, fill=255)
	gpio.add_event_detect(eb, gpio.RISING, callback=encrypt)
    #draw.text((x, top+16), ""   ,  font=font, fill=255)
    #draw.text((x, top+25),    ,  font=font, fill=255)
    # Display image.
	disp.image(image)
	disp.display()
    # the device would check everytime now.
    #gpio.add_event_detect(db, gpio.RISING, callback=decrypt)
	time.sleep(.1)
disp.clear()
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pro=0
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
#disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
pro=0
while True: 
	try:
	 if(pro==0) :
	 	pyAesCrypt.encryptFile("/media/pi/"+uuid+"/secret/rawtext.txt", "/media/pi/"+uuid+"/secret/converted/rawtext.txt.aes", password, bufferSize)
	except:
	 raw.rectangle((0,0,width,height), outline=0, fill=0)
	 draw.text((x,top), "A runtime error:", font=font, fill=255)
	 draw.text((x,top + 8), "possible: file_NP", font=font, fill=255)
	 disp.image(image)
	 disp.display()
	 time.sleep(.1)
	else:
	 draw.rectangle((0,0,width,height), outline=0, fill=0)
	 draw.text((x,top), "The file is encrypted", font=font, fill=255)
	 draw.text((x,top + 8), "succesfully", font=font, fill=255)		
	 pro=1
	 disp.display()
	 time.sleep(.1)
