import cv2
import numpy as np
import pytesseract
import pyautogui
import time
import tkinter as tk
from PIL import Image, ImageTk

# Hi-Lo värden
card_values = {
    '2': 1, '3': 1, '4': 1, '5': 1, '6': 1,
    '7': 0, '8': 0, '9': 0,
    '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1
}

running_count = 0
cards_seen = 0
num_decks = 6

# Konfigurera Tesseract om det behövs
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_cards(image):
    global running_count, cards_seen
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config='--psm 6')
    detected = []

    for word in text.split():
        word = word.upper().strip()
        if word in card_values:
            running_count += card_values[word]
            cards_seen += 1
            detected.append(word)

    return detected

def update_overlay(label):
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    detected_cards = detect_cards(frame)

    decks_remaining = max(num_decks - (cards_seen / 52), 1)
    true_count = round(running_count / decks_remaining, 2)

    info = f"Detected: {', '.join(detected_cards)}\nRunning Count: {running_count}\nTrue Count: {true_count}"
    label.config(text=info)
    label.after(2000, lambda: update_overlay(label))

# GUI-overlay
def start_overlay():
    root = tk.Tk()
    root.title("Blackjack Card Counter")
    root.geometry("300x150+100+100")
    root.attributes("-topmost", True)

    label = tk.Label(root, text="Initializing...", justify="left", font=("Consolas", 12))
    label.pack(padx=10, pady=10)

    update_overlay(label)
    root.mainloop()

if __name__ == "__main__":
    start_overlay()
