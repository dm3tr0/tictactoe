from pygame import *
import numpy as np
from tkinter import messagebox
import tkinter as tk
from constants import *
import time as t

win = tk.Tk()
win.withdraw()

window = display.set_mode((600, 600))
display.set_caption('Tic Tac Toe')
display.set_icon(image.load('C:\Python\PyGame rofls\TicTacT\icon.png'))
messagebox.showinfo('Good luck!', '[R] - restart, [LMC] - play.')

def show_lines():
    window.fill(BGCOLOR)
    draw.line(window, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
    draw.line(window, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)
    draw.line(window, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
    draw.line(window, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

show_lines()

def show_figures():
    for row in range(BROWS):
        for col in range(BCOLONS):
            if board[row][col] == 1:
                draw.circle(window, (103, 214, 101), (int(col*200+200/2), int(row*200+200/2)), 60, 15)
            elif board[row][col] == 2:
                
                start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                draw.line(window, (230, 95, 88), start_desc, end_desc, CROSS_WIDTH)
            
                start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                draw.line(window, (230, 95, 88), start_asc, end_asc, CROSS_WIDTH)

board = np.zeros((BROWS, BCOLONS))

def mark(row, col, player):
    board[row][col] = player

def avaible(row, col):
    return board[row][col] == 0

def full():
    for row in range(BROWS):
        for col in range(BCOLONS):
            if board[row][col] == 0:
                return False
    return True

def win(player):
    for col in range(BCOLONS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_line(col, player)
            return True
    for row in range(BROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_line(row, player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diagonal_line_1(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diagonal_line_2(player)
        return True
        
    return False

def vertical_line(col, player):
    pos_x = col * 200 + 100
    if player == 1:
        color = (103, 214, 101)
    elif player == 2:
        color = (230, 95, 88)
    draw.line(window, color, (pos_x, 15), (pos_x, HEIGHT-15), 15)
    
def horizontal_line(col, player):
    pos_y = col * 200 + 100

    if player == 1:
        color = (103, 214, 101)
    elif player == 2:
        color = (230, 95, 88)

    draw.line(window, color, (15, pos_y), (WIDTH-15, pos_y), 15)
    
def diagonal_line_1(player):
    if player == 1:
        color = (103, 214, 101)
    elif player == 2:
        color = (230, 95, 88)

    draw.line(window, color, (15, HEIGHT-15), (WIDTH-15, 15), 15)

def diagonal_line_2(player):
    if player == 1:
        color = (103, 214, 101)
    elif player == 2:
        color = (230, 95, 88)

    draw.line(window, color, (15, 15), (WIDTH-15, HEIGHT-15), 15)

def restart():
    window.fill(BGCOLOR)
    show_lines()
    for row in range(BROWS):
        for col in range(BCOLONS):
            board[row][col] = 0
        
game = True
finish = False

player = 1

while game:
    keys = key.get_pressed()
    for events in event.get():
        if events.type == QUIT:
            game = False
        if events.type == MOUSEBUTTONDOWN and not finish:
            m_x = events.pos[0]
            m_y = events.pos[1]

            c_row = int(m_y // 200)
            c_col = int(m_x // 200)
            
            if avaible(c_row, c_col) == True:
                if player == 1:
                    mark(c_row, c_col, 1)
                    if win(player):
                        finish = True
                    player = 2
                elif player == 2:
                    mark(c_row, c_col, 2)
                    if win(player):
                        finish = True
                    player = 1
                show_figures()

        if keys[K_r]:
            restart()
            player = 1
            finish = False
            

    display.update()