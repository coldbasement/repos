
# Winter Wonderland

from graphics import *
import math



#1st Circle


def main():
 win = GraphWin("Winder Wonderland", 320, 240)

 #Snow man
 circle1 = Circle(Point(100,100),20)
 circle1.setFill("white")
 circle1.setOutline("black")
 circle1.draw(win)
 circle2 = circle1.clone()
 circle2.move(0,38)
 circle2.draw(win)
 circle3 =circle1.clone()
 circle3.move(0,-38)
 circle3.draw(win)

 #Head
 eye1 = Circle(Point(95,50),2)
 eye1.setFill("black")
 eye1.draw(win)
 eye2 = eye1.clone()
 eye2.move(10,0)
 eye2.draw(win)
 nose = eye1.clone()
 nose.move(5,5)
 nose.draw(win)

 #Mouth
 mouth = nose.clone()
 mouth.move(0,10)
 mouth.draw(win)
 mouth1 = mouth.clone()
 mouth1.move(5,0)
 mouth1.draw(win)
 mouth2 = mouth1.clone()
 mouth2.move(5,0)
 mouth2.draw(win)
 mouth3 = mouth.clone()
 mouth3.move(-5,0)
 mouth3.draw(win)
 mouth4 = mouth3.clone()
 mouth4.move(-5,0)
 mouth4.draw(win)


 
 #Coal Body
 circle4 = Circle(Point(100,100),3)
 circle4.setFill("black")
 circle4.draw(win)
 circle5 = circle4.clone()
 circle5.move(0,10)
 circle5.draw(win)
 circle6 = circle4.clone()
 circle6.move(0,-10)
 circle6.draw(win)

 #Arms
 armcheck = Point(80,100).draw(win)
 arm1 = Point(50,80).draw(win)
 rightArm = Line(armcheck,arm1)
 rightArm.setOutline("brown")
 rightArm.draw(win)

 
 arm2 = Point(120, 100).draw(win)
 arm3 = Point(150, 120).draw(win)
 leftArm = Line(arm2,arm3)
 leftArm.setOutline("brown")
 leftArm.draw(win)



#Tree
 base = Rectangle(Point(200,150), Point(240, 200))
 base.setFill("brown")
 base.draw(win)

 test = Point(160,150).draw(win)
 test1 = Point(280,150).draw(win)
 test2 = Point(220,100).draw(win)
 triangle = Polygon(test,test1,test2)
 triangle.setFill("green")
 triangle.draw(win)
 triangle2 =triangle.clone()
 triangle2.move(0,-20)
 triangle2.draw(win)
 trangle3 = triangle2.clone()
 trangle3.move(0,-20)
 trangle3.draw(win)
 triangle4 = trangle3.clone()
 triangle4.move(0,-20)
 triangle4.draw(win)




 


main()
