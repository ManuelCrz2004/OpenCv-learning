import cv2 as cv
import numpy as np

lower_yellow = (20, 120, 70)
upper_yellow = (30, 255, 255)

capture = cv.VideoCapture("Parqueadero.mp4")

# def PlateAnalisis(frame, ScndBlank_img, contours):
    
    
def detectPlate(frame, blank_img, second_blank_img):
    # Convert into HSV format
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # threshold video
    threshold = cv.inRange(hsv, lower_yellow, upper_yellow)
    cv.imshow("threshed", threshold)
    
    # getting image contours
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    plates_contours = []
    
    for c in contours:
        if cv.contourArea(c) > 2000:
            plates_contours.append(c)
        
    # Drawing identified contours
    cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
    cv.imshow("Contours image", blank)
    
    for i in plates_contours:
        plate_area = cv.contourArea(i)
        if plate_area > 2000:
            plates_contours.append(i)
            x, y, w, h = cv.boundingRect(i)
            cropped_plate = frame[y:y+h, x:x+w]
            cv.rectangle(frame, (x,y), (x + w, y + h), (36, 255, 12), 2)
            
            
    print(f"{plates_contours}")
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

