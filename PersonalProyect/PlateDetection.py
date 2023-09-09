import cv2 as cv
import numpy as np

lower_yellow = (20, 120, 70)
upper_yellow = (30, 255, 255)

capture = cv.VideoCapture(0)

while True:
    # getting photogram frame
    isTrue, frame = capture.read()
    
    # # Creating blank
    # blank = np.zeros(frame.shape, dtype="uint8")
    
    # Convert into HSV format
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # threshold video
    threshold = cv.inRange(hsv, lower_yellow, upper_yellow)
    cv.imshow("threshed", threshold)
    
    # getting image contours
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        
    # Drawing identified contours
    # cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
    # cv.imshow("Contours image", blank)
    
    # Getting largest measure of contour
    largest_contour = max(contours, key=cv.contourArea)
    
    # Drawing square at original video
    cv.drawContours(frame, [largest_contour], -1, (0, 255, 0), 1)
    
    # Draw square around yellow square
    x, y, w, h = cv.boundingRect(largest_contour)
    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # # Getting a new video screen
    # new_video = cv.VideoWriter("zoomed_in.avi", cv.VideoWriter_fourcc('M','J','P','G'), 25, (w, h))
    
    # for i in range(0, h):
    #     for j in range(0, w):
    #         new_video.write(frame[y + i][x + j])
            
    # cv.imshow("zoomed plate video", new_video)
    
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

    capture.release()
    cv.destroyAllWindows()