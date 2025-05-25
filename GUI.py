import tkinter as tk
from solver import Solver
from tkinter import messagebox


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center', borderwidth=2, relief='solid')
                top = 2 if row % 3 == 0 else 1
                left = 2 if col % 3 == 0 else 1
                bottom = 2 if row == 8 else 1
                right = 2 if col == 8 else 1
                entry.grid(row=row, column=col, padx=(left, right), pady=(top, bottom))
                self.entries[row][col] = entry

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", font=('Arial', 14), command=self.solve_sudoku)
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)

        clear_button = tk.Button(self.root, text="Clear", font=('Arial', 14), command=self.clear_board)
        clear_button.grid(row=10, column=3, columnspan=3, pady=5)

    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                val = self.entries[row][col].get()
                current_row.append(int(val) if val.isdigit() else 0)
            board.append(current_row)
        return board

    def update_board(self, board):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                if board[row][col] != 0:
                    self.entries[row][col].insert(0, str(board[row][col]))

    def solve_sudoku(self):
        board = self.get_board()
        solver = Solver(board)
        if solver.solve():
            self.update_board(solver.board)
        else:
            messagebox.showerror("Error", "No solution found for this Sudoku.")

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)