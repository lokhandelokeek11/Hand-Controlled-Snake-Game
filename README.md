# 🐍 Hand-Controlled Snake Game with OpenCV and MediaPipe

A fun, gesture-controlled Snake game built using **OpenCV** and **MediaPipe**, where you control the snake using just your hand! This game was developed in Python and is a cool mix of computer vision and gaming logic.

## 🎮 Features

- Control the snake with your hand using a webcam 📷
- Real-time finger tracking with MediaPipe 🤚
- Classic snake gameplay logic
- Score display in-game
- Restart the game with a key press (`R`)

## ⚙️ Requirements

- Python 3.7 or above
- OpenCV
- MediaPipe
- Numpy
- [Optional] Sound support: playsound (for sound effects, currently disabled)

## 🔧 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lokhandelokeek11/snake-opencv-mediapipe.git
   cd snake-opencv-mediapipe
   
## 📸 Screenshot 

 ![image](https://github.com/user-attachments/assets/9be9ad15-e55d-4d81-a3b9-32088b3f8452)


## 🧠 How It Works
1. Uses MediaPipe to detect and track hand landmarks.
2. The tip of the index finger is used to control the snake's head.
3. Food is placed randomly on the screen. When the snake touches it, the score increases.
4. Collision with itself ends the game and displays a restart prompt.

## 🛠️ Future Enhancements
1. Add sound support (fix playsound issues on Windows)
2. Add levels or speed increase with score
3. Add leaderboard using file or database
4. Package into .exe for offline sharing
