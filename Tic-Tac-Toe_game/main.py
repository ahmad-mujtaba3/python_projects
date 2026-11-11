
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("420x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#151925")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        # Title
        title = tk.Label(
            root,
            text="TIC-TAC-TOE",
            font=("Arial", 25, "bold"),
            bg="#151925",
            fg="white"
        )
        title.pack(pady=15)

        # Turn indicator
        self.status = tk.Label(
            root,
            text="Player X's Turn",
            font=("Arial", 16),
            bg="#151925",
            fg="#aab8ff"
        )
        self.status.pack(pady=10)

        # Game board
        board_frame = tk.Frame(root, bg="#151925")
        board_frame.pack(pady=10)

        for i in range(9):
            button = tk.Button(
                board_frame,
                text="",
                font=("Arial", 30, "bold"),
                width=3,
                height=1,
                bg="#252d40",
                fg="white",
                activebackground="#35415a",
                activeforeground="white",
                relief="flat",
                cursor="hand2",
                command=lambda index=i: self.make_move(index)
            )

            button.grid(
                row=i // 3,
                column=i % 3,
                padx=5,
                pady=5
            )

            self.buttons.append(button)

        # Restart button
        restart_button = tk.Button(
            root,
            text="RESTART GAME",
            font=("Arial", 13, "bold"),
            bg="#526cf5",
            fg="white",
            activebackground="#7186ff",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.restart_game
        )

        restart_button.pack(pady=20, ipadx=20, ipady=10)

    # Make a move
    def make_move(self, index):
        if self.board[index] != "":
            return

        self.board[index] = self.current_player

        color = (
            "#526cf5"
            if self.current_player == "X"
            else "#ff647c"
        )

        self.buttons[index].config(
            text=self.current_player,
            fg=color,
            disabledforeground=color,
            state="disabled"
        )

        # Check winner
        if self.check_winner():
            self.status.config(
                text=f"Player {self.current_player} Wins!",
                fg="#55df9b"
            )

            self.end_game()

            messagebox.showinfo(
                "Game Over",
                f"Player {self.current_player} Wins!"
            )
            return

        # Check draw
        if "" not in self.board:
            self.status.config(
                text="It's a Draw!",
                fg="#ffc857"
            )

            self.end_game()

            messagebox.showinfo(
                "Game Over",
                "It's a Draw!"
            )
            return

        # Switch player
        self.current_player = (
            "O" if self.current_player == "X" else "X"
        )

        self.status.config(
            text=f"Player {self.current_player}'s Turn"
        )

    # Check winning combinations
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (
                self.board[a] == self.board[b] ==
                self.board[c] != ""
            ):
                return True

        return False

    # Disable buttons after game ends
    def end_game(self):
        for button in self.buttons:
            button.config(state="disabled")

    # Restart game
    def restart_game(self):
        self.current_player = "X"
        self.board = [""] * 9

        for button in self.buttons:
            button.config(
                text="",
                state="normal",
                fg="white"
            )

        self.status.config(
            text="Player X's Turn",
            fg="#aab8ff"
        )


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
