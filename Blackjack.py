import random
plali = []
cpuli = []

A = 1
J = 11
Q = 12
K = 13

number = [A,2,3,4,5,6,7,8,9,10,J,Q,K]
suits = ["H","S","C","D"]

def choosecards():
    plali.append((random.choice(number),random.choice(suits)))
    plali.append((random.choice(number),random.choice(suits)))
    cpuli.append((random.choice(number),random.choice(suits)))
    cpuli.append((random.choice(number),random.choice(suits)))

choosecards()
print(plali,cpuli)
    
