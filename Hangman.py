import random

guessli = []
lives = 6
plat = "-"
platli = []
dif = 0
a = 0
wordli = [["a","i"],["to","at","it","hi","no","on"],["the","ate","red","you","wet","mud","don","hop"],["quad","trio","hola","your","stop","four","skis","snow","ruck","sack"],["short","lying","treat"]]



def setup():
    print("Welcome to hangman!")
    print("In hangman your victim has 6 body parts: head, torso, 2x arms, 2x legs.")
    print("You have to guess the letters in the word one by one.\n")
    
def choosedif():
    dif = int(input("How many letters?\n"))
    for i in range(dif):
        platli.append(plat)
    for i in platli:
        print(i, end=" ")
    print()
    return dif

    
def getguess():
    print("The letters you have used are:", guessli)
    guess = input("Your guess? \n")
    if 0 > len(guess) or len(guess) > 1:
        print("That isn't a single letter")
        getguess()
    else:
        if guess in guessli:
            print("You have already guessed this")
            getguess()
        else:
            guessli.append(guess)
            return guess

def checkwin():
    c = 0
    print(platli)
    for a in range(len(liword)):
        if liword[c] != platli[c]:
            return 0
        else:
            c += 1
    return 1
        

def checkguess(lives):
    if checkwin() == 1:
        print("Well done you have guessed the word!")
        return 1
    elif lives == 0:
        print("You have run out of lives.","The word was", word)
        return 1
    else:
        guess = getguess()
        if guess in word:
            print("That is a correct letter.")
            platli[word.find(guess)] = guess
        else:
            lives -= 1
            print("Thats not a correct letter. You now have",lives,"lives")
        return 0,lives
        
#Play
setup()
dif = choosedif()
word = random.choice(wordli[dif-1])
liword = list(word)
while a == 0:
    a = checkguess(lives)[0]
    
