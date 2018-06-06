#Project2GemotricShapes.py
#CS 1400
#By Kody Carling
# This program uses the graphics library's objects to draw Geomitric Shapes
# I think the hardest part is figuring out how to draw and where it shows up on the Screen. 
# I did not  have help on this. I did this all on my own. I had a ton of fun with it, Very Interesting!

from graphics import *

def main():
    win = GraphWin("5 Platonic Solids", 1500, 1000)
    
    ###### Tetrahadron ###### 
    #Test the Points According to Picture found on 
    test1 = Point(200,100).draw(win)
    test2 = Point(200,200).draw(win)
    test3 = Point(100,90).draw(win)
    test4 = Point(300,70).draw(win)

    #draw the Triangles based on the test points
    triangle1 = Polygon(test1,test2,test3)
    triangle1.draw(win)
    triangle1.setFill("red")
    triangle2 = Polygon(test1,test2,test4)
    triangle2.draw(win)
    triangle2.setFill("blue")
    traingle3 = Polygon(test1,test3,test4)
    traingle3.draw(win)
    traingle3.setFill("yellow")

    ###### Cube #########
    #Going to use Lines 
    cube1 = Point(600, 50).draw(win)
    cube1.setFill("red")
    cube2 = Point(600, 150).draw(win)
    cube2.setFill("green")
    cube3 = Point(500, 100).draw(win)
    cube3.setFill("blue")
    cube4 = Point(700,100).draw(win)
    cube4.setFill("yellow")
    cube5 = Point(600, 260).draw(win)
    cube6 = Point(500, 200).draw(win)
    cube7 = Point(700, 200).draw(win)
    
    #Draw Lines based on Test Points
    cube_line1= Line(cube1,cube3).draw(win)
    cube_line1.setFill("red")
    cube_line2= Line(cube1,cube4).draw(win)
    cube_line2.setFill("blue")
    cube_line3= Line(cube4,cube2).draw(win)
    cube_line3.setFill("green")
    cube_line4= Line(cube2,cube3).draw(win)
    cube_line4.setFill("purple")
    cube_line5 = Line(cube2, cube5).draw(win)
    cube_line6 = Line(cube4, cube7).draw(win)
    cube_line7 = Line(cube5, cube7).draw(win)
    cube_line8 = Line(cube3, cube6).draw(win)
    cube_line9 = Line(cube6, cube5).draw(win)

    ###############Octahedron############
    #Test Points
    oct1 = Point(1000,10).draw(win)
    oct2 = Point(990,110).draw(win)
    oct3 = Point(920,180).draw(win)
    oct4 = Point(880,60).draw(win)
    oct5 = Point(1060,130).draw(win)
    #Draw Triangles
    oct_triangle1 = Polygon(oct1,oct4,oct2)
    oct_triangle1.draw(win)
    oct_triangle1.setOutline("black")
    oct_triangle1.setFill("green")
    oct_triangle2 = Polygon(oct2,oct4, oct3)
    oct_triangle2.draw(win)
    oct_triangle2.setOutline("black")
    oct_triangle2.setFill("green")
    oct_triangle3 = Polygon(oct1,oct2,oct5)
    oct_triangle3.draw(win)
    oct_triangle3.setOutline("black")
    oct_triangle3.setFill("green")
    oct_triangle4 = Polygon(oct2, oct5, oct3)
    oct_triangle4.draw(win)
    oct_triangle4.setOutline("black")
    oct_triangle4.setFill("green")


#### dodcahedron 
    #Front view
    dot1 = Point(400,500).draw(win)
    dot2 = Point(330, 550).draw(win) 
    dot3 = Point(470, 550).draw(win)
    dot4 = Point(445, 630).draw(win)
    dot5 = Point(355,630).draw(win)
    dot_line1 = Line(dot1,dot2).draw(win)
    dot_line1.setFill("Red")
    dot_line2 = Line(dot1,dot3).draw(win) 
    dot_line2.setFill("Blue")
    dot_line3 = Line(dot4, dot5).draw(win)
    dot_line3.setFill("Green")
    dot_line4 = Line(dot2, dot5).draw(win)
    dot_line4.setFill("Black")
    dot_line5 = Line(dot3, dot4).draw(win) 
    dot_line5.setFill("Purple")
   # Top view
    #top right
    dot6 = Point(405,450).draw(win)
    dot7 = Point(475,465).draw(win)
    dot8 = Point(515,520).draw(win)
    dot_line7= Line(dot1,dot6).draw(win)
    dot_line8 = Line(dot6, dot7).draw(win)
    dot_line9 = Line(dot7,dot8).draw(win)
    dot_line10 = Line(dot3,dot8).draw(win)
    #topleft
    dot9 = Point(350,470).draw(win)
    dot10 = Point(310,510).draw(win)
    dot_line11= Line(dot6,dot9).draw(win)
    dot_line12 = Line(dot9, dot10).draw(win)
    dot_line13= Line(dot10,dot2).draw(win)

   #Bottom right
    dot11 =Point(530,570).draw(win)
    dot12 = Point(510,640).draw(win)
    dot_line12 = Line(dot11, dot8).draw(win)
    dot_line13 = Line(dot11, dot12).draw(win)
    dot_line14 = Line(dot12, dot4).draw(win)    

   #Bottom Left 
    dot13 = Point(290,590).draw(win)
    dot14 = Point(330,650).draw(win)
    dot_line15 = Line(dot13, dot10).draw(win)
    dot_line16 = Line(dot13,dot14).draw(win)
    dot_line17 = Line(dot5,dot14).draw(win)

    #Bottom
    dot15 = Point(445, 660).draw(win)
    dot_line18 = Line(dot15, dot14).draw(win)
    dot_line19 = Line(dot15, dot12).draw(win)

    ####Iscosahedron####  

    #Red Triangle
    is_test1 = Point(900, 470).draw(win)
    is_test2 = Point(800, 600).draw(win)
    is_test3 = Point(1000, 600).draw(win)

    is_triangle_1 =Polygon(is_test1, is_test2, is_test3)
    is_triangle_1.setFill("red")
    is_triangle_1.setOutline("black")
    is_triangle_1.draw(win)
 
    #Blue Trangle
    is_test4 = Point(900,730).draw(win)
    blueTri = Polygon(is_test2,is_test3,is_test4).draw(win)
    blueTri.setFill("blue")
    blueTri.setOutline("black")

    is_test5 = Point(770, 580).draw(win)
    is_test6 = Point(1030, 580).draw(win)

    #TopLeftSide
    sidetri = Polygon(is_test5,is_test2, is_test1).draw(win)
    sidetri.setFill("yellow")
    sidetri.setOutline("black")

    #TopRightSide
    sidetri2 = Polygon(is_test6, is_test1, is_test3).draw(win)
    sidetri2.setFill("yellow")
    sidetri2.setOutline("black")
    

    #BottomRight
    is_test7 = Point(770,730).draw(win)
    bottomtri = Polygon(is_test7,is_test4,is_test2).draw(win)
    bottomtri.setFill("green")
    bottomtri.setOutline("black")

    #BottomLeft
    is_test8 = Point(1030,730).draw(win)
    bottomtri2 = Polygon(is_test8, is_test4,is_test3).draw(win)
    bottomtri2.setFill("green")
    bottomtri2.setOutline("black")

    smallbottomtri2= Polygon(is_test7, is_test2, is_test5).draw(win)
    smallbottomtri2.setFill("purple")
    smallbottomtri= Polygon(is_test3, is_test6, is_test8).draw(win)
    smallbottomtri.setFill("purple")





main()