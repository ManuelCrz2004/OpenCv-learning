# Blurring an image, lot of noise, lighting or distraction to the analysis
import cv2 as cv

img = cv.imread("OpenCvCourse/Material/cats.jpg")
cv.imshow("Cats", img)

# Kernell: Window 3x3 of a specific places on an image, you can setup your own size (previous was an example)


# Avaraging
avarage = cv.blur(img, (3, 3))
cv.imshow("Avarage Blur", avarage)

# Gauusian Blur
gauus = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gauus)

# Median Bleur (same as avaraging, but takes the median)
median = cv.medianBlur(img, 3)
cv.imshow("Median bleur", median)

# Bilateral bleur (most efectivs: how it bleus, retain edges)
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral bleur", bilateral)

cv.waitKey(0)