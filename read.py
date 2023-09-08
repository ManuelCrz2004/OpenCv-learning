import cv2 as cv

### Reading a video
img = cv.imread("OpenCvCourse/Material/cat.jpg")  #path to the image
cv.imshow("Cat",img )

cv.waitKey(0)

### Reading a Video
capture = cv.VideoCapture("OpenCvCourse/Material/dog.mp4") # path to the video

# Viedo capture funcionto
while True: 
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()