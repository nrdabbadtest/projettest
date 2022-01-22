#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 17:12:50 2021

@author: nourreddineabbad
"""

import cv2
import mediapipe as mp
import time

from handTrack_module import handDetector



pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)

detector = handDetector()

while True:

    success, img = cap.read()
    
    img = detector.findHands(img)
    
    lmlist = detector.findPosition(img)
    
    if len(lmlist) != 0 :
        print(lmlist[4])
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime 
    
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)