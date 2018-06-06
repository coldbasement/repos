#convert_gui.pyw
#Program to convert Celsius to Fahrenheit using a simple
# Graphical Interface

from graphics import *

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    #Draw the Interface 
    Text(Point(1,3), "  Celsius Temperature").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText(" ")
    inputText.draw(win)
    outputText = Text(Point(2.25,1), "")
    outputText.draw(win)
    button = Text(Point(1.5,2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

    # Wait for a mouse click
    win.getMouse()

    # convert input
    celsius = float(inputText.getText())
    farenheit = 9.0/5.0 * celsius + 32

    #Display output and change button
    outputText.setText(round(farenheit,2))
    button.setText("Quit")

    #Wait for click and then quit
    win.getMouse()
    win.close()


    #blah blah blah 
   # input("Press <Enter> to exit.")
main()



