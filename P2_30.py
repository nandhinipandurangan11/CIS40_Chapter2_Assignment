# CIS40 : Summer 2020: Chapter 2.30 Exercise: Nandhini Pandurangan
# This program uses ezgraphics to solve the problem

# P2.30: Write a program that displays the Olympic Rings. Color the rings in Olympic Colors

from ezgraphics import GraphicsWindow

# creating the window and the canvas
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# setting the thickness of the line
canvas.setLineWidth(4)

# creating blue circle
canvas.setOutline("blue")
canvas.drawOval(10,10,60,60)

# creating black circle
canvas.setOutline("black")
canvas.drawOval(73,10,60,60)

# creating red circle
canvas.setOutline("red")
canvas.drawOval(136,10,60,60)

# creating yellow circle
canvas.setOutline("yellow")
canvas.drawOval(43,40,60,60)

# creating green circle
canvas.setOutline("green")
canvas.drawOval(106,40,60,60)

# waiting for the user to close the window
win.wait()

''' 


'''