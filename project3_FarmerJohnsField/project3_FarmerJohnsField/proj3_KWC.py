#proj3_KWC.py
# by Kody Carling
# Project Title = Farmer John's Field
# Course = CS1400 Section 
# Due Date = 2/25/2018
# I decided to display information in the Console as well as in the Graphics box to the User
# I did not know how to shade the diamond area in the box, so I focused on the other shapes to add color. If there was a way, I would love to learn how
# I also learned that The shapes stack on each other. I had the square displayed before the circles. When I filled the circles, my square went away.
# I had to color the square lines, after the circles were drawn and filled. 




import math
from graphics import *

def circle_area(rad):
    ca = round(math.pi * math.pow(rad,2),2)
    return ca
def field_area(side):
    fa = round(math.pow(side,2),2)
    return fa


def main():
  
    side = int(input("Please Enter the length of one side of the square field  : "))
    rad = side * .5
    message = print("The length of each side of the Square filed is", side, "feet")
    message2 = print("The area of each cirular field is", circle_area(rad),"ft^2")
    message3 = print("The area of the square field is", field_area(side), "ft^2")
    CircleArea = circle_area(rad)
    FieldArea = field_area(side)
    #By the look of the drawing it should be 1 box area - 1 cicle fields area(THE Box gets 1/4 of each circle
    Total_Area = round(FieldArea - CircleArea,2)
    message4 = print("The area in question is", Total_Area, "ft^2")
   
    win = GraphWin("Farmers Johns Fields", 500, 300)


 # Drawing the Square Field
    p1 = Point(200, 100).draw(win)
    p2 = Point(250, 100).draw(win)
    p3 = Point(200, 150).draw(win)
    p4 = Point(250, 150).draw(win)
    p5 = Point(220, 50)
    p6 = Point(250,200)
    p7 = Point(240,250)

# Drawing the Circles
    radius = 25
    circle1 = Circle(p1, radius).draw(win)
    circle1.setFill("yellow")
    circle2 = Circle(p2, radius).draw(win)
    circle2.setFill("yellow")
    circle3 = Circle(p3, radius).draw(win)
    circle3.setFill("yellow")
    circle4 = Circle(p4, radius).draw(win)
    circle4.setFill("yellow")

# Drawing the Square Field
    line1 = Line(p1,p2).draw(win)
    line1.setOutline("red")
    line2 = Line(p3,p4).draw(win)
    line2.setOutline("red")
    line3 = Line(p1,p3).draw(win) 
    line3.setOutline("red")
    line4 = Line(p2,p4).draw(win)
    line4.setOutline("red")

# Drawing Labels
    text1 = Text(p1, "A").draw(win)
    text2 = Text(p2, "B").draw(win)
    text3 = Text(p3, "C").draw(win)
    text4 = Text(p4, "D").draw(win)
    message5 = Text(p5, "Farmer Johns Field")
    message5.draw(win)
    message6 = Text(p6, "The area of the white shade inside the square field is(ft^2): ").draw(win)
    message7 = Text(p7,Total_Area).draw(win)
    message7.setTextColor("blue")
                    
main()

