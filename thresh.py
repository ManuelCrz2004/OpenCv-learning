import cv2 as cv

img = cv.imread("Material/cats.jpg")
cv.imshow("img", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grat", gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 155, 255, cv.THRESH_BINARY)
cv.imshow("simple tresholede", thresh)

threshold, thresh_inverse = cv.threshold(gray, 155, 255, cv.THRESH_BINARY_INV)
cv.imshow("Inverted simple thresholede", thresh_inverse)


# Adoptive thresholding
adaptive_thres = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptativve thresholded", adaptive_thres)

cv.waitKey(0)