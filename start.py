from tkinter import *
from tkinter import messagebox
from ai_player import *
FONT = ("Verdana", 40, "bold")


def new_game():
    board = [["" for i in range(3)] for i in range(3)]
    return board


def game_over(status):
    if status == "X":
        messagebox.showinfo("Result", "You won.Play again.")
    elif status == "O":
        messagebox.showinfo("Result", "You lost!retry?")
    else:
        messagebox.showinfo("Result", "It's a draw!")


class Grid:
    lb_names = []

    def __init__(self, master):
        frame = Frame(master, height=400, width=400, bg='dark red')
        frame.grid()
        self.board = new_game()
        self.game_status = "continue"
        self.grid = []
        for i in range(3):
            row = []
            lb_name = []
            for j in range(3):
                cell = Frame(frame, height=125, width=125, bg="orange")
                lb = Label(cell, text='', justify=CENTER, height=2, width=4, font=FONT)
                row.append(lb)
                lb.pack()
                lb_name.append(lb)
                lb.bind("<Button-1>", self.user_turn)
                cell.grid(row=i, column=j, padx=4, pady=4)
            self.lb_names.append(lb_name)
            self.grid.append(row)
        self.game_turn = messagebox.askyesno("Who wants to start?", "Do you want to start first?")  # True for user turn
        if not self.game_turn:
            self.ai_turn()
        master.mainloop()

    def user_turn(self, event):
        for i in range(3):
            for j in range(3):
                if self.lb_names[i][j] == event.widget and self.board[i][j] == "" and self.game_turn:
                    self.board[i][j] = "X"
                    self.game_turn = False
                    self.update_grid()
                    self.ai_turn()
                    return

    def ai_turn(self):
        if not self.game_turn:
            move = determine_move(self.board, "O")
            if move[0] != -1:
                self.board[move[0]][move[1]] = "O"
            self.game_turn = True
            self.update_grid()

    def update_grid(self):
        for i in range(3):
            for j in range(3):
                self.grid[i][j].config(text=str(self.board[i][j]))

        self.game_status = get_game_status(self.board)
        print(self.game_status)
        if self.game_status != "continue":
            game_over(self.game_status)
            self.board = new_game()
            for i in range(3):
                for j in range(3):
                    self.grid[i][j].config(text=self.board[i][j])
            self.game_turn = messagebox.askyesno("Who wants to start?", "Do you want to start first?")
            if not self.game_turn:
                self.ai_turn()


root = Tk()
root.geometry("487x435+100+100")  # "width of window x height of window + position"
g = Grid(root)