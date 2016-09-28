#This is my first attempt at writing a dice rolling simulator 
#using one six sided die
import random

def OneDie(roll):
    
    rollAgain="yes"
    
    while rollAgain=="yes":
        
        print("Okay, rolling!")
        
        
        print( "The die is " + str(random.randint(1,6)))
        
        rollAgain = input("Would you like to roll again? ")
        
    return "Goodbye!"

def TwoDie(roll):
    
    rollAgain="yes"
    
    diceValue=[]
    values=[1,2,3,4,5,6]
    
    while len(diceValue)<2:
        
        random.shuffle(values)
        
        diceValue.append(random.choice(values))
        diceValue.append(random.choice(values))
    
    while rollAgain=="yes":
        
        print("Okay, rolling the die!")
        
        print("The die is " + str(diceValue))
            
        rollAgain=input("Would you like to roll again? ")
        
    
    
    
    
    
        
        
        
        
    
    