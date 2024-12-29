import pyautogui
import time
import os
import tkinter as tk
from tkinter import messagebox

# Function to perform spamming
def start_spamming():
    word = entry_word.get()
    count = entry_count.get()
    
    if not word or not count.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid word and a number.")
        return
    
    count = int(count)
    time.sleep(4)  # Optional: Delay before starting
    for i in range(count):
        pyautogui.typewrite(word)

# Create the main window
root = tk.Tk()
root.title("Dark Spammer")
root.geometry("300x200")

# Create and place labels and entry fields
label_word = tk.Label(root, text="Enter a word to spam:")
label_word.pack(pady=5)

entry_word = tk.Entry(root)
entry_word.pack(pady=5)

label_count = tk.Label(root, text="Specify how many times to spam:")
label_count.pack(pady=5)

entry_count = tk.Entry(root)
entry_count.pack(pady=5)

# Create and place the spam button
spam_button = tk.Button(root, text="Start Spamming", command=start_spamming)
spam_button.pack(pady=20)

# Run the application
root.mainloop()