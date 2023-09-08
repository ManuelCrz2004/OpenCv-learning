import cv2 as cv

img = cv.imread("OpenCvCourse/Material/park.jpg")
cv.imshow('Cat', img)

# Converting image into greyscales
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cat', gray)

# Blur an image (Gaussian)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) # Highest tuple value (impar) more blur (borroso)
cv.imshow("Blur image", blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny image", canny) # To get less edges, you can apply edge cascade with a blured image

# Dilating an image (Dilatar)
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated Image", dilated)

# Eroding (Opposite of dilating)
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow("Eroded Dilate image", eroded)

# Resize
resize = cv.resize(img, (500, 500))
cv.imshow("Resized image", resize)

# Cropping
crop = img[50:200, 200:400]
cv.imshow("Cropped image", crop)


cv.waitKey(0)