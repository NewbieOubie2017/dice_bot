import random

def rollDice(cnt):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    x = int(die1 + die2)
    print('Roll #', cnt, 'was', x)
    return x
'''
def total_bank(bank):
    bet = 0
    print('You have ${} in your bank.'.format(bank))
    bet = input('Enter your bet (or 0 to quit): ')
    bet = int(bet)
    while bet < 0 or bet > min([500,bank]):
        total_bank(bank)    
    if bet == 0: 
        print('Thanks for playing!')
        exit()
    return bank, bet

def get_guess():
    guess = 0
    while (guess < 2 or guess > 12):    
        try:
            guess = int(input('Choose a number between 2 and 12: '))
            #print("\n{}\n".format(guess))
        except ValueError:
            guess = 0
    if (guess >= 2 and guess <= 12): 
        return guess
'''
#prog_info()
bank = 500
#guess = get_guess()
rcnt = 1

while rcnt < 4:
    print('You now have ${} in your bank.'.format(bank))
    rcnt = 0
    guess = 7
    bet = 50  # total_bank(bank) # this function returns two variables
    if guess == rollDice(rcnt+1):
        bank += bet * 2
    elif guess == rollDice(rcnt+2):
        bank += bet * 1.5
    elif guess == rollDice(rcnt+3):
        bank = bank
    else:
        bank = bank - bet
        if bank == 0:
            print('You went bust! : > (')
            print('Thanks for playing!')
            exit()
        elif bank >= 1000:
            print('You Broke the bank : > }')
            print('You now have ${} in your bank.'.format(bank))
            print('Thanks for playing!')
            exit()

