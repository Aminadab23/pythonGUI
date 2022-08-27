import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
handDetector = mp.solutions.hands.Hands()
while True:
    _, frame = cap.read()
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(0)