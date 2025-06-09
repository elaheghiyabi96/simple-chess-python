#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install python-chess cairosvg


# In[2]:


import tkinter as tk  # GUI library
import chess  # Python-Chess library for handling game logic

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")  # Set the window title
        self.board = chess.Board()  # Create a new chess board
        self.selected_square = None  # Keep track of selected square
        self.buttons = {}  # Dictionary to store button widgets

        self.create_board()  # Initialize board GUI

    def create_board(self):
        # Create 8x8 grid of buttons for the chessboard
        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)  # Convert GUI coordinates to board square
                btn = tk.Button(
                    self.root,
                    width=6,
                    height=3,
                    command=lambda s=square: self.on_click(s),  # Set click handler
                    font=("Arial", 16)
                )
                btn.grid(row=row, column=col)  # Place button on grid
                self.buttons[square] = btn  # Store button reference

        self.update_board()  # Update button labels/colors

    def update_board(self):
        # Update all buttons based on current board state
        for square, btn in self.buttons.items():
            piece = self.board.piece_at(square)  # Get piece on this square

            if piece:
                symbol = piece.symbol()  # Get symbol (e.g., 'P', 'k')
                btn.config(text=symbol)

                # Set font color based on piece color
                if piece.color:  # White piece
                    btn.config(fg="black")
                else:  # Black piece
                    btn.config(fg="white")
            else:
                btn.config(text="", fg="black")  # Empty square

            # Set background color (light/dark) for chessboard pattern
            col, row = chess.square_file(square), chess.square_rank(square)
            color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"
            btn.config(bg=color)

    def on_click(self, square):
        # Handle piece selection and movement
        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square  # Select piece if it's this player's turn
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)  # Make the move
                self.selected_square = None
                self.update_board()  # Refresh board display

                # Check if the game is over
                if self.board.is_game_over():
                    result = "Game over: " + self.board.result()
                    self.show_end(result)
            else:
                self.selected_square = None  # Deselect if move is illegal

    def show_end(self, message):
        # Display game over message in a popup window
        top = tk.Toplevel(self.root)
        tk.Label(top, text=message, font=("Arial", 18)).pack(padx=20, pady=20)
        tk.Button(top, text="Exit", command=self.root.quit).pack(pady=10)

# Create the application window and run the game
root = tk.Tk()
app = ChessGUI(root)
root.mainloop()


# In[ ]:




