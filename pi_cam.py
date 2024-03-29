import numpy as np
import cv2
import os

filename='video.avi'
fps=24.0
my_res='480p'

# Set resolution for the video capture
# Function adapted from the https://kirr.co/016qmh
def change_res(cap,width,height):
    cap.set(3,width)
    cap.set(4,height)

# Standard Video Dimensions Sizes
STD_DIMENTIONS={
"480p": (640,480),
"720p": (1280,720),
"1080p": (1920,1080),
"4k": (3840,2160)
}

def get_dims(cap,res='720p'):
    width,height=STD_DIMENTIONS['480p']
    if res in STD_DIMENTIONS:
        width,height=STD_DIMENTIONS[my_res]
    change_res(cap,width,height)
    return width,height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE={
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext=os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap=cv2.VideoCapture(0)
dims=get_dims(cap,res=my_res)

video_type_cv2=get_video_type(filename)

out=cv2.VideoWriter(filename,video_type_cv2,fps,dims) # can put width/height instead of dims

while(True):
    # Capture frame by frame
    ret, frame=cap.read()
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destoryAllWindows()
