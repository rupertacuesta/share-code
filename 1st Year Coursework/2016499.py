from graphics import *
from time import sleep

def main():
    size, colour1, colour2, colour3 = getInputs()
    drawGrid(size, colour1, colour2, colour3)

def getInputs():
    while True:
        size = input("enter size: ")
        if size == "5" or size == "7":
            break
        else:
            print("invalid input, enter again")
    colours = "red green blue magenta orange cyan grey white"
    splitColours = colours.split() #split into list of strings
    while True:
        colourNum = 1
        colour1 = validColour(splitColours, colourNum)
        colourNum += 1
        colour2 = validColour(splitColours, colourNum)
        colourNum += 1
        colour3 = validColour(splitColours, colourNum)
        if colour1 == colour2 == colour3:
            print("invalid, there must be at least 1 different colour")
        else:
            break
    return size, colour1, colour2, colour3

def validColour(splitColours, colourNum):
    notValid = True
    while notValid:
        inputColour = input("enter colour {0}: ".format(colourNum))
        for eachColour in splitColours:
            if inputColour != eachColour:
                pass
            else:
                notValid = False
                break
        if notValid == False:
            break
        else:
            print("invalid colour, enter again")
    return inputColour

def drawGrid(size, colour1, colour2, colour3):
    intSize = int(size)
    win = GraphWin("window", intSize*100, intSize*100)
    newSize = int((intSize+1)/2) #diagonal squares
    downSquares = 2
    upSquares = intSize - 1
    x = 0
    y = (intSize*100) - 100
    for finalPatch in range(newSize):
        finalNumberPatch(win, x, y, colour1)
        if finalPatch > 0: #add patches downwards aside from 1st box
            penultimateNumberPatch(win, x-100, y+100, colour1)
            downY = y + 100
            downY2 = y + 200
            for downFinPatch in range(downSquares):
                finalNumberPatch(win, x, downY, colour2)
                downY += 100
            for downFinPatch2 in range(downSquares-1):
                penultimateNumberPatch(win, x-100, downY2, colour2)
                downY2 += 100
            downSquares += 2
        upY = y - 100 #add patches upwards aside from last top right box
        upY2 = y - 200
        for upPenPatch in range(upSquares):
            penultimateNumberPatch(win, x, upY, colour3)
            upY -= 100
        for upPenPatch2 in range(upSquares-1):
            penultimateNumberPatch(win, x+100, upY2, colour3)
            upY2 -= 100
        upSquares -= 2
        x += 200
        y -= 200
    time.sleep(5)

def finalNumberPatch(win, x, y, colour):
    topY = y - 10 #only these 2 dimensions change
    bottomX = x + 110
    for i in range(5):
        drawRectangle(win, x, topY+10, bottomX-10, y+100, "white")
        drawRectangle(win, x, topY+20, bottomX-20, y+100, colour)
        topY += 20
        bottomX -= 20

def penultimateNumberPatch(win, x, y, colour):
    circlesY = y
    for circlesDown in range(3): #draws 3 circles down
        drawCircle(win, x, circlesY, colour)
        drawTriangle(win, Point(x+20, circlesY),
        Point(x+10, circlesY+10), Point(x+20, circlesY+20))
        squaresX = x
        if circlesDown < 2: #draws 3 squares across on 2 rows
            for circlesInbetween in range(3):
                drawSquare(win, squaresX, circlesY+20, colour)
                if circlesInbetween < 2: #draws 2 circles inbetween main rows
                    drawCircle(win, squaresX+20, circlesY+20, colour)
                    drawTriangle(win, Point(squaresX+20, circlesY+20),
                    Point(squaresX+30, circlesY+30), Point(squaresX+20, circlesY+40))
                squaresX += 40
        circlesX = x + 40
        for circlesAcross in range(2): #draws 2 circles across
            drawCircle(win, circlesX, circlesY, colour)
            drawTriangle(win, Point(circlesX+20, circlesY),
            Point(circlesX+10, circlesY+10), Point(circlesX+20, circlesY+20))
            drawSquare(win, circlesX-20, circlesY, colour) #draws 2 squares in between 3 circles
            circlesX += 40
        circlesY += 40

def drawRectangle(win, x, topY, bottomX, bottomY, colour):
    rectangle = Rectangle(Point(x, topY), Point(bottomX, bottomY))
    rectangle.setFill(colour)
    rectangle.draw(win)

def drawCircle(win, rowX, rowY, colour):
    circle = Circle(Point(rowX+10, rowY+10), 10)
    circle.setFill(colour)
    circle.draw(win)

def drawSquare(win, rowX, rowY, colour):
    square = Rectangle(Point(rowX, rowY), Point(rowX+20, rowY+20))
    square.setFill(colour)
    square.draw(win)

def drawTriangle(win, point1, point2, point3):
    triangle = Polygon(Point(point1.getX(), point1.getY()),
    Point(point2.getX(), point2.getY()),
    Point(point3.getX(), point3.getY()))
    triangle.setOutline("white")
    triangle.setFill("white")
    triangle.draw(win)

main()
