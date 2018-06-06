from graphics import *
#circ = Circle(Point(100,100), 30)
#win = GraphWin()
#circ.draw(win)

##Incorrect Way
'''
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
win = GraphWin()
leftEye.draw(win)
rightEye = leftEye
rightEye.move(20,0) 
'''

#Correct Way to draw 
'''
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
win = GraphWin()
leftEye.draw(win)
rightEye = leftEye.clone() #rightEye is an exact copy of the left
rightEye.move(20,0)
rightEye.draw(win)
'''


