from graphics import *

def main():
    size, colour1, colour2, colour3 = getInputs()
    drawFinalGrid(size, colour1, colour2, colour3)

def getInputs():
    while True:
        size = input("enter size(valid sizes are 5 & 7): ") #cant be int otherwise error
        if size == "5" or size == "7":
            break
        print("invalid size input, enter again")
    print("pick colours from: red, green, blue, magenta, orange & cyan")
    validColours = ["red", "green", "blue", "magenta", "orange", "cyan"]
    while True:
        colour1 = checkValid(validColours, 1)
        colour2 = checkValid(validColours, 2)
        colour3 = checkValid(validColours, 3)
        if colour1 == colour2 == colour3: #at least 1 different colour
            print("invalid, there must be at least 1 different colour")
        else:
            break
    return int(size), colour1, colour2, colour3

def checkValid(validColours, numCount):
    notValid = True
    while notValid:
        inputColour = input("enter colour {0}: ".format(numCount)).lower()
        for validColour in validColours:
            if inputColour == validColour:
                notValid = False #valid colour found
                break
        if notValid == True:
            print("invalid colour input, enter again")
    return inputColour

def drawFinalGrid(size, colour1, colour2, colour3):
    win = GraphWin("window", size*100, size*100)
    x, y = 0, (size*100) - 100
    bottomSquares, topSquares = 1, size-1
    for diagonalSquare in range(size): #diagonal squares
        if(diagonalSquare % 2) == 0: #even means final number patch
            finalNumPatch(win, x, y, colour2)
        else:
            penNumPatch(win, x, y, colour2)
        if diagonalSquare > 0:
            downY = y + 100
            for bottomSquare in range(bottomSquares): #bottomside squares
                if(bottomSquares % 2) == 0:
                    finalNumPatch(win, x, downY, colour3)
                else:
                    penNumPatch(win, x, downY, colour3)
                downY += 100
            bottomSquares += 1
        upY = y - 100
        for topSquare in range(topSquares): #topside squares
            penNumPatch(win, x, upY, colour1)
            upY -= 100
        topSquares -= 1
        x += 100
        y -= 100

def finalNumPatch(win, x, y, colour):
    bottomX, topY = x + 100, y
    for square in range(5):
        drawSquare(win, x, topY, bottomX, y+100, "white")
        drawSquare(win, x, topY+10, bottomX-10, y+100, colour)
        topY += 20
        bottomX -= 20

def penNumPatch(win, x, y, colour):
    circleY = y #row of circles downwards
    for circleRow in range(3):
        circleX = x #circles going to the right
        for circle in range(3):
            drawCircle(win, circleX, circleY, 20, colour)
            if circle < 2: # 2 boxes in between
                drawSquare(win, circleX+20, circleY,
                circleX+40, circleY+20, colour)
            if circleRow < 2: #3 boxes in 2 rows
                drawSquare(win, circleX, circleY+20,
                circleX+20, circleY+40, colour)
            if circleRow < 2 and circle < 2: #4 circles facing opposite direction
                drawCircle(win, circleX+20, circleY+20, 0, colour)
            circleX += 40
        circleY += 40

def drawCircle(win, x, y, directionX, colour):
    circle = Circle(Point(x+10, y+10), 10)
    circle.setFill(colour)
    circle.setOutline(colour)
    triangle = Polygon(Point(x+directionX, y), Point(x+10, y+10),
    Point(x+directionX, y+20))
    triangle.setFill("white")
    triangle.setOutline("white")
    circle.draw(win)
    triangle.draw(win)

def drawSquare(win, x, y, x2, y2, colour):
    square = Rectangle(Point(x, y), Point(x2, y2))
    square.setFill(colour)
    square.setOutline(colour)
    square.draw(win)

main()