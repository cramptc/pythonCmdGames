#RULES
print("This game is called mines and is designed to test your memory. "
      "The object is to reach the end in as few moves as possible. "
      "To do this you will choose where to go. "
      "If that space has a mine then you will be sent back to the beginning but if it is clear then you move to that space and guess the next row. It will count everytime you are sent back")






#SETUP


#defenitions
boardlength = int(input("How long do you want the board?: "))
boardwidth = int(input("How wide do you want it to be? (2 = easy, 4 = medium, 6 = hard, 8 = tryhard): "))
o = 0
ylist = []
inum = 1
coordx = 0
coordy = []
backcount = 0
rlboard = []
xlist = []
jnum = 1
bwc = 0
win = 0
ting = 0


#def board w/ specs
board = []

#coordx def

if boardwidth == 2:
    endboardwidth = [o,o]
elif boardwidth == 4:
    endboardwidth = [o,o,o,o]
elif boardwidth == 6:
    endboardwidth = [o,o,o,o,o,o]
elif boardwidth == 8:
    endboardwidth = [o,o,o,o,o,o,o,o]                                # Remeber x = board width, y = board length
else:
    print("")
    print("YOU MUST CHOOSE ONE OF THE GIVEN DIFFICULTY LEVELS!!!!!")
    quit()

for z in range(boardlength):
    xlist.append("x"+("j"*jnum))
    

for zzz in xlist:
    board.append(endboardwidth)

#coordy def

for zz in range(len(board)):
    ylist.append("y"+("i"*inum))
    inum += 1

#random numbers
import random

rng = random.Random()

for a in ylist:
    a = rng.randrange(0,(boardwidth))
    coordy.append(a)

#Show board

'''for drawboard in range(0,boardlength):
    print(board[drawboard])'''
    
#placing safespace


for safeplc in coordy:
   board[coordx][safeplc] = 1
   coordx += 1
print(board)


    

#PLAY

'''while win == 0:
    checkmove = int(input("Where?"))'''































   





