from graphics import * 
def main():
 win = GraphWin("A program that Draws two Circles", 320, 240)

 '''
 circle1 = Circle(Point(cir1_pointx,cir1_pointy), cir1_radius)
 circle1.setFill("red")
 circle1.setOutline("black")
 circle1.draw(win)

 circle2 = Circle(Point(cir2_pointx,cir2_pointy),cir2_radius)
 circle2.setFill("blue")
 circle2.setOutline("black")
 circle2.draw(win)
 '''
 Text(Point(150,220), "The circles overlap").draw(win)

main()