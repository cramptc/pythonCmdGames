import random

file = open("Bulls and Cows Playcount","a")

def Intro():
    print("Welcome to Bulls and Cows; a fun isogram game for people of all ages.")
    print("Choose a difficulty and try to find the word in the least number of guesses.")
    print("The difficulties are 4, 10, 12 and 14 letters")

def Setup():
    Diff = int(input("What difficulty do you want to play?: "))
    FourLetters = ["bold","hola","play","bald","dang","four","quiz","trio","ring",
                   "meal","your","sold","told","cold","shoe","bolt"]
    TenLetters = ["aftershock", "artichokes","authorizes","background","bankruptcy",
                 "binoculars","blackhorse","blacksmith","boyfriends","campground",
                 "clothespin","complaints","conjugated","copyrights","despicably",
                 "destroying","downstrea m","dumbwaiter","duplicates","farsighted",
                 "formidable","godparents","graciously","greyhounds","hospitable",
                 "importance","infamously","introduces","judgmental","juxtaposed",
                 "lawrencium","lumberjack","malnourish","mistakenly","monarchist",
                 "nightmares","noticeably","pathfinder","phlegmatic","quadriceps",
                 "scunthorpe","shockingly","slumbering","trampoline","trapezoids",
                 "volkswagen","waveringly"]
    TwelveLetters = ["absorptively","ambidextrous",
                    "bankruptcies",
                    "configurated",
                    "considerably",
                    "demographics",
                    "demonstrably",
                    "exclusionary",
                    "exculpations",
                    "exhaustingly",
                    "flowcharting",
                    "gunpowderish",
                    "housewarming",
                    "hypnotizable",
                    "lexicography",
                    "malnourished",
                    "metalworking",
                    "misconjugate",
                    "overhaulings",
                    "packinghouse",
                    "questionably",
                    "recognizably",
                    "recognisably",
                    "thunderclaps",
                    "unforgivable",
                    "unforgivably",
                    "unprofitable",
                    "unprofitably",
                    "upholstering"]
    FourteenLetters = [ "ambidextrously",
                        "computerizably",
                        "croquet-playing",
                        "dermatoglyphic",
                        "hydromagnetics",
                        "hydropneumatic",
                        "pseudomythical",
                        "subformatively",
                        "troublemakings",
                        "undiscoverably"]
    if Diff == 4:
        Word = random.choice(FourLetters)
    elif Diff == 10:
        Word = random.choice(TenLetters)
    elif Diff == 12:
        Word = random.choice(TwelveLetters)
    elif Diff == 14:
        Word = random.choice(FourteenLetters)
    else:
        print("That is not a valid choice.")
    return Word

def TestGuess(Word):
    turns = 15
    go = 0
    checka = 0
    checkb = 0
    bulls = 0
    cows = 0
    while go < turns:
        Guess = str(input("What is your guess?: "))
        if Guess == "Admin":
            print(Word)
            print("\n"*100)
        elif Guess == Word:
            print("Well Done! You guessed the word.")
            return go
        elif Guess == "\h":
            print("The first letter is a", Word[0])
        else:
            if len(Guess) == len(Word):
                while checka < len(Word):
                    while checkb < len(Word):
                        if Word[checka] == Guess[checkb] and checka == checkb:
                            bulls += 1
                        elif Word[checka] == Guess[checkb]:
                            cows += 1
                        #print("checkb",checkb)
                        checkb += 1
                    checkb = 0
                    #print("checka",checka)
                    checka += 1
                go += 1
                print("You have",bulls,"bulls and",cows,"cows with the word",Guess)
                bulls = 0
                cows = 0
                checka = 0
                checkb = 0
            else:
                print("You've got it wrong, retry")
        if go == 15:
            print("You have run out of turns, the word was", Word)
            return go
                

Intro()
name = str(input("What's your name? "))
TestGuess(Setup())
file.write(name," ",go,"\n")
