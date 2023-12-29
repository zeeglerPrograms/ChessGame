# Developed by Daniel Zeegler
# Written 12-11-2023
# Here is a chessboard

piece = 'k'
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank = ['1', '2', '3', '4', '5', '6', '7', '8']

def instructions():
    print("Welcome to a game of chess! Have fun.")
def pieceIsHere(boardPosition):
    #call where all pieces are
    #gatherPiecePosition()
    #if a piece is here
    if(boardPosition == 'd1' or boardPosition == 'e8'):
        #display the piece
        print(("|" + ' k' + " "), end = '')
    #this is a test of putting pieces out
    elif(boardPosition == 'e1' or boardPosition == 'd8'):
        print(("|" + ' q' + " "), end = '')
    elif(boardPosition == 'a2' or boardPosition == 'b2' or boardPosition == 'c2' or boardPosition == 'd2' or boardPosition == 'e2' or boardPosition == 'f2' or boardPosition == 'g2' or boardPosition == 'h2'):
        print(("|" + ' p' + " "), end = '')
    elif(boardPosition == 'a7' or boardPosition == 'b7' or boardPosition == 'c7' or boardPosition == 'd7' or boardPosition == 'e7' or boardPosition == 'f7' or boardPosition == 'g7' or boardPosition == 'h7'):
        print(("|" + ' p' + " "), end = '')
    #else display an empty space
    else:
        print(("|" + boardPosition + " "), end = '')

def gatherPiecePosition():
    #This will gather all pieces' positions
    global whitePieces
    global blackPieces
    global allPieces
    global turnNumber
    #this sets the whitePieces at the beginning of the game
    for eachPiece in whitePieces:
        if eachPiece == "wKing":
            if(turnNumber == 1):
                piecePosition = "e1"
        elif eachPiece == "wQueen":
            if(turnNumber == 1):
                piecePosition = "d1"
        elif eachPiece == "wRook1":
            if(turnNumber == 1):
                piecePosition = "a1"
        elif eachPiece == "wRook2":
            if(turnNumber == 1):
                piecePosition = "h1"
        elif eachPiece == "wKnight1":
            if(turnNumber == 1):
                piecePosition = "b1"
        elif eachPiece == "wKnight2":
            if(turnNumber == 1):
                piecePosition = "g1"
        elif eachPiece == "wLightBishop":
            if(turnNumber == 1):
                piecePosition = "c1"
        elif eachPiece == "wDarkBishop":
            if(turnNumber == 1):
                piecePosition = "f1"
        elif eachPiece == "wP1":
            if(turnNumber == 1):
                piecePosition = "a2"
        elif eachPiece == "wP2":
            if(turnNumber == 1):
                piecePosition = "b2"
        elif eachPiece == "wP3":
            if(turnNumber == 1):
                piecePosition = "c2"
        elif eachPiece == "wP4":
            if(turnNumber == 1):
                piecePosition = "d2"
        elif eachPiece == "wP5":
            if(turnNumber == 1):
                piecePosition = "e2"
        elif eachPiece == "wP6":
            if(turnNumber == 1):
                piecePosition = "f2"
        elif eachPiece == "wP7":
            if(turnNumber == 1):
                piecePosition = "g2"
        elif eachPiece == "wP8":
            if(turnNumber == 1):
                piecePosition = "h2"
        else:
            piecePosition = ""
        #print(Piece(eachPiece, piecePosition))
    
    for eachPiece in blackPieces:
        if eachPiece == "bKing":
            if(turnNumber == 1):
                piecePosition = "d8"
        elif eachPiece == "bQueen":
            if(turnNumber == 1):
                piecePosition = "e8"
        elif eachPiece == "bRook1":
            if(turnNumber == 1):
                piecePosition = "h8"
        elif eachPiece == "bRook2":
            if(turnNumber == 1):
                piecePosition = "a8"
        elif eachPiece == "bKnight1":
            if(turnNumber == 1):
                piecePosition = "g8"
        elif eachPiece == "bKnight2":
            if(turnNumber == 1):
                piecePosition = "b8"
        elif eachPiece == "bLightBishop":
            if(turnNumber == 1):
                piecePosition = "f8"
        elif eachPiece == "bDarkBishop":
            if(turnNumber == 1):
                piecePosition = "c8"
        elif eachPiece == "bP1":
            if(turnNumber == 1):
                piecePosition = "a7"
        elif eachPiece == "bP2":
            if(turnNumber == 1):
                piecePosition = "b7"
        elif eachPiece == "bP3":
            if(turnNumber == 1):
                piecePosition = "c7"
        elif eachPiece == "bP4":
            if(turnNumber == 1):
                piecePosition = "d7"
        elif eachPiece == "bP5":
            if(turnNumber == 1):
                piecePosition = "e7"
        elif eachPiece == "bP6":
            if(turnNumber == 1):
                piecePosition = "f7"
        elif eachPiece == "bP7":
            if(turnNumber == 1):
                piecePosition = "g7"
        elif eachPiece == "bP8":
            if(turnNumber == 1):
                piecePosition = "h7"
        else:
            piecePosition = ""
        
        #print(Piece(eachPiece, piecePosition))

def horLine():
    #this makes a horizontal line with 8 spaces for squares
    print(" ---" * 8)

def verLine(rankName):
    #this makes a vertical line with 8 spaces for squares. I add one | for closing the board
    for i in range(8):
        #this gives the name of the square in the row
        squareName =  row[i] + rankName
        #this calls a function that checks to see if a piece is on this square
        pieceIsHere(squareName)
    print("|")

def drawBoard():
    #this draws out the board
    rank.sort(reverse=True)
    for i in range(8):
        horLine()
        verLine(rank[i])
    horLine()

class Piece:
    def __init__(self, pieceName, piecePosition):
        self.pieceName = pieceName
        self.piecePosition = piecePosition
    def __str__(self):
        return f"{self.pieceName}({self.piecePosition})"

    #I'd like to have the move rules here

whitePieces = ["wKing", "wQueen", "wRook1", "wRook2", "wKnight1", "wKnight2", "wLightBishop", "wDarkBishop", "wP1", "wP2", "wP3", "wP4", "wP5", "wP6", "wP7", "wP8"]
blackPieces = ["bKing", "bQueen", "bRook1", "bRook2", "bKnight1", "bKnight2", "bLightBishop", "bDarkBishop", "bP1", "bP2", "bP3", "bP4", "bP5", "bP6", "bP7", "bP8"]
allPieces = whitePieces + blackPieces
turnNumber = 1

#main program
instructions()
gatherPiecePosition()
drawBoard()


"""
for whitePiece in whitePieces:
    print(Piece(whitePiece))
for blackPiece in blackPieces:
    print(Piece(blackPiece))
"""