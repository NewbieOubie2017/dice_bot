import random

def rollDice(cnt):
    win = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    x = int(die1 + die2)
    if cnt == 1: print('Roll #', cnt, 'was', x)
    if (cnt == 1 and x >3 and x < 11 and x != 7 and x != 11):
        print("That is your point to make.")
        win = 0
    elif ((cnt == 1) and (x == 7 or x == 11)):
        print("You win.")
        win = 1
    elif (cnt ==1):
        print("You lose.  : > ( CRAPS")
        win = -1
    if cnt > 1: print("roll is {}".format(x, win))
    return x, win


roll = 0
bank = 500
lowBank = 500
highBank = 500
print('You now have ${} in your bank.'.format(bank))
bet = 50 
while (bank > 0 and bank < 1000):
    win = 0
    makePoint, win = rollDice(1)
    while (win == 0):
        roll, win = rollDice(2)
        if makePoint == roll:
            bank += bet 
            win = 2
        elif roll == 7:  
            bank -= bet 
            win = 2
    if (win == 1): 
        bank += bet
    if (win == -1):
        bank -= bet
    if (bank < lowBank): lowBank = bank
    if (bank > highBank): highBank = bank

if bank == 0:
    print('You went bust! : > (')
    print("Your highest stake was {}".format(highBank))
    print('Thanks for playing!')
    exit()
elif bank >= 1000:
    print('You Broke the bank : > }')
    print('You now have ${} in your bank.'.format(bank))
    print("Your lowest stake was {}".format(lowBank))
    print('Thanks for playing!')
    exit()
else:
    print("Error?!")
    print('Thanks for playing!')
    exit()
