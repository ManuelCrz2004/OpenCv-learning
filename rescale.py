import cv2 as cv

img = cv.imread("OpenCvCourse/Material/cat.jpg")
cv.imshow('Cat', img)

def rescaleFrame(frame, scales = 0.75):
    # Works for Images, Videos and Live video
    width = int(frame.shape[1]* scales)
    height = int(frame.shape[0] * scales)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def chageRes(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4,height)
    
resized_image = rescaleFrame(img)
cv.imshow("Image", resized_image)

capture = cv.VideoCapture("OpenCvCourse/Material/dog.mp4")

while True: 
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow("Video", frame)
    cv.imshow("VideoResized", frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()