import random

#!Rock, Paper, Scissors Game
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choice = {"player" : player_choice, "computer" : computer_choice}

    return choice

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    
    #! Nested elif statement
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
        
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
        
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cutes paper! You win!"
        else:
            return "Rock smashes scissors! You lose"

#* This wil call the function
choices = get_choices()
result = check_win(choices["player"], choices["computer"])  
print(result)


#! Notes
#! Functions
# def example():
#     return "This is an example"
    
#! Variables 
#player_choice = "rock"
#computer_choice = "paper"

#! f-strings or simple concatenation strings
#age = 25
#print(f"Jim is {age} years old")
#! Dictionaries in Python or Objects. It uses key value pairs
# dict = {"name": "beau", "color" : choices}
 
 #* to choose a key value inside of the dictionary
 # # p_choices = dict["name"]

#! Lists or arrays inside of python
#food = ["pizza", "carrots", "eggs"]

#! using import random library inside of lists
#dinner = random.choice(food)
#print(dinner)

#! Logical Statements
#* IF ELSE
# age = 20 
# if age >=18:
#     print("You are an adult")
# elif age > 12:
#     print("You are a teenager")
# elif age > 1 :
#     print("You are a child")
# else:
#     print("You are a baby")    
 
    