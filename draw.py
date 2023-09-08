import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blanck', blank)

# img = cv.imread("OpenCvCourse/Material/cat.jpg")
# cv.imshow("Cat", img)

# 1. Paint the image a certain colour
# Setting a colored squared at the image
blank[200:300, 300:400] = 0, 255, 0  # RGB Color scale
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,250,0), thickness=-1)
cv.imshow("Rectangle", blank)

#3. Draw a cirche
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,250), thickness=1)
cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(blank, (0,500), (250,250), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, "Hello world", (115, 115), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255, 0),2)
cv.imshow("Text", blank)

cv.waitKey(0)