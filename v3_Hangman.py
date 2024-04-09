import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        # Initialize the HangmanGame class
        self.root = root
        self.root.title("Hangman Game")
        
        # List of words for the game
        self.word_list = ["apple", "banana", "orange", "grape", "pineapple", 
    "strawberry", "watermelon", "kiwi", "pear", "peach", 
    "apricot", "plum", "blueberry", "raspberry", "blackberry", 
    "cherry", "lemon", "lime", "coconut", "melon", 
    "mango", "pomegranate", "fig", "nectarine", "cantaloupe", 
    "avocado", "guava", "papaya", "dragonfruit", "passionfruit", 
    "lychee", "jackfruit", "durian", "breadfruit", "persimmon", 
    "quince", "cranberry", "tangerine", "kumquat", "boysenberry", 
    "elderberry", "gooseberry", "honeydew", "mulberry", "rhubarb", 
    "tamarind", "acai", "plantain", "carambola",
    "cat", "dog", "horse", "elephant", "giraffe",
    "lion", "tiger", "zebra", "cheetah", "bear",
    "wolf", "fox", "rabbit", "deer", "squirrel",
    "bird", "eagle", "hawk", "owl", "parrot",
    "penguin", "seagull", "robin", "sparrow", "swan",
    "peacock", "dolphin", "whale", "shark", "octopus",
    "starfish", "jellyfish", "crab", "lobster", "snail",
    "butterfly", "dragonfly", "ladybug", "grasshopper", "beetle",
    "ant", "spider", "scorpion", "centipede", "millipede",
    "snake", "lizard", "turtle", "frog", "toad"]
        
        # Select a random word from the word list
        self.secret_word = random.choice(self.word_list)
        
        # Initialize guessed letters, failed attempts, and attempts left
        self.guessed_letters = set()
        self.failed_attempts = ""
        self.attempts = 6
        
        # Create and pack widgets for displaying word, input field, buttons, and labels
        self.word_display = tk.Label(root, text=self.hide_word(), font=('Arial', 24))
        self.word_display.pack()
        
        self.guess_label = tk.Label(root, text="Enter a letter:", font=('Arial', 16))
        self.guess_label.pack()
        
        self.guess_entry = tk.Entry(root, font=('Arial', 16))
        self.guess_entry.pack()
        
        # Bind <Return> event to the entry field for guessing the word
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())
        
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess, font=('Arial', 16))
        self.guess_button.pack()
        
        self.attempts_label = tk.Label(root, text="Attempts left: {}".format(self.attempts), font=('Arial', 16))
        self.attempts_label.pack()
        
        self.failed_attempts_label = tk.Label(root, text="Failed attempts: {}".format(self.failed_attempts), font=('Arial', 16))
        self.failed_attempts_label.pack()
        
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, font=('Arial', 16))
        self.restart_button.pack()
        
        # Create canvas widget
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        
        # Draw hangman figure
        self.draw_hangman(0)

    
    def hide_word(self):
        """Hide the secret word by replacing unguessed letters with underscores."""
        return ''.join([letter if letter in self.guessed_letters else '_ ' for letter in self.secret_word])
    
    def check_guess(self):
        """Check the user's guess."""
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
            return
        
        # Check if the letter has already been guessed
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You have already guessed this letter.")
            return
        
        # Add the guess to the guessed letters
        self.guessed_letters.add(guess)
        self.word_display.config(text=self.hide_word())
        
        # Check if the guess is correct
        if guess not in self.secret_word:
            # Decrement attempts if the guess is incorrect
            self.attempts -= 1
            self.failed_attempts += guess
            self.failed_attempts_label.config(text="Failed attempts: {}".format(self.failed_attempts))
            self.attempts_label.config(text="Attempts left: {}".format(self.attempts))
            # Draw hangman figure for the current stage
            self.draw_hangman(6 - self.attempts)
            # End the game if attempts run out
            if self.attempts == 0:
                if messagebox.askyesno("Game Over", "You ran out of attempts! The word was '{}'. Do you want to restart?".format(self.secret_word)):
                    self.restart_game()
                else:
                    self.root.destroy()
        else:
            # End the game if the word is correctly guessed
            if self.hide_word() == self.secret_word:
                messagebox.showinfo("Congratulations!", "You've guessed the word '{}' correctly!".format(self.secret_word))
                self.root.destroy()
    
    def draw_hangman(self, stage):
        self.canvas.delete("hangman")
        if stage == 0:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
        elif stage == 1:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
            self.canvas.create_oval(275, 150, 325, 200, width=5, tags="hangman", outline="#654321")
        elif stage == 2:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
            self.canvas.create_oval(275, 150, 325, 200, width=5, tags="hangman", outline="#654321")
            self.canvas.create_line(300, 200, 300, 300, width=5, tags="hangman", fill="#654321")
        elif stage == 3:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
            self.canvas.create_oval(275, 150, 325, 200, width=5, tags="hangman", outline="#654321")
            self.canvas.create_line(300, 200, 300, 300, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 250, 275, width=5, tags="hangman", fill="#654321")
        elif stage == 4:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
            self.canvas.create_oval(275, 150, 325, 200, width=5, tags="hangman", outline="#654321")
            self.canvas.create_line(300, 200, 300, 300, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 250, 275, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 350, 275, width=5, tags="hangman", fill="#654321")
        elif stage == 5:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
            self.canvas.create_oval(275, 150, 325, 200, width=5, tags="hangman", outline="#654321")
            self.canvas.create_line(300, 200, 300, 300, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 250, 275, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 350, 275, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 300, 250, 350, width=5, tags="hangman", fill="#654321")
        elif stage == 6:
            self.canvas.create_line(50, 350, 350, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 350, 200, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(200, 100, 300, 100, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 100, 300, 150, width=5, tags="hangman", fill="#654321")
            self.canvas.create_oval(275, 150, 325, 200, width=5, tags="hangman", outline="#654321")
            self.canvas.create_line(300, 200, 300, 300, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 250, 275, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 225, 350, 275, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 300, 250, 350, width=5, tags="hangman", fill="#654321")
            self.canvas.create_line(300, 300, 350, 350, width=5, tags="hangman", fill="#654321")

    
    def restart_game(self):
        """Restart the game with a new word."""
        # Select a new random word From List
        self.secret_word = random.choice(self.word_list)
        # Reset guessed letters, failed attempts, and attempts left
        self.guessed_letters = set()
        self.failed_attempts = ""
        self.attempts = 6
        # Update widgets
        self.word_display.config(text=self.hide_word())
        self.attempts_label.config(text="Attempts left: {}".format(self.attempts))
        self.failed_attempts_label.config(text="Failed attempts: {}".format(self.failed_attempts))
        # Clear canvas
        self.canvas.delete("hangman")
        # Draw initial hangman figure
        self.draw_hangman(0)

def main():
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
