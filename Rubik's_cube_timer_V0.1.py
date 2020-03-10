from tkinter import *

window=Tk()

window.title('NPTimer')

c=Canvas(window, height=800, width=1000)
c.create_rectangle(0, 0, 1010, 250, fill='yellow') # Box for scramble
c.create_text(500, 100, font= ('ariel',25), text="D R' B U R2 D R B D' L2 F' D2 F' U2 L2 B R2 F D2 R2" )
c.grid()
