
#Futval_Graph.py

from graphics import *
'''
def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get the principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), " O.OK").draw(win)
    Text(Point(20, 180),  " 2.5K").draw(win)
    Text(Point(20, 130),  " 5.0K").draw(win)
    Text(Point(20, 80),  " 7.5K").draw(win)
    Text(Point(20, 30),  "10.5K").draw(win)

    # Draw Bar For Intitial Principal

    height = principal * 0.02
    bar = Rectangle(Point(42, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
  
   # Draw bars for successive Years 

    for year in range (1,11):
       #Calculate value for the next year
       principal =  principal * (1 + apr)
       # draw bar for this value
       xll = year * 25 + 42
       height = principal * 0.02
       bar = Rectangle(Point(xll, 230), Point(xll+25, 230-height))
       bar.setFill("green")
       bar.setWidth(2)
       bar.draw(win)


    input("Prese <Enter> to quit")
    win.close()
main()
'''
def main():

# Introduction
 print("This program plots the growth of a 10-year investment.")

    # Get the principal and interest rate
principal = float(input("Enter the initial principal: "))
apr = float(input("Enter the annualized interest rate: "))

# Create a Graphics window with labels on left edge 
win = GraphWin("Investment Growth Chart", 320, 240)
win.setBackground("white")
win.setCoords(-1.75,-200, 11.5, 10400)
Text(Point(-1, 0), " O.OK").draw(win)
Text(Point(-1, 2500),  " 2.5K").draw(win)
Text(Point(-1, 5000),  " 5.0K").draw(win)
Text(Point(-1, 7500),  " 7.5K").draw(win)
Text(Point(-1, 10000),  "10.5K").draw(win)


  # Draw Bar For Intitial Principal

bar = Rectangle(Point(0, 0), Point(1, principal))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

# Draw a bar for each subsequent year
for year in range(1,11):
    principal = principal * (1 + apr)
    bar = Rectangle(Point(year, 0), Point(year+1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


input("Press <Enter> to quit.")
win.close()

main()
