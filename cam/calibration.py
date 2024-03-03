import cv2
import keyboard
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(1)  # Change the index to 0 for the laptop's built-in camera
cap2 = cv2.VideoCapture(2) 
num = 0

while cap.isOpened():
    success, img = cap.read()
    success2, img2 = cap2.read()
    cv2.waitKey(10)

    if keyboard.is_pressed('s'):
        cv2.waitKey(100)
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', img)
        cv2.imwrite('images/stereoRight/imageR' + str(num) + '.png', img2)
        print("Image saved!")
        num += 1
        
    elif keyboard.is_pressed('q'):
        break

    cv2.imshow('Img 1', img)
    cv2.imshow('Img 2', img2)

cap.release()
cap2.release()

cv2.destroyAllWindows()