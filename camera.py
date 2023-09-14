#initialization of packages used in program
from picamera import PiCamera
from datetime import datetime
from time import sleep


#initialize the camera variable as a PiCamera object
camera=PiCamera()

#intialize all variables to be used in program please use this section to modify the variables for calls later in the program (also note all numbers are in seconds)

#how long for the camera to sleep between pictures
sleepTime = 2

#number of pictures to be taken by program loop (note that numPictures + sleepTime will be the amount of time the program will run unless otherwise specified)
numPictures = 5

#this is where the pictures will be stored ***the %s will change based on the loop number so the pictures have different names
pictureDirectory='/home/pi/Desktop/norris_shared/pictures/image%s.jpg'

#set resolution for camera
camera.resolution = (1280, 720)

#this is where the videos will be stored ***the %s will change based on the loop number so the videos have different names
videoDirectory = '/home/pi/Desktop/norris_shared/images/videos%s.h264'

#length of video segments (camera currently set to run indefinitely so this will only change the file size saved to directory, and how many files you will have)
videoLength = 1800


def take_picture(camera):

    #camera.start_preview()    ***add in only fi you would like a preview of the picture that it will take
    for i in range(numPictures):
        sleep(sleepTime)
        currentTime = datetime.now()
        camera.annotate_text = str(currentTime)
        camera.capture(pictureDirectory %i)
        
    #camera.stop_preview()    ***make sure this is enabled if the start preview commmand is enabled 
    
def take_video(camera):
    #j is the jth video that has been recorded while this function runs
    j=0

    #while True loops with no other conditions run indefinitely
    while True:
        camera.start_recording('/home/pi/Desktop/norris_shared/videos/video%s.h264' %j)
        camera.wait_recording(videoLength)
        camera.stop_recording()
        #increment the j value to tell how many videos have been shot from this function
        j += 1
    

### If need to rotate camera use the following command ###
#camera.rotation = 180

### Below are the function calls, depending on what you would like you camera to do please only have one active at a time ###
#take_picture(camera)
take_video(camera)




