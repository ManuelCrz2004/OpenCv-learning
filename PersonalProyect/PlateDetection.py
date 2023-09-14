import cv2 as cv
import numpy as np

lower_yellow = (20, 120, 70)
upper_yellow = (30, 255, 255)

capture = cv.VideoCapture("Parqueadero_2.mp4")

def rescaleFrame(frame, scales = 0.75):
    # Works for Images, Videos and Live video
    width = int(frame.shape[1]* scales)
    height = int(frame.shape[0] * scales)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def detectPlate(frame, blank_img, second_blank_img):

    # Getting cropped image fragment
    h, x, c = frame.shape

    # New image analysis
    # Y
    x1 = int(h /3)
    x2 = (x1 * 2)

    # X configurations
    y1_len = (x/2)
    y1 = int(x/3 - y1_len/6)
    y2 = int(y1 + y1_len)

    cropped_img = frame[x1:x2, y1:y2]
    cv.imshow("Cropped", cropped_img)
    # Convert into HSV format
    hsv = cv.cvtColor(cropped_img, cv.COLOR_BGR2HSV)

    # threshold video
    threshold = cv.inRange(hsv, lower_yellow, upper_yellow)
    cv.imshow("threshed", threshold)

    # getting image contours
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    h, x, c = frame.shape
    
    x1 = int(x/3)
    x2 = (x1 * 2)
    
    y1 = int(h/3)
    y2 = (y1 * 2)
    
    img_recortada = frame[y1:y2, x1:x2]
    cv.imshow("Imagen recortada", img_recortada)
        
    # Drawing identified contours

    cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
    cv.imshow("Contours image", blank)

    for i in contours:
        plate_area = cv.contourArea(i)
        # print(f"{plate_area}")
        if plate_area > 35:
            x, y, w, h = cv.boundingRect(i)
            cropped_plate = cropped_img[y:y+h,x:x+w]
            cropped_plate = rescaleFrame(cropped_plate, 10)
            cv.rectangle(frame, (y1 + x, x1 + y), (y1 +x + w, x1 + y + h), (36, 255, 12), 2)


    # print(f"{contours}")
    cv.imshow("Video", frame)
    try:
        cv.imshow("Cropped_PLATE", cropped_plate)
    except:
        print("No plate detected")




while True:
    # getting photogram frame
    isTrue, frame = capture.read()

    # Rescaling frame
    
    # y_frame, x_frame, c = frame.shape
    # y1_frame = int(y_frame / 3)
    # y2_frame = int(y1_frame * 2)
    
    # frame = frame[y1_frame:y2_frame, 0:x_frame]
    
    # frame = rescaleFrame(frame, 1.5)

    # Creating necesary blank images
    blank = np.zeros(frame.shape, dtype="uint8")
    second_blank = np.zeros(frame.shape, dtype="uint8")

    detectPlate(frame, blank, second_blank)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break

