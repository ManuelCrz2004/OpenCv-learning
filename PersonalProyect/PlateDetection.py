import cv2 as cv
import numpy as np

lower_yellow = (20, 120, 70)
upper_yellow = (30, 255, 255)

capture = cv.VideoCapture("Parqueadero.mp4")
    
    
def detectPlate(frame, blank_img, second_blank_img):
    # Convert into HSV format
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # threshold video
    threshold = cv.inRange(hsv, lower_yellow, upper_yellow)
    cv.imshow("threshed", threshold)
    
    # getting image contours
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    h, x, c = frame.shape
    
    x1 = int(x/3)
    x2 = (x1 * 2)
    
    y1 = int(h/3)
    y2 = (y1 * 2)
    
    img_recortada = frame[y1:y2, x1:x2]
    cv.imshow("Imagen recortada", img_recortada)
        
    # Drawing identified contours
    cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
    cv.imshow("Contours image", blank)
    
    for i in contours:
        plate_area = cv.contourArea(i)
        if plate_area > 2000:
            x, y, w, h = cv.boundingRect(i)
            cropped_plate = frame[y:y+h, x:x+w]
            cv.rectangle(frame, (x,y), (x + w, y + h), (36, 255, 12), 2)
            
            
    print(f"{contours}")
    cv.imshow("Video", frame)
    cv.imshow("Cropped", cropped_plate)
    
    


while True:
    # getting photogram frame
    isTrue, frame = capture.read()
    
    # Creating necesary blank images
    blank = np.zeros(frame.shape, dtype="uint8")
    second_blank = np.zeros(frame.shape, dtype="uint8")
    
    detectPlate(frame, blank, second_blank)
    
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

