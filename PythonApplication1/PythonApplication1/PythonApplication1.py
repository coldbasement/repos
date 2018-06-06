
from graphics import *

def main():
 win = GraphWin("A program that Draws two Circles")
 win.setCoords(0,-100,200,100)

circle2 = Circle(Point(5,0),5)
circle2.setFill("blue")
circle2.setOutline("black")
circle2.draw(win)


main()