import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("OpenCvCourse/Material/park.jpg")
cv.imshow("park", img)

plt.imshow(img)
plt.show()

# BGR to Grayscales
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray img", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

plt.imshow(rgb)
plt.show()

# TO PROCESS COLORS AT

cv.waitKey(0)