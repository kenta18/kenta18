import cv2
import time
import imutils

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(1)
count =0
firstframe=None
area = 500
while True:
    ret, frame = cam.read()
    text='Normal'
    img = imutils.resize(frame, width=500)
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianimg = cv2.GaussianBlur(grayimg, (21, 21), 0)
    if firstframe is None:
        firstframe = gaussianimg
        continue
    imgdiff = cv2.absdiff(firstframe, gaussianimg)
    threshimg = cv2.threshold(imgdiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshimg = cv2.dilate(threshimg, None, iterations=2)
    cnts = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), 2)
        text = "moving object detected"

    if text=="moving object detected":
       count+=1
  

    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("cam img", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cam.release()
print(count)
cv2.destroyAllWindows()
