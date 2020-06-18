import numpy as np
import  cv2 as cv
cap = cv.VideoCapture('vtest.avi')
#fgbg = cv.createBackgroundSubtractorMOG2()
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=True) # (shadow will be shown in gray color) detectShadows=True
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard ==27:
        break
cap.release()
cv.destroyAllWindows()