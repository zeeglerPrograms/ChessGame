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
        #and this one makes squares blank
        print("|   ", end = '')

def friendOrFoe(possibleMove, pieceName, piecePosition):
    global allPieces
    squaresTaken = piecesAreHere()
    possibleMoveFinal = ""
    #if possible move is taken by a piece
    if possibleMove in squaresTaken:
        #check all pieces
        for thisPiece in allPieces:
            #for the piece on this square
            if thisPiece.piecePosition == possibleMove:
                #if the first letter is the same, same color, so do nothing
                if thisPiece.pieceName[0] == pieceName[0]:
                    break
                elif thisPiece.pieceName[0] != pieceName[0]:
                    #otherwise its an enemy piece, and show it taking.
                    possibleMoveFinal = str(pieceName[1]).lower() + piecePosition + "x" + thisPiece.piecePosition
                    #possibleMoves.append(str(pieceName[1]) + piecePosition + "x" + thisPiece.piecePosition)
    return possibleMoveFinal

#def move like a rook
def rookMoves(pieceName, piecePosition):
    global row
    global rank
    global allPieces
    squaresTaken = piecesAreHere()
    rank.sort()
    letterPosition = piecePosition[0]
    numberPosition = piecePosition[1]
    possibleMoves = []
    #moving up the numbers
    thisRank = numberPosition
    while int(thisRank) < 8:
        thisRank = int(thisRank) + 1
        possibleMove = (letterPosition + str(thisRank))
        if possibleMove in squaresTaken:
            for thisPiece in allPieces:
                if thisPiece.piecePosition == possibleMove:
                    if thisPiece.pieceName[0] == pieceName[0]:
                        break
                    elif thisPiece.pieceName[0] != pieceName[0]:
                        pieceLetter = pieceName[1].lower()
                        possibleMoves.append(pieceLetter + piecePosition + "x" + thisPiece.piecePosition)
            break
        else:
            possibleMoves.append(possibleMove)
    #moving down the numbers
    
    thisRank = numberPosition   
    while int(thisRank) > 1:
        thisRank = int(thisRank) - 1
        possibleMove = (letterPosition + str(thisRank))
        if possibleMove in squaresTaken:
            for thisPiece in allPieces:
                if thisPiece.piecePosition == possibleMove:
                    if thisPiece.pieceName[0] == pieceName[0]:
                        break
                    elif thisPiece.pieceName[0] != pieceName[0]:
                        pieceLetter = pieceName[1].lower()
                        possibleMoves.append(pieceLetter + piecePosition + "x" + thisPiece.piecePosition)
            break
        else:
            #how do I get it to list 'a1' 'a2' and not reversed like this
            possibleMoves.append(possibleMove)
        
    #sideways movement
    for thisRow in row:
        if letterPosition == thisRow:
            continue
        else:
            if(letterPosition < thisRow):
                possibleMove = thisRow + numberPosition
                if possibleMove in squaresTaken:
                    rookMove = friendOrFoe(possibleMove, pieceName, piecePosition)
                    if(rookMove):
                        possibleMoves.append(rookMove)
                        break
                    else:
                        break
                else:
                    possibleMoves.append(thisRow + numberPosition)
            if(letterPosition > thisRow):
                rowToCheck = row.index(letterPosition) - row.index(thisRow)
                print("row to check:")
                print(rowToCheck)
                i = 1
                while i <= rowToCheck:
                    possibleMove = row[rowToCheck - i] + numberPosition
                    if possibleMove in squaresTaken:
                        rookMove = friendOrFoe(possibleMove, pieceName, piecePosition)
                        if(rookMove):
                            if rookMove in possibleMoves:
                                break
                            else:
                                rookMoveRow = int(row.index(rookMove[1])) - (i)
                                oneRowUp = row[rookMoveRow] + numberPosition
                                oneRowUp = pieceName[1].lower() + piecePosition + "x" + oneRowUp
                                print("this onerow up is: " + oneRowUp)

                                if oneRowUp not in possibleMoves:
                                    possibleMoves.append(rookMove) 
                                i += 500             
                                break
                        else:
                            break
                    else:
                        if possibleMove in possibleMoves:
                            break
                        else:
                            possibleMoves.append(possibleMove)
                    i += 1

    
    return possibleMoves

#def move like a bishop
def bishopMoves(pieceName, piecePosition):
    global row
    global rank
    global allPieces
    squaresTaken = piecesAreHere()
    rank.sort()
    letterPosition = piecePosition[0]
    numberPosition = piecePosition[1]
    possibleMoves = []
    possibleMoveList = []
    i = 1
    j = 0
    foundMove = False
    if letterPosition in row:
        rowIndex = row.index(letterPosition)

    #bishopMoves
    # i wish I could write a loop that would include all this below
    while i <= rowIndex and foundMove == False:
        upLeftMove = row[int(rowIndex) - i] + str(int(numberPosition) + i)
        if upLeftMove in squaresTaken:
            #need to add in friend_or_foe
            thisMove = friendOrFoe(upLeftMove, pieceName, piecePosition)
            if(thisMove):
                possibleMoveList.append(thisMove)
                foundMove = True
            else:
                break
        else:
            possibleMoveList.append(upLeftMove)
        i += 1
    i = 1
    foundMove = False
    while i <= rowIndex and foundMove == False:
        downLeftMove = row[int(rowIndex) - i] + str(int(numberPosition) - i)
        if downLeftMove in squaresTaken:
            #need to add in friend_or_foe
            
            thisMove = friendOrFoe(downLeftMove, pieceName, piecePosition)
            if(thisMove):
                possibleMoveList.append(thisMove)
                foundMove = True
            else: 
                break
        else:
            possibleMoveList.append(downLeftMove)
        i += 1
    i = 1
    foundMove = False
    while i < (8 - rowIndex) and foundMove == False:
        upRightMove = row[int(rowIndex) + i] + str(int(numberPosition) + i)
        if upRightMove in squaresTaken:
            thisMove = friendOrFoe(upRightMove, pieceName, piecePosition)
            if(thisMove):
                possibleMoveList.append(thisMove)
                foundMove = True
            else:
                break
        else:
            possibleMoveList.append(upRightMove)
        i += 1
    i = 1
    foundMove = False
    while i < (8 - rowIndex) and foundMove == False:
        backRightMove = row[int(rowIndex) + i] + str(int(numberPosition) - i)
        if backRightMove in squaresTaken:
            #need to add in friend_or_foe
            thisMove = friendOrFoe(backRightMove, pieceName, piecePosition)
            if(thisMove):
                possibleMoveList.append(thisMove)
                foundMove = True
            else:
                break
        else:
            possibleMoveList.append(backRightMove)
        i += 1
    i = 1

    #checks the moves to see if they work
    for possibleMove in possibleMoveList:
        #thispiece takes thispiece is 6 char long
        if(len(possibleMove) == 6):
            possibleMoves.append(possibleMove)
        #not valid if only 1 long
        elif(len(possibleMove) == 1):
            continue
        #not valid if a negative number
        elif(possibleMove[1] == "-"):
            continue
        else:
            #if out of range or the wrong length, do nothing
            if int(possibleMove[1]) < 1 or int(possibleMove[1]) > 8 or len(possibleMove) == 3:
                continue
            else:    
                #this move passed the test.
                possibleMoves.append(possibleMove)
    foundMove = False
    return possibleMoves

def pawnMoves(pieceName, piecePosition):
    global row
    global rank
    global allPieces
    squaresTaken = piecesAreHere()
    rank.sort()
    letterPosition = piecePosition[0]
    numberPosition = piecePosition[1]
    possibleMoves = []
    possibleMoveList = []
    #define moves for white pawn
    if letterPosition in row:
            rowIndex = row.index(letterPosition)
    if pieceName == "wP":
        numberToUse = "2"
        pawnMoves = ((letterPosition + str(int(numberPosition) + 1)), (letterPosition + str(int(numberPosition) + 2)))
        possibleMove = letterPosition + str(int(numberPosition) + 1)
        if rowIndex != 7:
            possibleCapture1 = (row[rowIndex + 1] + str(int(numberPosition) + 1))
        else:
            possibleCapture1 = ""
        if rowIndex != 0:
            possibleCapture2 = (row[rowIndex - 1] + str(int(numberPosition) + 1))
        else:
            possibleCapture2 = ""
    #define moves for black pawn
    elif pieceName == "bP":
        numberToUse = "7"
        pawnMoves = ((letterPosition + str(int(numberPosition) - 1)), (letterPosition + str(int(numberPosition) - 2)))
        possibleMove = letterPosition + str(int(numberPosition) - 1)
        if rowIndex != 7:
            possibleCapture1 = (row[rowIndex + 1] + str(int(numberPosition) - 1))
        else:
            possibleCapture1 = ""
        if rowIndex != 0:
            possibleCapture2 = (row[rowIndex - 1] + str(int(numberPosition) - 1))
        else:
            possibleCapture2 = ""
    
    #pawns can move two spaces on their first move
    if numberPosition == numberToUse:
        for possibleMove in pawnMoves:
            if possibleMove not in squaresTaken:
                possibleMoves.append(possibleMove)
    else: 
        #or one space afterwards
        if possibleMove not in squaresTaken:
            possibleMoves.append(possibleMove)
        
    #if either of these are in squares taken, check if theyre friend or foe and return them
    if possibleCapture1 in squaresTaken or possibleCapture2 in squaresTaken:
        possibleCaptures = [possibleCapture1, possibleCapture2]
        for possibleCapture in possibleCaptures:
            possibleMove = friendOrFoe(possibleCapture, pieceName, piecePosition)
            if possibleMove:
                possibleMoves.append(possibleMove)
            
    return possibleMoves

    #pawns can en pessant

def gatherPossibleMoves(pieceName, piecePosition):
    #This will gather all pieces' possible moves
    global row
    global rank
    global allPieces
    global allWhiteMoves
    global allBlackMoves
    squaresTaken = piecesAreHere()
    rank.sort()
    if piecePosition == "":
        pass
    else:
        letterPosition = piecePosition[0]
        numberPosition = piecePosition[1]
        

        possibleMoves = []
        i = 1
        #this lets us move up and down in rows
        if letterPosition in row:
                rowIndex = row.index(letterPosition)

        if pieceName == "wK" or pieceName == "bK":
            #white king can move forward, back, left, right, diagonally forward left, dfr, dbl, dbr
            
            possibleMoveList = ((letterPosition + str(int(numberPosition) + 1)), (row[int(rowIndex) + 1] + str(int(numberPosition) + 1)), 
                                (row[int(rowIndex) + 1] + numberPosition), (row[int(rowIndex) + 1] + str(int(numberPosition) - 1)), 
                                (letterPosition + str(int(numberPosition) - 1)), (row[int(rowIndex) - 1] + str(int(numberPosition) - 1)),
                                (row[int(rowIndex) - 1] + numberPosition), (row[int(rowIndex) - 1] + str(int(numberPosition) + 1)))
            #kings can castle if they havent moved yet and if the rook hasnt moved yet
            for possibleMove in possibleMoveList:
                #if possible move is out of range, do nothing
                if possibleMove[1] == "0" or int(possibleMove[1]) > 8:
                    continue
                else:
                    #king cant move into check
                    if pieceName == "wK":
                        for everyBlackMove in allBlackMoves:
                            for eachBlackMove in everyBlackMove:
                                if possibleMove in eachBlackMove:
                                    possibleMove = ""
                    if pieceName == "bK":
                        for everyWhiteMove in allWhiteMoves:
                            for eachWhiteMove in everyWhiteMove:
                                if possibleMove in eachWhiteMove:
                                    possibleMove = ""  
                    #if possible move is taken by a piece
                    if possibleMove in squaresTaken:
                        #check all pieces
                        for thisPiece in allPieces:
                            #for the piece on this square
                            if thisPiece.piecePosition == possibleMove:
                                #if the first letter is the same, same color, so do nothing
                                if thisPiece.pieceName[0] == pieceName[0]:
                                    continue
                                #otherwise its an enemy piece, and show it taking.
                                elif thisPiece.pieceName[0] != pieceName[0]:
                                    possibleMoves.append("k" + piecePosition + "x" + thisPiece.piecePosition)
                    else :
                        if possibleMove != "":
                            possibleMoves.append(possibleMove)
            return possibleMoves
        elif pieceName == "wQ" or pieceName == "bQ":
            #white queen can move like a rook + a bishop
            rookSquares =  rookMoves(pieceName, piecePosition)
            bishopSquares = bishopMoves(pieceName, piecePosition)
            queenMoves = bishopSquares + rookSquares
            return queenMoves
        elif pieceName == "wR" or pieceName == "bR":
            return rookMoves(pieceName, piecePosition)
        elif pieceName == "wN" or pieceName == "bN":
            #knights can move up two and over 1
            #if theyre not too low of a row or too high of a row or position they can go + 2 there

            #if knight can have all moves
            if rowIndex > 2 and rowIndex < 7 and int(numberPosition) > 2 and int(numberPosition) < 7:
                pass
            else:
                #else take away moves here
                if rowIndex == 6 or rowIndex == 7:
                    if rowIndex == 6:
                        rowIndexP2 = ""
                        rowIndexP1 = row[rowIndex + 1]
                    if rowIndex == 7:
                        rowIndexP2 = ""
                        rowIndexP1 = ""
                if rowIndex == 1 or rowIndex == 0:
                    if rowIndex == 1:
                        rowIndexM2 = ""
                        rowIndexM2 = row[rowIndex - 2]
                    if rowIndex == 0:
                        rowIndexM1 = ""
                        rowIndexM2 = ""
                if int(numberPosition) > 6 or int(numberPosition) < 3:
                    if int(numberPosition) > 2:
                        if numberPosition == "7":
                            numPosP2 = ""
                        if numberPosition == "8":
                            numPosP1 = ""
                            numPosP2 = ""
                    elif int(numberPosition) == 2 or int(numberPosition) == 1:
                        if int(numberPosition) == 2:
                            numPosM2 = ""
                        if int(numberPosition) == 1:
                            numPosM1 = ""
                            numPosM2 = ""
            #check for existance of variables. If not there, give the move
            try:
                rowIndexP1
            except NameError:
                rowIndexP1 = row[rowIndex + 1]
            try:
                rowIndexP2
            except NameError:
                rowIndexP2 = row[rowIndex + 2]
            try:
                rowIndexM1
            except NameError:
                rowIndexM1 = row[rowIndex - 1]
            try:
                rowIndexM2
            except NameError:
                rowIndexM2 = row[rowIndex - 2]
            try:
                numPosP1
            except NameError:
                numPosP1 = str(int(numberPosition) + 1)
            try:
                numPosP2
            except NameError:
                numPosP2 = str(int(numberPosition) + 2)
            try:
                numPosM1
            except NameError:
                numPosM1 = str(int(numberPosition) - 1)
            try:
                numPosM2
            except NameError:
                numPosM2 = str(int(numberPosition) - 2)
            
            #here are all the possible moves
            possibleMove1 = (rowIndexP1 + numPosP2)
            possibleMove2 = (rowIndexP1 + numPosM2)
            possibleMove3 = (rowIndexM1 + numPosP2)
            possibleMove4 = (rowIndexM1 + numPosM2)
            possibleMove5 = (rowIndexP2 + numPosP1)
            possibleMove6 = (rowIndexP2 + numPosM1)
            possibleMove7 = (rowIndexM2 + numPosP1)
            possibleMove8 = (rowIndexM2 + numPosM1) 

            #this makes a list of them
            possibleMovesList = []
            possibleMovesListToFilter = [possibleMove1, possibleMove2, possibleMove3, possibleMove4, possibleMove5, possibleMove6, possibleMove7, possibleMove8]
            #if the possible moves don't have two spaces, they arent good moves
            for possibleMoveForList in possibleMovesListToFilter:
                if(len(possibleMoveForList) == 2):
                    possibleMovesList.append(possibleMoveForList)
            #check each possible move
            for possibleMove in possibleMovesList:
                if possibleMove == "":
                    continue
                #if possible square is out of range of board
                elif possibleMove[0] not in row:
                    continue
                #if possible square is a negative number or 0
                elif possibleMove[1] == "-" or possibleMove[1] == "0":
                    continue
                else:
                    if possibleMove in squaresTaken:
                        finalMove = friendOrFoe(possibleMove, pieceName, piecePosition)
                        if finalMove:  
                            possibleMoves.append(finalMove)
                    elif len(possibleMove) == 2:
                        possibleMoves.append(possibleMove)
            return possibleMoves
        elif pieceName == "wB" or pieceName == "bB":
            return bishopMoves(pieceName, piecePosition)
        elif pieceName == "wP" or pieceName == "bP":
            return pawnMoves(pieceName, piecePosition)

def takeAPiece(squareMoved):
    global allPieces
    for eachPiece in allPieces:
        if eachPiece.piecePosition == squareMoved:
            eachPiece.piecePosition = ""

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
    global whoseTurn
    #this makes a vertical line with 8 spaces for squares. I add one | for closing the board
    for i in range(8):
        #this gives the name of the square in the row
        squareName =  row[i] + rankName
        #this calls a function that checks to see if a piece is on this square
        pieceIsHere(squareName)
    #this prints the end of the line with the line number as well
    if whoseTurn == "white":
        print("| " + str(8 - int(counter)))
    elif whoseTurn == "black":
        print("| " + str(int(counter) + 1))

def drawBoard():
    #this draws out the board
    global rank
    global row
    global whoseTurn
    if whoseTurn == "white":
        row.sort(reverse = False)
        rank.sort(reverse=True)
    elif whoseTurn == "black":
        row.sort(reverse=True)
        rank.sort(reverse = False)
    drawLetters()
    for i in range(8):
        horLine()
        verLine(rank[i], str(i))           
    horLine()
    print()

def flipTurn():
    global whoseTurn
    if whoseTurn == "white":
        whoseTurn = "black"
    elif whoseTurn == "black":
        whoseTurn = "white"

def checkChecker():
    #this checks for checks
    global whitePieces
    global blackPieces
    global whiteIsInCheck
    global blackIsInCheck
    global wKing
    global bKing
    global whoseTurn
    global allWhiteMoves
    global allBlackMoves
    
    if(whoseTurn == "white" or blackIsInCheck == True):
        i = 0
        for whitePiece in whitePieces:
            allWhiteMoves = []
            allWhiteMoves.append(gatherPossibleMoves(whitePiece.pieceName, whitePiece.piecePosition)) 
            takesKing = ("x" + bKing.piecePosition)
            for eachWhiteMove in allWhiteMoves:
                if type(eachWhiteMove) == list :
                    for everyWhiteMove in eachWhiteMove:
                        if everyWhiteMove != "":
                            if takesKing in everyWhiteMove:
                                i += 1
                                blackIsInCheck = True
                        
        if i == 0:
            blackIsInCheck = False
        else:
            print("black is still in check")
            blackIsInCheck = True
            

         
    if(whoseTurn == "black" or whiteIsInCheck == True):
        i = 0  
        for blackPiece in blackPieces:
            allBlackMoves = []
            allBlackMoves.append(gatherPossibleMoves(blackPiece.pieceName, blackPiece.piecePosition)) 
            takesKing = ("x" + wKing.piecePosition)
            for eachBlackMove in allBlackMoves:
                if type(eachBlackMove) == list :
                    for everyBlackMove in eachBlackMove:
                        if everyBlackMove != "":
                            if takesKing in everyBlackMove:
                                i += 1
                                whiteIsInCheck = True
        if i == 0:
            whiteIsInCheck = False
        else:
            whiteIsInCheck = True

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
wKnight1 = Piece("wN", "b1")
wKnight2 = Piece("wN", "g1")
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
bKing = Piece("bK", "e8")
bQueen = Piece("bQ", "d8")
bRook1 = Piece("bR", "h8")
bRook2 = Piece("bR", "a8")
bKnight1 = Piece("bN", "g8")
bKnight2 = Piece("bN", "b8")
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
#moves storage
allWhiteMoves = []
allBlackMoves = []
#row and rank
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank = ['1', '2', '3', '4', '5', '6', '7', '8']
#turn etc
turnNumber = 1.0
whoseTurn = "white"
#check
whiteIsInCheck = False
whiteIsStillInCheck = False
blackIsInCheck = False
blackIsStillInCheck = False
#quit conditions
whiteIsCheckMated = False
blackIsCheckMated = False
userQuit = False

#main program
instructions()

#dictionary test


#here starts the turn loop
while whiteIsCheckMated == False and blackIsCheckMated == False and userQuit == False:
    legalMoves = False
    moveCondition = False
    print("Move number " + str(turnNumber) + ". It is " + whoseTurn + "'s turn.")
    print()
    drawBoard()

    while(moveCondition == False and userQuit == False):
        while legalMoves == False:
            possibleMoves = []
            #if in check print this
            if whiteIsInCheck == True or blackIsInCheck == True:
                print("You are in check. You must move your king or block the check. Type 'q' to Quit")
            else:
                print("Your turn. Select a piece move, or type 'q' to Quit")
            squareMoveFrom = input("Which square is the piece you want to move on?:")
            if squareMoveFrom == 'q':
                print("Thanks for playing!")
                userQuit = True
                break
            for eachPiece in allPieces:
                whoseTurnLetter = whoseTurn[0]
                pieceColor = eachPiece.pieceName[0]
                if whoseTurnLetter == pieceColor:
                    if eachPiece.piecePosition == squareMoveFrom:
                        possibleMoves = gatherPossibleMoves(eachPiece.pieceName, eachPiece.piecePosition)
                        if possibleMoves:
                            print("This piece can move to these squares: (enter 'c' to change pieces) ")
                            print(possibleMoves)
                            legalMoves = True
                            break
                        else:
                            print("That piece has no legal moves.")
                    else:
                        continue
            if legalMoves == False:
                print()
        #Gets input on which square to move to, or starts loop over with 'c'
        if userQuit != True:
            squareMoveTo = input("Which square would you like to move it to? (or enter 'c' to choose another piece) : ")
            if squareMoveTo == 'q':
                print("Thanks for playing!")
                userQuit = True
                break
            if squareMoveTo == 'c':
                print("Please choose another piece")
                print()
                moveCondition = False
                legalMoves = False
                continue
            if squareMoveTo in possibleMoves:
                if "x" in squareMoveTo:
                    squareMoveTo = squareMoveTo.split("x")
                    squareMoveTo = squareMoveTo[1]
                    takeAPiece(squareMoveTo)
                if whiteIsInCheck == True or blackIsInCheck == True:
                    oldPiecePosition = eachPiece.piecePosition
                eachPiece.piecePosition = squareMoveTo
                #check for checks
                if whiteIsInCheck == True or blackIsInCheck == True:
                    checkChecker()
                    if(whiteIsInCheck == True):
                        print()
                        print("That move did not get you out of check. You must stop check.")
                        eachPiece.piecePosition = oldPiecePosition
                        break
                    elif(blackIsInCheck == True):
                        print()
                        print("That move did not get you out of check. You must stop check.")
                        eachPiece.piecePosition = oldPiecePosition
                        break     
                    else:
                        print()
                        print("Here's an updated image of the board.")
                        moveCondition = True    
                else:
                    checkChecker()
                    if(whiteIsInCheck == True):
                        print("White is in check")
                    if(blackIsInCheck == True):
                        print("Black is in check")
                    #in gatherPossibleMoves add in a check checker to see if you can move any piece except king
                    print()
                    print("Here's an updated image of the board.")
                    moveCondition = True
            else:
                print("That move is not a legal move. Please select from the options listed.")
    if legalMoves == True and moveCondition == True:
        flipTurn()
        turnNumber += .5