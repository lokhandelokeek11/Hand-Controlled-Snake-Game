import cv2
import random
import time
import pygame
from playsound import playsound
import threading

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.points = [(100, 100)]
        self.lengths = [0]
        self.total_length = 0
        self.allowed_length = 150
        self.previous_head = (100, 100)
        self.food = self.random_food()
        self.score = 0
        self.game_over = False
        self.food_radius = 10
        self.snake_thickness = 15
        self.speed_increment = 10

    def random_food(self):
        return random.randint(100, 500), random.randint(100, 400)

    def play_eat_sound(self):
        try:
            threading.Thread(target=playsound, args=("eat.wav",), daemon=True).start()
        except:
            pass

    def update(self, cursor, frame):
        if self.game_over:
            cv2.putText(frame, "GAME OVER", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            cv2.putText(frame, f"Score: {self.score}", (230, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(frame, "Press 'R' to Restart", (180, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 0), 2)
            return frame  # No game over message

        px, py = self.previous_head
        cx, cy = cursor

        self.points.append((cx, cy))
        distance = ((cx - px) ** 2 + (cy - py) ** 2) ** 0.5
        self.total_length += distance
        self.lengths.append(distance)
        self.previous_head = (cx, cy)

        while self.total_length > self.allowed_length:
            self.total_length -= self.lengths[0]
            self.lengths.pop(0)
            self.points.pop(0)

        # Draw Snake
        for i in range(1, len(self.points)):
            cv2.line(frame, self.points[i - 1], self.points[i], (0, 255, 0), self.snake_thickness)

        # Draw Food
        fx, fy = self.food
        cv2.circle(frame, (fx, fy), self.food_radius, (0, 0, 255), cv2.FILLED)

        # Check for collision with food
        if abs(cx - fx) < self.food_radius + self.snake_thickness and abs(cy - fy) < self.food_radius + self.snake_thickness:
            self.play_eat_sound()
            self.food = self.random_food()
            self.allowed_length += self.speed_increment
            self.score += 1

        # Check collision with self
        if len(self.points) >= 10:
            pts = self.points[:-10]
            for pt in pts:
                if abs(cx - pt[0]) < self.snake_thickness and abs(cy - pt[1]) < self.snake_thickness:
                    self.game_over = True
                    break

        # Display score
        cv2.putText(frame, f"Score: {self.score}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 255), 2)
        return frame
