import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

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

FourByFour = [
				None,[0,38],[0,39],[0,40],[0,41],[1,38],[1,39],[1,40],[1,41],
			 	[2,38],[2,39],[2,40],[2,41],[3,38],[3,39],[3,40],[3,41]
			 ]

j = 0
#run whenever new tile occurs or on spin
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

NewFour = getPositions(tileFive, 0)
#print(NewFour)
while True: #to the end of while statement represents one tile
    j += 1
    #NewFourByFour = FourByFour[:]

    next_key = w.getch()
    if next_key == curses.KEY_END:
        curses.endwin()
        quit()
    #if (j == 9):
    #	tileOne.spinRight()
    for i in range(0, 4):
    	w.addch(NewFour[i][0] + j - 1, NewFour[i][1], ' ')
    for i in range(0, 4):
    	w.addch(NewFour[i][0] + j, NewFour[i][1], curses.ACS_CKBOARD)
