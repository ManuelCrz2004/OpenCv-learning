# Allow to se pixels distributions for RGB and GRAYSCALE images (0 to 256 - black to white) 
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Material/cats.jpg")
cv.imshow("img", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# Creating mask paramater for certain part of image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)



# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray img", gray)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("mask", masked)


# # Histogram for grayscales 
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title("Grayscale histogram")
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Colour histogram

plt.figure()
plt.title("Colour histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([masked], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)