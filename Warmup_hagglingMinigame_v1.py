#!/usr/bin/env python
# coding: utf-8

# In[11]:


# So for this, I want to see if I can make a basic haggling game, in which you try to get
# the highest price for an item you're selling. We'll give the player and npc different stats
# that can affect how likely they are to take certain prices, and use random values as
# the prices you're trying to find.
item_value = 0
current_profit = 0
difficulty = 0
bid_value = False

import random

difficulty = random.random()
print("Difficulty: " + str(difficulty))

# This first function will give you an idea of the price of the object being appraised, but it will
# obscure the true value using some simple randomizations
def value_appraise(iValue, iDifficulty):
    if iDifficulty < 0.25:
        print("You feel a bid between " + str(iValue - (iValue*iDifficulty*(0.0625+random.random()))) + " and " + str(iValue + (iValue*iDifficulty*(0.0625+random.random()))) + " would be reasonable")
        print("You are quite confident of its value")
    elif iDifficulty >= 0.25 and iDifficulty <= 0.75:
        print("You feel a bid between " + str(iValue - (iValue*iDifficulty*(0.125+random.random()))) + " and " + str(iValue + (iValue*iDifficulty*(0.125+random.random()))) + " would be reasonable")
        print("You are somewhat confident of its value")
    elif iDifficulty > 0.75:
        print("You feel a bid between " + str(iValue - (iValue*iDifficulty*(0.1875+random.random()))) + " and " + str(iValue + (iValue*iDifficulty*(0.1875+random.random()))) + " would be reasonable")
        print("You are not very confident of its value")
    else:
        print("Something went wrong but idk what")

# I also need to be able to check if someone tries to input a value that is not a float when we expect one
def number_check(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Now for the actual game function itself. We want to keep track of a few things: Did you ask a low
# enough price for the customer to take it? Did you make money? And have you make enough money to
# win the game?
def haggle_minigame(iValue, cProfit):
    current_profit = cProfit
    while current_profit < 500:
        value_appraise(iValue, difficulty)
        bid_float_check = False
        while bid_float_check == False:
            bid_value = input("Enter your bid: ")
            if number_check(bid_value) == True:
                bid_float_check = True
                bid_value = float(bid_value)
                break
            else:
                print("That is not a valid bid")
        haggle_active = True
        while haggle_active == True:
            if bid_value <= float(iValue * 1.15):
                print("Oh, that's a perfectly fine price!")
                current_profit = current_profit + (bid_value - iValue)
                print("Current profits: " + str(current_profit))
                iValue = random.randint(1,500)
                haggle_active = False
            else:
                print("No no, that's far too much. Can't you go lower?")
                bid_float_check = False
                while bid_float_check == False:
                    bid_value = input("Enter your bid: ")
                    if number_check(bid_value) == True:
                        bid_float_check = True
                        bid_value = float(bid_value)
                        break
                    else:
                        print("That is not a valid bid")

# After making the code finally work how I want, I realize now that I could have condenced the
# "bid_float_check lines into its own function, as that came up a couple times and each time
# I ended up copying the exact same code.

# In future versions, it could be nice to have a "patience" system for the customers, where you have
# only a certain number of attempts at finding the right haggle price. For now I'm just happy I made
# this work in a reasonable way!


# In[13]:


item_value = random.randint(1,500)
print("Welcome to your new life as a shopkeep! Your job is to try and make $500 in profit")
print("People will bring you items for you to buy, so try and make your money with each sale")
print("Oh look, our first customer\n")
haggle_minigame(item_value, difficulty)


# In[ ]:




