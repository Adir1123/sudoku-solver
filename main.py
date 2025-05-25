import tkinter as tk
from GUI import SudokuGUI

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()