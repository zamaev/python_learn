import tkinter
import random
import time

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.bind('<Button-1>', self.click)
        self.restart()
        
    def restart(self):
        self.delete('all')
        self.draw_lines()
        self.state = [None, None, None, None, None, None, None, None, None]
        
    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(0, 100, 300, 100, fill='grey')
        self.create_line(0, 200, 300, 200, fill='grey')
        
    def add_x(self, column, row):
        self.create_line(column*100+20, row*100+20, column*100+80, row*100+80, width=5, fill='blue')
        self.create_line(column*100+20, row*100+80, column*100+80, row*100+20, width=5, fill='blue')
        self.update()
    
    def add_o(self, column, row):
        self.create_oval(column*100+20, row*100+20, column*100+80, row*100+80, width=5, outline='red')
        self.update()

    def click(self, event):
        column = event.x // 100
        row = event.y // 100
        pos = row * 3 + column
        if self.state[pos] is None:
            self.state[pos] = 'x'
            self.add_x(column, row)
            time.sleep(.3)
            if self.get_winner() == False:
                self.bot_move()
            if self.get_winner() == True:
                time.sleep(.5)
                self.restart()

    def bot_move(self):
        free_poss = []
        for i, s in enumerate(self.state):
            if s is None:
                free_poss.append(i)
        if len(free_poss) > 0:
            pos = random.choice(free_poss)
            self.state[pos] = 'o'
            column = pos % 3
            row = pos // 3
            self.add_o(column, row)
            
    def get_winner(self):
        st = self.state
        if st[0] and st[0] == st[1] == st[2]:
            color = 'red' if st[0] == 'o' else 'blue'
            self.create_line(20, 50, 280, 50, width=5, fill=color)
        elif st[3] and st[3] == st[4] == st[5]:
            color = 'red' if st[3] == 'o' else 'blue'
            self.create_line(20, 150, 280, 150, width=5, fill=color)
        elif st[6] and st[6] == st[7] == st[8]:
            color = 'red' if st[6] == 'o' else 'blue'
            self.create_line(20, 250, 280, 250, width=5, fill=color)
        elif st[0] and st[0] == st[3] == st[6]:
            color = 'red' if st[0] == 'o' else 'blue'
            self.create_line(50, 20, 50, 280, width=5, fill=color)
        elif st[1] and st[1] == st[4] == st[7]:
            color = 'red' if st[1] == 'o' else 'blue'
            self.create_line(150, 20, 150, 280, width=5, fill=color)
        elif st[2] and st[2] == st[5] == st[8]:
            color = 'red' if st[2] == 'o' else 'blue'
            self.create_line(250, 20, 250, 280, width=5, fill=color)
        elif st[0] and st[0] == st[4] == st[8]:
            color = 'red' if st[0] == 'o' else 'blue'
            self.create_line(20, 20, 280, 280, width=5, fill=color)
        elif st[2] and st[2] == st[4] == st[6]:
            color = 'red' if st[2] == 'o' else 'blue'
            self.create_line(20, 280, 280, 20, width=5, fill=color)
        elif None in st:
            return False
        self.update()
        return True 

window = tkinter.Tk()
game = TicTacToe(window)
game.pack()

window.mainloop()
