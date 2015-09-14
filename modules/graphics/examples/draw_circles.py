from graphics import *


def main():
    win = GraphWin("My Window", 500, 500)
    
    circle = Circle(Point(80, 80), 10)
    circle.setFill("blue")
    circle.setOutline("white")
    circle.draw(win)
    
    for i in range(20):
        pointClicked = win.getMouse()

        # creates a clone of circle
        newCircle = circle.clone()

        # uncomment this if you want to see where you click
        #print("Clicked at point", pointClicked.getX(), "," , pointClicked.getY())
        
        circleCenter = circle.getCenter()

        # how many pixels to move in the x axis
        dx = pointClicked.getX() - circleCenter.getX()

        dy = pointClicked.getY() - circleCenter.getY()
        
        #circle.move(dx, dy)
        
        newCircle.move(dx, dy)
        newCircle.draw(win)
    
        # uncomment this if you want to see how much you moved in the x and y axis.
        #print("Moved", dx, "pixels in the x-axis and", dy, "pixels in the y-axis!")
        
    text = Text(Point(250, 250), "Hello World!")
    text.setSize(24)
    text.setTextColor("red")
    text.draw(win)
    win.getMouse()  # pause for click in window
    win.close()

main()
