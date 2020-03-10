from tkinter import *

import random
lastMove=7

# MOVES
U=["U","U2","U'"]
R=["R","R2","R'"]
F=["F","F2","F'"]
B=["B","B2","B'"]
L=["L","L2","L'"]
D=["D","D2","D'"]

move_list=[]

for i in range(0,25):
    move=random.randint(1,6)
    if move==lastMove:
        move=move+1
    lastMove=move
    moveType=random.randint(0,2)
    if move == 1:
        t=U[moveType]
        str(t)
        #print(t)
        move_list.append(t)
    elif move == 2:
        t=R[moveType]
        str(t)
        #print(t)
        move_list.append(t)
    elif move == 3:
        t=F[moveType]
        str(t)
        #print(t)
        move_list.append(t)
    elif move == 4:
        t=B[moveType]
        str(t)
        #print(t)
        move_list.append(t)
    elif move == 5:
        t=L[moveType]
        str(t)
        #print(t)
        move_list.append(t)
    elif move == 6:
        t=D[moveType]
        str(t)
        #print(t)
        move_list.append(t)

window=Tk()

window.title('NPTimer')

c=Canvas(window, height=800, width=1000)
c.create_rectangle(0, 0, 1010, 250, fill='yellow') # Box for scramble
c.create_text(500, 100, font= ('ariel',25), text=move_list )
c.grid()
