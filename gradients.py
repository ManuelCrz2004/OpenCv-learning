import cv2 as cv
import numpy as np

img = cv.imread("Material/park.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel x", sobelx)
cv.imshow("Sobel Y", sobely)

bitwise = cv.bitwise_or(sobely, sobelx)
cv.imshow("Sobel", bitwise)

cv.waitKey(0)