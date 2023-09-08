# Contour meaning is "contornos"
import cv2 as cv
import numpy as np



img = cv.imread("OpenCvCourse/Material/cats.jpg")

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)

cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

blur = cv.blur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blur", blur) 

canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

# Contour method ->
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)}')

# Drawing contours on a blank
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("controus img", blank)

# LIST -> ALL
# EXTERNAL -> EXTENARL
# TREE -> COTORNS ON HIRECICHAL

# APROX:
#     NONE: NO APROXIMATION
#     SIMPLE: GENERAL AND EASIAST
cv.waitKey(0)
 