# Practical Worksheet P3: Graphical Programming
# Rupert Acuesta, 2016499

from graphics import *

#1
def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    leftLeg = Line(Point(80, 160), Point(100, 120))
    rightLeg = Line(Point(120, 160), Point(100, 120))
    arm = Line(Point(80, 100), Point(120, 100))

    arm.draw(win)
    rightLeg.draw(win)
    leftLeg.draw(win)
    body.draw(win)

#2
def drawCircle():
    win = GraphWin()
    radius = float(input("Enter radius: "))
    circle = Circle(Point(100, 100), radius)
    circle.draw(win)

#3
def drawArcheryTarget():
    win = GraphWin()

    #inner circle
    yellowCircle = Circle(Point(100, 100), 20)
    yellowCircle.setOutline("yellow")

    #second circle
    redCircle = Circle(Point(100, 100), 20*2)
    redCircle.setOutline("red")

    #outer circle
    blueCircle = Circle(Point(100, 100), 20*3)
    blueCircle.setOutline("blue")

    blueCircle.draw(win)
    redCircle.draw(win)
    yellowCircle.draw(win)

#4
def drawRectangle():
    win = GraphWin("draw rectangle", 200, 200)
    height = float(input("Enter height: "))
    width = float(input("Enter width: "))
    rectangle = Rectangle(Point())

#5
def blueCircle():
    win = GraphWin("Blue circle", 400, 400)
    point = win.getMouse()
    centre = Circle(Point(point.getX(), point.getY()), 50)
    centre.setOutline("blue")
    centre.draw(win)

#6
def drawLine():
    win = GraphWin("Line Drawer", 400, 400)
    for i in range(10):
        p1 = win.getMouse()
        point1 = Point(p1.getX(), p1.getY())
        point1.draw(win)
        p2 = win.getMouse()
        point2 = Point(p2.getX(), p2.getY())
        point2.draw(win)
        line = Line(p1, p2)
        line.draw(win)

#7
def tenStrings():
    win = GraphWin("ten strings", 400, 400)
    for i in range(10):
        p = win.getMouse()
        inputBox = Entry(Point(p.getX(), p.getY()), 10)
        inputBox.draw(win)

#8
def tenColouredRectangles():
    win = GraphWin("coloured rectangles", 400, 400)
    for i in range(10):
        inputBox = Entry(Point(200, 50), 10)
        p1 = win.getMouse()
        p1.draw(win)
        p2 = win.getMouse()
        p2.draw(win)

        inputBox.draw(win)
        win.getMouse()
        inputBox.setText("")

        rectangle = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
        rectangle.setOutline(inputBox.getText())
        rectangle.draw(win)

#9
def fiveClickStickFigure():

    win = GraphWin("stick figure", 400, 400)

    #head and radius
    headCentre = win.getMouse()
    headCentre.draw(win)
    radiusPoint = win.getMouse()
    radiusValue = radiusPoint.getX() - headCentre.getX()
    headCircle = Circle(Point(headCentre.getX(), headCentre.getY()), radiusValue)
    headCircle.draw(win)

    #middle body
    middleBody = win.getMouse()
    middleLine = Line(Point(headCentre.getX(), headCentre.getY() + radiusValue), Point(headCentre.getX(), middleBody.getY()))
    middleLine.draw(win)

    #middle arms
    arm = win.getMouse()
    armLine = Line(Point(arm.getX(), arm.getY()), Point(headCentre.getX() + (headCentre.getX() - arm.getX()), arm.getY()))
    armLine.draw(win)

    #left leg
    leftPoint = win.getMouse()
    leftLeg = Line(Point(leftPoint.getX(), leftPoint.getY()), Point(headCentre.getX(), middleBody.getY()))
    leftLeg.draw(win)

    #right leg
    rightPoint = win.getMouse()
    rightLeg = Line(Point(rightPoint.getX(), rightPoint.getY()), Point(headCentre.getX(), middleBody.getY()))
    rightLeg.draw(win)


def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")