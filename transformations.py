import cv2 as cv
import numpy as np


img = cv.imread("OpenCvCourse/Material/park.jpg")

cv.imshow("Boston", img)

# Transaltion
def translateImg(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x: Left
# -y: Upa
# x: Right
# y: Down

translate = translateImg(img, 100, 100)
cv.imshow("translated img", translate)

# Rotation
def rotateImg(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotateImg(img, 45,)
cv.imshow("Rotated img", rotated)

# Resize
resized = cv.resize(img, (500, 5000))
cv.imshow("Resize", resized)

# Flip image
flip = cv.flip(img, 1)
cv.imshow("Fliped0", flip)

# Cropping
cropped = img[200:400, 0:200]
cv.imshow("Cropped", cropped)



cv.waitKey(0)