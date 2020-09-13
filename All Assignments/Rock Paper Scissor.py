#!/usr/bin/env python
# coding: utf-8

# In[1]:


def TakePlayerInput():
    player = "blank"
    while not( player.lower() == "r" or player.lower() == "p" or player.lower() == "s") :
        player = input("Enter your input (R | P | S) - ")
    return player.lower()


# In[2]:


TakePlayerInput()


# In[3]:


import random 

def GetBotInput():
    lst = ['r','s','p']
    return random.choice(lst)


# In[4]:


GetBotInput()


# In[5]:


def CheckWinner(player,bot):
    if player == 'r' and bot == "r":
        return "draw"
    elif player == "r" and bot == "p":
        return "bot"
    elif player == "r" and bot == "s":
        return "player"
    elif player == "p" and bot == "s":
        return "bot"
    elif player == "p" and bot == "r":
        return "player"
    elif player == "p" and bot == "p":
        return "draw"
    elif player == "s" and bot == "r":
        return "bot"
    elif player == "s" and bot == "p":
        return "player"
    elif player == "s" and bot == "s":
        return "draw"
    else:
        return "draw"


# In[6]:


CheckWinner(player = "r",bot = "s")


# In[7]:


def RockPaperScissor():
    EndTheGame = "n"
    Player_Score = 0 
    Bot_Score = 0
    while EndTheGame.lower() != "y":
        ply = TakePlayerInput()
        bt = GetBotInput()
        print('Bot Entered - ', bt)
        print(" ")
        winner = CheckWinner(player = ply, bot = bt)
        print(" Winner is - ", winner)
        print(" ")
        if winner == "player":
            Player_Score += 2
        elif winner == "bot":
            Bot_Score += 2
        else :
            Player_Score += 1
            Bot_Score += 1
            
        print("---SCORE BOARD---")
        print("Player - ",Player_Score)
        print("Bot - ",Bot_Score)
        print(" ")
        EndTheGame = input("You want to end Y/N - ")


# In[8]:


RockPaperScissor()


# In[ ]:




