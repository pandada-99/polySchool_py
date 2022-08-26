import cv2
import os

pwd = os.getcwd()
print(pwd)
print(os.listdir(pwd))

files = os.listdir(pwd)

def getFrame(sec, f):
    vidcap = cv2.VideoCapture(f)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    file_name = f.replace(".mp4", "")
    if hasFrames:
        cv2.imwrite("images/" + file_name + str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames


for f in files:
    if "mp4" not in f:
        print("not video file!")
        continue
    sec = 0
    frameRate = 0.5
    count = 1
    success = getFrame(sec, f)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, f)