
import tkinter as tk
import random

WORDS = ["python", "hangman", "coding", "random", "project"]
MAX_ATTEMPTS = 6

# -------------------------------
# Game Functions
# -------------------------------
def start_new_game():
    global secret_word, guessed_letters, incorrect_guesses
    secret_word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    status_label.config(text="", fg="#2c3e50")
    attempts_label.config(text=f"Attempts Left: {MAX_ATTEMPTS}")
    update_word_display()
    reset_canvas()

    for btn in letter_buttons:
        btn.config(state="normal", bg="#3498db")

def update_word_display():
    display = ""
    for letter in secret_word:
        display += letter + " " if letter in guessed_letters else "_ "
    word_label.config(text=display)

def guess_letter(letter):
    global incorrect_guesses

    if letter in guessed_letters:
        status_label.config(text="Letter already guessed!", fg="orange")
        return

    guessed_letters.append(letter)

    if letter not in secret_word:
        incorrect_guesses += 1
        draw_hangman(incorrect_guesses)
        attempts_label.config(
            text=f"Attempts Left: {MAX_ATTEMPTS - incorrect_guesses}"
        )

    update_word_display()
    check_game_status()

def check_game_status():
    if all(letter in guessed_letters for letter in secret_word):
        status_label.config(text="🎉 You Won!", fg="green")
        disable_buttons()
    elif incorrect_guesses >= MAX_ATTEMPTS:
        status_label.config(
            text=f"💀 Game Over! Word: {secret_word}", fg="red"
        )
        disable_buttons()

def disable_buttons():
    for btn in letter_buttons:
        btn.config(state="disabled", bg="#95a5a6")

# -------------------------------
# Hangman Drawing
# -------------------------------
def reset_canvas():
    canvas.delete("all")
    canvas.create_line(40, 180, 160, 180, width=3)
    canvas.create_line(100, 180, 100, 30, width=3)
    canvas.create_line(100, 30, 170, 30, width=3)
    canvas.create_line(170, 30, 170, 50, width=3)

def draw_hangman(step):
    if step == 1:
        canvas.create_oval(150, 50, 190, 90, width=3)
    elif step == 2:
        canvas.create_line(170, 90, 170, 130, width=3)
    elif step == 3:
        canvas.create_line(170, 100, 150, 120, width=3)
    elif step == 4:
        canvas.create_line(170, 100, 190, 120, width=3)
    elif step == 5:
        canvas.create_line(170, 130, 150, 160, width=3)
    elif step == 6:
        canvas.create_line(170, 130, 190, 160, width=3)

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Hangman Game")
root.geometry("520x620")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

title_label = tk.Label(
    root, text="🎮 Hangman Game",
    font=("Helvetica", 22, "bold"),
    bg="#ecf0f1", fg="#2c3e50"
)
title_label.pack(pady=10)

canvas = tk.Canvas(root, width=240, height=200, bg="white")
canvas.pack(pady=10)

word_label = tk.Label(
    root, font=("Courier", 20, "bold"),
    bg="#ecf0f1", fg="#34495e"
)
word_label.pack(pady=10)

attempts_label = tk.Label(
    root, font=("Arial", 12),
    bg="#ecf0f1", fg="#2c3e50"
)
attempts_label.pack()

status_label = tk.Label(
    root, font=("Arial", 12, "bold"),
    bg="#ecf0f1"
)
status_label.pack(pady=5)

buttons_frame = tk.Frame(root, bg="#ecf0f1")
buttons_frame.pack(pady=10)

letter_buttons = []
for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    btn = tk.Button(
        buttons_frame,
        text=letter.upper(),
        width=4,
        font=("Arial", 10, "bold"),
        bg="#3498db",
        fg="white",
        command=lambda l=letter: guess_letter(l)
    )
    btn.grid(row=i // 7, column=i % 7, padx=4, pady=4)
    letter_buttons.append(btn)

restart_btn = tk.Button(
    root, text="🔄 Restart Game",
    font=("Arial", 12, "bold"),
    bg="#2ecc71", fg="white",
    command=start_new_game
)
restart_btn.pack(pady=10)

start_new_game()
root.mainloop()
