from graphics import *
#Open a graphics Window
win = GraphWin('Shapes')
#Draw a red Circle centered at point (100,100) with radius 30
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
#Put a Textual lable in the center of the cirlce
label = Text(center, "Red Circle")
label.draw(win)
##Draw a square using a Rectangle object
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)
#Draw a line segment using a Line Object
line = Line(Point(20,30), Point(180, 199))
line.draw(win)
##Draw an oval using the Oval object
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)

