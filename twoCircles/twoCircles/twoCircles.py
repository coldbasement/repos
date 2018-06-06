#A program to draw two circles

from graphics import *
import math

#Introduction 
print("This Program will Draw 2 circles")
print("The User must enter the Center Points(1 = x axix, 2 = y axis) and the Radius")

#1st Circle
print("Circle 1 Red")
cir1_pointx = int(input("Enter center point 1(x axis): "))
cir1_pointy = int(input("Enter center point 2(y axis): "))
cir1_radius = int(input("Enter the radius for Circle 1(1-20): "))
areacir1= round(math.pi *math.pow(cir1_radius,2),2)
print("The area of the Red circle is", areacir1)
print("Circle 2 Blue")
cir2_pointx = int(input("Enter center point 1(x axis): "))
cir2_pointy = int(input("Enter center point 2(y axis): "))
cir2_radius = int(input("Enter the radius for Circle 2(1-20): "))
areacir2 = round(math.pi *math.pow(cir2_radius,2),2)
print("the area of the blue circle is", areacir2)

def main():
 win = GraphWin("A program that Draws two Circles", 320, 240)

 circle1 = Circle(Point(cir1_pointx,cir1_pointy), cir1_radius)
 circle1.setFill("red")
 circle1.setOutline("black")
 circle1.draw(win)

 circle2 = Circle(Point(cir2_pointx,cir2_pointy),cir2_radius)
 circle2.setFill("blue")
 circle2.setOutline("black")
 circle2.draw(win)
''' 
 if cir1_pointx - cir2_pointx < 20 or cir2_pointx - cir1_pointx < 20:
  Text(Point(150,220), "The circles overlap").draw(win)
 elif cir1_pointy - cir2_pointy < 20 or cir2_pointy - cir1_pointy < 20:
  Text(Point(150,220), "The circles overlap").draw(win)
 else:
  Text(Point(150,220), "The circles Do not overlap").draw(win)

if 
 Text(Point(150,220), "The circles do not overlap").draw(win)
'''


main()





