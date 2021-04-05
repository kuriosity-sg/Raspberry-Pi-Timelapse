from picamera import PiCamera
from time import sleep
from os import system
import datetime

#set the time to run the timelapse
runningMinutes = 1
#delay between each photo taken in seconds
sleepDelay = 1
#total number of photos to take based on running minutes and sleep delay
totalPhotos = int((runningMinutes*60)/sleepDelay)

#create camera object
camera = PiCamera()
#set the image resolution
camera.resolution = (1024, 768)

#create a loop to take multiple images
for i in range(totalPhotos):
    #capture image and name it in a 4-digit sequence
    camera.capture('/home/pi/Pictures/image{0:04d}.jpg'.format(i))
    #wait before taking next image
    sleep(sleepDelay)

#get the current datetime
dateraw= datetime.datetime.now()
#format datetime into year, month, date, hour, minute
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
#use ffmpeg to create video from images
system('ffmpeg -r {} -f image2 -s 1024x768 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(30, datetimeformat))
