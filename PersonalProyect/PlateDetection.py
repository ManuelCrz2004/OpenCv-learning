import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image

lower_yellow = (20, 120, 70)
upper_yellow = (30, 255, 255)

capture = cv.VideoCapture("Parqueadero_2.mp4")

def rescaleFrame(frame, scales = 0.75):
    # Works for Images, Videos and Live video
    width = int(frame.shape[1]* scales)
    height = int(frame.shape[0] * scales)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def detectPlate(frame, plate_image):

    # Convert into HSV format
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # threshold video
    threshold = cv.inRange(hsv, lower_yellow, upper_yellow)
    cv.imshow("threshed", threshold)

    # getting image contours
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Showing images contours
    cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
    cv.imshow("Contours image", blank)
    
    # Drawing square around a plate
    for i in contours:
        plate_area = cv.contourArea(i)
        if plate_area > 2000:
            x, y, w, h = cv.boundingRect(i)
            if plate_image == None:
                plate_image = cv.imwrite("foto_vehiculo.jpg", frame[y-450:y+h+40, x-240:x+w+240])
                id_vehiculo = pytesseract.image_to_string(Image.open("foto_vehiculo.jpg"))
                print(id_vehiculo)
            cv.rectangle(frame, (x, y), (x + w, y + h), (36, 255, 12), 2)
            
        
    cv.imshow("Placa", cv.imread("foto_vehiculo.jpg"))
    cv.imshow("Video", frame)




while True:
    # getting photogram frame
    isTrue, frame = capture.read()

    blank = np.zeros(frame.shape, dtype="uint8")
    second_blank = np.zeros(frame.shape, dtype="uint8")
    plate_image = None

    detectPlate(frame, plate_image)


    if cv.waitKey(20) & 0xFF==('d'):
        break

