import cv2
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'‪C:\Program Files\tesseract.exe'

def recText(filename):
    text=pytesseract.image_to_string(img)
    return text
cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    text = "Normal"

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == 27:
        info = recText(img)
        print("Conversion:\n",info)
        break


cam.release()
cv2.destroyAllWindows()
