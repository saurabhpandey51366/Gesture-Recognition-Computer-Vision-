import cv2
import numpy as np
import time
import HandTackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


######################################
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPercent = -(volume.GetMasterVolumeLevel())
area = 0
colorVol = (255, 0, 0)
#######################################


######################################

wCam, hCam = 640, 480

######################################

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0

detector = htm.HandDetector(detectionCon=0.7, maxHands=1)

def gestureVolumeControl(img):

    #find hand
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        #Filter based on size
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        if 250 < area < 1000:
            #Find distance between index and the thumb
            length, img, lineInfo = detector.findDistance(4, 8, img)

            #convert volume
            volBar = np.interp(length, [15, 150], [400, 150])
            volPercent = np.interp(length, [15, 150], [0, 100])

            #reduce resolution to make it smoother
            smoothness = 10
            volPercent = smoothness * round(volPercent/smoothness)

            #check fingers up
            fingers = detector.fingersUp()

            #if pinky is down set volume
            if not fingers[4]:
                volume.SetMasterVolumeLevelScalar(volPercent/100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 8, (0,255,0), cv2.FILLED)

            #drawing
            cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 255), 3)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 255), cv2.FILLED)
            cv2.putText(img, f'{int(volPercent)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3)
            cVol = int(volume.GetMasterVolumeLevelScalar()*100)
            cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3)
  


while True:
    success, img = cap.read()
    gestureVolumeControl(img)
    
    #Frame rate
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)