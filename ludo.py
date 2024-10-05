import tkinter as tk
import random
from PIL import Image, ImageTk  # Make sure you have Pillow installed

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ludo Game - Two Player")

        # Create a canvas to hold the background image
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Load and set the background image
        self.background_image = Image.open("C:/Users/preeti/Downloads/ludo.png")
        self.background_image = self.background_image.resize((600, 400), Image.LANCZOS)
        self.background_tk = ImageTk.PhotoImage(self.background_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_tk)

        # Load dice images
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"C:/Users/preeti/Downloads/dice.jpg").resize((50, 50), Image.LANCZOS))
            for i in range(1, 7)
        ]

        # Player positions
        self.player_positions = [0, 0]  # Player 1 and Player 2
        self.current_player = 0  # Player 1 starts

        # GUI elements
        self.info_label = tk.Label(root, text="Player 1's Turn!", font=("Helvetica", 14), bg='lightblue')
        self.info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.player1_label = tk.Label(root, text="Player 1 position: 0", bg='lightblue')
        self.player1_label.grid(row=2, column=0, padx=10, pady=10)

        self.player2_label = tk.Label(root, text="Player 2 position: 0", bg='lightblue')
        self.player2_label.grid(row=2, column=1, padx=10, pady=10)

        self.dice_label = tk.Label(root, text="Roll the dice!", font=("Helvetica", 12), bg='lightblue')
        self.dice_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Dice display
        self.dice_image_label = tk.Label(root, bg='lightblue')
        self.dice_image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.dice_label.config(text=f"Player {self.current_player + 1} rolled a {roll}!")

        # Display the rolled dice image
        self.dice_image_label.config(image=self.dice_images[roll - 1])  # Show corresponding dice image
        
        # If the player is at position 0, they need to roll a 6 to start
        if self.player_positions[self.current_player] == 0 and roll != 6:
            self.next_turn()
            return
        
        # Update the player position
        new_position = self.player_positions[self.current_player] + roll
        
        # Check if the player exceeds 100 (can't move beyond finish line)
        if new_position > 100:
            self.info_label.config(text=f"Player {self.current_player + 1} needs an exact roll to finish.")
        else:
            self.player_positions[self.current_player] = new_position
            
            # Check if the player has won
            if new_position == 100:
                self.info_label.config(text=f"Player {self.current_player + 1} Wins!")
                self.roll_button.config(state=tk.DISABLED)
                return

        # Update the GUI to show the player's new position
        self.update_player_positions()

        # Switch turns
        self.next_turn()

    def next_turn(self):
        # Switch to the other player
        self.current_player = 1 if self.current_player == 0 else 0
        self.info_label.config(text=f"Player {self.current_player + 1}'s Turn!")
        
    def update_player_positions(self):
        self.player1_label.config(text=f"Player 1 position: {self.player_positions[0]}")
        self.player2_label.config(text=f"Player 2 position: {self.player_positions[1]}")

    def reset_game(self):
        # Reset the game state
        self.player_positions = [0, 0]
        self.current_player = 0
        self.info_label.config(text="Player 1's Turn!")
        self.dice_label.config(text="Roll the dice!")
        self.dice_image_label.config(image='')  # Clear the dice image
        self.update_player_positions()
        self.roll_button.config(state=tk.NORMAL)

# Create the tkinter window
root = tk.Tk()
game = LudoGame(root)
root.mainloop()