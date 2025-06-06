#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Here we're following an exercise of using booleans by making code from Pac-Man
# I'll space out each question into its own block for the sake of our work here


# In[2]:


# 1. Define if Pac-Man eats a ghost (if power pellet active and he touches a ghost, return boolean value)
def eat_ghost(pellet_active, touching_ghost):
    if pellet_active == True and touching_ghost == True :
        return True
    else:
        return False


# In[3]:


# 2. Define if Pac-Man scores (if touching a dot or power pellet, return boolean value)
def gain_score(touching_pellet, touching_dot):
    if touching_pellet == True or touching_dot == True :
        return True
    else:
        return False


# In[4]:


# 3. Define if Pac-Man loses (if touching a ghost without pellet active, return boolean value)
def pacman_death(pellet_active, touching_ghost):
    if pellet_active == False and touching_ghost == True :
        return True
    else:
        return False


# In[5]:


# 4. Define if Pac-Man wins (if eaten all the dots and has not lost, return boolean value)
# It also says to add if the pellet is active, I'm assuming to test that we know how to use it
def pacman_win(all_dots_eaten, pellet_active, touching_ghost):
    if all_dots_eaten == True and touching_ghost == False:
        return True
    elif all_dots_eaten == True and touching_ghost == True and pellet_active == True:
        return True
    else:
        return False


# In[9]:


# With that, the website's lesson ends, but let's actually test out our code
# First we have to set up our variables at the start of the game
all_dots_eaten = False
touching_ghost = False
pellet_active = False
touching_dot = False
touching_pellet = False


# In[10]:


# So lets say the game is going, and I got trapped and a ghost just caught me first...
touching_ghost = True
print("Pac-Man dies?: " + str(pacman_death(pellet_active, touching_ghost)))


# In[11]:


# Oh nice that worked, ok lets try seeing if we score some points
# First let me reset the ghost check
touching_ghost = False

touching_dot = True
print("Did we score some points?: " + str(gain_score(touching_pellet, touching_dot)))


# In[13]:


# Awesome! Last one let's try to really mess with the win conditions
# First reset as usual
touching_dot = False

# First will be if we just cleared the board, no ghost touching
# Then a ghost will hit us on the same frame as we clear the board
# Finally, we'll have a power pellet active when we get hit
all_dots_eaten = True
print("Did we win?: " + str(pacman_win(all_dots_eaten, pellet_active, touching_ghost)))

touching_ghost = True
print("Did we win?: " + str(pacman_win(all_dots_eaten, pellet_active, touching_ghost)))

pellet_active = True
print("Did we win?: " + str(pacman_win(all_dots_eaten, pellet_active, touching_ghost)))


# In[ ]:




