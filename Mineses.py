#RULES

print("This game is called mines and is designed to test your memory. "
      "The object is to reach the end in as few moves as possible. "
      "To do this you will choose where to go. "
      "If that space has a mine then you will be sent back to the beginning but if it is clear then you move to that space and guess the next row. It will count everytime you are sent back"
      "If at any point you are stuck, type 'help' or 'h' and you will recieve 1 of 3 hints.")



#SETUP

o = 0
board = [[o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],
         [o,o,o,o],]

coordx = 0
coordy = []
kden = 0
helps = 0
bru = 0
diff = ["Easy","Medium","Hard","Custom"]
al = 0

print(board[0])
print(board[1])
print(board[2])
print(board[3],"- Easy")
print(board[4])
print(board[5],"- Medium")
print(board[6])
print(board[7],"- Hard")
print(board[8])
print(board[9])
print(board[10])
print(board[11])
print(board[12])
print(board[13])
print(board[14])
print(board[15])
print(board[16]) 
print(" |  |  |  |")
print(" 1, 2, 3, 4 ")





#Random numbers

import random

rng = random.Random()

for a in range(19):
    a = rng.randrange(0,4)
    coordy.append(a)

for safeplc in coordy:
    board[coordx][safeplc] = "s"
    coordx += 1
    




#DIFFICULTY

wdiff = int(input("What difficulty (Easy - [1], Medium - [2], Hard - [3], Custom - [9-18])? "))
wdiff -= 1

if wdiff == 0:
    al = 0
    d = 4
elif wdiff == 1:
    al = 1
    d = 6
elif wdiff == 2:
    al = 2
    d = 8
else:
    d = wdiff
    al = 3





    
#PLAY

pcoordx = 0
pcoordy = 0
resetc = 0

while pcoordx < d:
    pcoordy = input("Where? ")
    if pcoordy == "help" or pcoordy == "h":
        if helps >= 0:
            print("You have used too many helps")
        else:
            print(board[pcoordx])
            helps += 1
    else:
        if int(pcoordy) < 1 or  int(pcoordy) > 4:
            print("Out of range")
        else:
                pcoordy = int(pcoordy)
                pcoordy -= 1
                if board[pcoordx][pcoordy] == "s":
                    print("Safe")
                    pcoordx += 1
                else:
                    print("\n"*100)
                    print("Mine")
                    resetc += 1
                    print("Reset count =", resetc)
                    pcoordx = 0




#FINALE

print("")
print("")
print("WELL DONE, you won in",resetc,"resets and",helps,"helps on",diff[al],"difficulty")
print("")
print("This was the route:")

for zzz in range(15):
    print(board[bru])
    bru += 1




