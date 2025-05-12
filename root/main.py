# Assuming you already have the necessary imports, etc.
import cv2
from utils.snake import SnakeGame  # adjust if your filename is different

game = SnakeGame()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

import mediapipe as mp
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if lmList:
                index_finger_tip = lmList[8]  # 8 is index finger tip
                img = game.update(index_finger_tip, img)

            draw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
    else:
        img = game.update((0, 0), img)  # prevent crash if no hand

    cv2.imshow("Snake Game", img)
    key = cv2.waitKey(1)

    # 🚨 This listens for R to restart
    if key == ord('r') or key == ord('R'):
        game.reset()

    if key == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
