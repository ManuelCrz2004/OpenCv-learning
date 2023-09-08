import cv2 as cv

video = cv.VideoCapture(0   )

while True:
    isTrue, frame = video.read()
    cv.imshow("frame", frame)
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("gray frame", gray)
    
    canny = cv.Canny(gray, 125, 175)
    cv.imshow("canny framme", canny)
    
    if cv.waitKey(1) == 27:
        break
    
video.release()
cv.destroyAllWindows()