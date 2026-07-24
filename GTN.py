import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumber:
    def __init__(self, root):
        self.root = root
        self.root_entry = tk.Entry(self.root, font=("Courier New", 18, "bold"), fg="#cbd5e1", bg="#16222f", justify="center")
        self.root_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, fg="#cbd5e1", bg="#3b4856", activebackground="#506175", relief="raised")
        self.guess_button.pack(pady=10)

        self._add_giveup_button()

    def check_guess(self):
        try:
            guess = int(self.root_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")
            return

        if guess == self.root.number:
            messagebox.showinfo("Result", "Congratulations! You guessed the correct number.")
        elif guess < self.root.number:
            messagebox.showinfo("Hint", "The number is higher than your guess.")
        else:
            messagebox.showinfo("Hint", "The number is lower than your guess.")

    def give_up(self):
        messagebox.showinfo("Game Over", f"The correct number was: {self.root.number}")
        self.root_entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        self.giveup_button.config(state='disabled')

    def _add_giveup_button(self):
        self.giveup_button = tk.Button(self.root, text="Give Up", command=self.give_up)
        self.giveup_button.pack(pady=5)

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("300x400")
    window.resizable(False, False)
    window.number = random.randint(1, 9999999)
    window.title("Guess the number")
    app = GuessTheNumber(window)
    window.mainloop()
        
        