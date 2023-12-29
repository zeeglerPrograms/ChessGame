# Developed by Daniel Zeegler
# Written 12-11-2023
# Here is a chessboard

def instructions():
    print("Welcome to a game of chess! Have fun.")
    print()
    
def piecesAreHere():
    global allPieces
    #call where all pieces are
    squaresTaken = []
    for eachPiece in allPieces:
        squaresTaken.append(eachPiece.piecePosition)
    return squaresTaken

def pieceIsHere(boardPosition):
    squaresTaken = piecesAreHere()
    #if a piece is here
    if boardPosition in squaresTaken:
        for eachPiece in allPieces:
            if boardPosition == eachPiece.piecePosition:
                print(("|" + eachPiece.pieceName), end = ' ')
            else:
                continue
    #else display an empty space
    else:
        print(("|" + boardPosition + " "), end = '')

def gatherPossibleMoves(pieceName, piecePosition):
    #This will gather all pieces' possible moves
    global row
    global rank
    squaresTaken = piecesAreHere()
    rank.sort()
    letterPosition = piecePosition[0]
    numberPosition = piecePosition[1]
    possibleMoves = []
    
    i = 1
    if pieceName == "wP":
        if numberPosition == "2":
            pawnMoves = ((letterPosition + str(int(numberPosition) + 1)), (letterPosition + str(int(numberPosition) + 2)))
            for possibleMove in pawnMoves:
                if possibleMove not in squaresTaken:
                    possibleMoves.append(possibleMove)
        else: 
            possibleMove = letterPosition + str(int(numberPosition) + 1)
            if possibleMove not in squaresTaken:
                possibleMoves.append(possibleMove)
        return possibleMoves
    elif pieceName == "wR":
            for thisRank in rank:
                if numberPosition == thisRank:
                    continue
                else:
                    possibleMove = (letterPosition + thisRank)
                    if possibleMove in squaresTaken:
                        break
                    else:
                        possibleMoves.append(possibleMove)
            for thisRow in row:
                if letterPosition == thisRow:
                    continue
                else:
                    possibleMove = thisRow + numberPosition
                    if possibleMove in squaresTaken:
                        break
                    else:
                        possibleMoves.append(thisRow + numberPosition)
            return possibleMoves
    elif pieceName == "bP":
        if numberPosition == "2":
            possibleMoves = ((letterPosition + str(int(numberPosition) - 1)), (letterPosition + str(int(numberPosition) - 2)))
        else: 
            possibleMoves = letterPosition + str(int(numberPosition) - 1)
        return possibleMoves
    
    
def drawLetters():
    #this labels the letters on the board
    global row
    for letter in row:
        print("  " + letter, end = " ")
    print()

def horLine():
    #this makes a horizontal line with 8 spaces for squares
    print(" ---" * 8)

def verLine(rankName, counter):
    #this makes a vertical line with 8 spaces for squares. I add one | for closing the board
    for i in range(8):
        #this gives the name of the square in the row
        squareName =  row[i] + rankName
        #this calls a function that checks to see if a piece is on this square
        pieceIsHere(squareName)
    #this prints the end of the line with the line number as well
    print("| " + str(8 - int(counter)))

def drawBoard():
    #this draws out the board
    global rank
    rank.sort(reverse=True)
    drawLetters()
    for i in range(8):
        horLine()
        verLine(rank[i], str(i))
    horLine()
    print()

class Piece:
    def __init__(self, pieceName, piecePosition):
        self.pieceName = pieceName
        self.piecePosition = piecePosition
    def __str__(self):
        return f"{self.pieceName}({self.piecePosition})"

    #I'd like to have the move rules here

#White Pieces
wKing = Piece("wK", "e1")
wQueen = Piece("wQ", "d1")
wRook1 = Piece("wR", "a1")
wRook2 = Piece("wR", "h1")
wKnight1 = Piece("wK", "b1")
wKnight2 = Piece("wK", "g1")
wLightBishop = Piece("wB", "f1")
wDarkBishop = Piece("wB", "c1")
wP1 = Piece("wP", "a2")
wP2 = Piece("wP", "b2")
wP3 = Piece("wP", "c2")
wP4 = Piece("wP", "d2")
wP5 = Piece("wP", "e2")
wP6 = Piece("wP", "f2")
wP7 = Piece("wP", "g2")
wP8 = Piece("wP", "h2")
#black Pieces
bKing = Piece("bK", "d8")
bQueen = Piece("bQ", "e8")
bRook1 = Piece("bR", "h8")
bRook2 = Piece("bR", "a8")
bKnight1 = Piece("bK", "g8")
bKnight2 = Piece("bK", "b8")
bLightBishop = Piece("bB", "c8")
bDarkBishop = Piece("bB", "f8")
bP1 = Piece("bP", "a7")
bP2 = Piece("bP", "b7")
bP3 = Piece("bP", "c7")
bP4 = Piece("bP", "d7")
bP5 = Piece("bP", "e7")
bP6 = Piece("bP", "f7")
bP7 = Piece("bP", "g7")
bP8 = Piece("bP", "h7")
#here are the pieces in arrays
whitePieces = [wKing, wQueen, wRook1, wRook2, wKnight1, wKnight2, wLightBishop, wDarkBishop, wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8]
blackPieces = [bKing, bQueen, bRook1, bRook2, bKnight1, bKnight2, bLightBishop, bDarkBishop, bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8]
allPieces = whitePieces + blackPieces
#row and rank
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank = ['1', '2', '3', '4', '5', '6', '7', '8']
#turn number
turnNumber = 1
#quit conditions
whiteIsCheckMated = False
blackIsCheckMated = False
userQuit = False

#main program
instructions()

#here starts the turn loop
while whiteIsCheckMated == False and blackIsCheckMated == False and userQuit == False:
    drawBoard()
    legalMoves = False
    while legalMoves == False:
        possibleMoves = []
        
        print("Your turn. Select a piece move, or type 'q' to Quit")
        squareMoveFrom = input("Which square is the piece you want to move on?:")
        if squareMoveFrom == 'q':
            print("Thanks for playing!")
            userQuit = True
            break
        for eachPiece in allPieces:
            if eachPiece.piecePosition == squareMoveFrom:
                possibleMoves = gatherPossibleMoves(eachPiece.pieceName, eachPiece.piecePosition)
                if possibleMoves:
                    print("This piece can move to these squares: ")
                    print(possibleMoves)
                    legalMoves = True
                    break
                else:
                    print("That piece has no legal moves.")
            else:
                continue
        
    moveCondition = False
    while(moveCondition == False):
        squareMoveTo = input("Which square would you like to move it to?: ")
        if squareMoveTo in possibleMoves:
            eachPiece.piecePosition = squareMoveTo
            print()
            print("Here's an updated image of the board.")
            moveCondition = True
        else:
            print("That move is not a legal move. Please select from the options listed.")
    turnNumber += 1
    
        