#A program to draw two circles

from graphics import *
import math

#Introduction 


def main():
    win = GraphWin("A program that Draws two Circles")
    win.setCoords(0,-100,200,100)

    c1 = Circle(Point(0, 0), 5)
    c1.draw(win)
    c2 = Circle(Point(4, 5),2)
    c2.draw(win)
    c3 = c1
    c4 = c2


main()
