#!/usr/bin/env python
# coding: utf-8

# In[6]:


## So this one is going to be an exercise in using dictionaries
## You can basically set a dictionary of keys linked to specific values (So A --> B)
## To create, you can use dict([(A,B),(C,D)]) or dict(A=B,C=D) or just {A:B,C:D}
## Ex:
bear = {"speed":40,"height":"7-8ft"}
print(bear["speed"])
print("^ returned 40 because we asked for what 'speed' was in the bear dict")


# In[8]:


## To avoid an error from incorrect calls, you can instead use .get(<key>,<default value>)
print(bear.get("color","no color registered"))


# In[ ]:


## To add more, you can just set new pairs: bear["color"] = brown
## To remove a combo, you can use .pop(<key>,<default value>)
## You can also directly look at keys in loops, ex. for key in bear:...


# In[15]:


## Onto the actual exercise...
## For this, we have to make an inventory system that can go up or down in value depending on
## how many of the item we have, and should be able to return how many we have stored.
inventory = ["blisterPack","blisterPack","blisterPack","boosterBox","boosterBox","starterDeck","starterDeck","starterDeck","starterDeck"]
inventory_Count = {}

def create_inventory(stock):
    for item in stock:
        inventory_Count[item] = inventory_Count.get(item,0) + 1

create_inventory(inventory)
print(inventory_Count)


# In[16]:


## We also need a way to add to our inventory
def add_inventory(new_stock):
    for item in new_stock:
        inventory_Count[item] = inventory_Count.get(item,0) + 1
    new_Stock.clear()

new_Stock = ["blisterPack","blisterPack","blisterPack","blisterPack","playmat","playmat"]
add_inventory(new_Stock)
print(inventory_Count)


# In[20]:


## What if we sell some stuff? Remove items from the inventory!

## The big key thing I had to figure out here was not just removing items, but making sure that
## items we don't have in stock don't break the system. So they need to be added to our inventory
## and if they go below 0, set the stock to 0 instead

def sell_inventory(sold_stock):
    for item in sold_stock:
        if item in inventory_Count:
            inventory_Count[item] = inventory_Count.get(item,0) - 1
            if inventory_Count.get(item) == -1:
                inventory_Count[item] = 0
        else:
            inventory_Count[item] = 0
    sold_Stock.clear()

sold_Stock = ["blisterPack","blisterPack","playmat","boosterBox", "diceTray"]
sell_inventory(sold_Stock)
print(inventory_Count)


# In[21]:


## Now we need to be able to remove an item from our system entirely

def remove_inventory(removed_stock):
    for item in removed_stock:
        if item in inventory_Count:
            inventory_Count.pop(item)
        else:
            return
        removed_stock.clear

removed_Stock = ["diceTray","diceSet"]
remove_inventory(removed_Stock)
print(inventory_Count)


# In[25]:


## The last thing this exercise wants is a function to show our inventory... I guess that's not
## just the print outputs we've been using? Should be easy

def show_inventory():
    print("Current inventory:")
    for item in inventory_Count:
        print("name: " + str(item) + "     Quantity: " + str(inventory_Count.get(item)))

show_inventory()


# In[ ]:




