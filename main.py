import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(500)

key = curses.KEY_RIGHT

from Tile import Tile

tileOne = Tile("O", [None, False, False, True, True, False, False, True,
						 True, False, False, False, False, False, False, False, False])
tileTwo = Tile("I", [None, False, False, True, False, False, False, True,
						False, False, False, True, False, False, False, True, False])
tileThree = Tile("T", [None, False, True, True, True, False, False, True,
						False, False, False, False, False, False, False, False, False])
tileFour = Tile("J", [None, False, True, True, True, False, False, False,
						  True, False, False, False, False, False, False, False, False])
tileFive = Tile("L", [None, False, True, True, True, False, True, False,
						  False, False, False, False, False, False, False, False, False])
tileSix = Tile("S", [None, False, False, True, True, False, True, True,
						  False, False, False, False, False, False, False, False, False])
tileSeven = Tile("Z" , [None, False, True, True, False, False, False, True,
						  True, False, False, False, False, False, False, False, False])

CurrentTile = tileThree

FourByFour = [
				None,[0,38],[0,39],[0,40],[0,41],[1,38],[1,39],[1,40],[1,41],
			 	[2,38],[2,39],[2,40],[2,41],[3,38],[3,39],[3,40],[3,41]
			 ]
ActPos = [
			[21, 35], [21, 36], [21, 37], [21, 38], [21, 39], 
			[21, 40], [21, 41], [21, 42], [21, 43], [21, 44]
		]
for i in range(0, 9):
	w.addch(ActPos[i][0], ActPos[i][1], curses.ACS_CKBOARD)

j = 0
#run whenever new tile occurs or on spin
def moveRight(theTile, j):
		for i in range (0, 4):
			w.addch(NewFour[i][0] + j, NewFour[i][1], ' ')
		for i in range (0, 4):
			NewFour[i][1] += 1
			w.addch(NewFour[i][0] + j, NewFour[i][1], curses.ACS_CKBOARD)
def moveLeft(self):
		for i in range (0, 4):
			NewFour[i][1] += 1
		for i in range (0, 4):
			NewFour[i][1] = NewFour[i][1] - 1


def getPositions(theTile, j):
	TCounter = 0
	NewFour = [[0, 0],[0, 0],[0, 0],[0, 0]]
	for i in range(1, 17): #take four positions and make array
		    if theTile.shape[i] == True and TCounter < 4:
		    	NewFour[TCounter][0] = FourByFour[i][0] + j
		    	NewFour[TCounter][1] = FourByFour[i][1]
		    	TCounter += 1
		    	#w.addch(FourByFour[i][0] + j - 1, FourByFour[i][1], ' ')
	return NewFour

NewFour = getPositions(CurrentTile, 0)
#print(NewFour)
check = False
while check == False: #to the end of while statement represents one tile
    j += 1
    #NewFourByFour = FourByFour[:]

    next_key = w.getch()
    if next_key == curses.KEY_END:
        curses.endwin()
        quit()
    if next_key == curses.KEY_RIGHT:
    	moveRight(CurrentTile, j)
    if next_key == curses.KEY_UP:
    	CurrentTile.spinRight()
    	for i in range(0, 4):
    		w.addch(NewFour[i][0] + j - 1, NewFour[i][1], ' ')
    	NewFour = getPositions(CurrentTile, 0)
    if next_key == curses.KEY_DOWN:
    	CurrentTile.spinLeft()
    	for i in range(0, 4):
    		w.addch(NewFour[i][0] + j - 1, NewFour[i][1], ' ')
    	NewFour = getPositions(CurrentTile, 0)	
    for i in range(0, 4):
    	w.addch(NewFour[i][0] + j - 1, NewFour[i][1], ' ')
    for i in range(0, 4):	
    	w.addch(NewFour[i][0] + j, NewFour[i][1], curses.ACS_CKBOARD)
    for i in range(0, 4):
    	for x in range(0, len(ActPos) - 1):
    		if NewFour[i][0] + j == ActPos[x][0] and NewFour[i][1] == ActPos[x][1] :
    			check = True
    			for i in range(0, 4):
    				w.addch(NewFour[i][0] + j - 1, NewFour[i][1], curses.ACS_CKBOARD)
    #if check != True:		
    #	w.addch(NewFour[i][0] + j, NewFour[i][1], curses.ACS_CKBOARD)
