# Program will play rock paper scissors with the user
# 11/11/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Jacob White
# Import random
# define randomnumber function
# define computer choice function
# define user choice function, get user input
# define determine winner function
# define restart function
# define main, display output
import random

def generateRandomNumber():
    randomNumber = random.randint(1,3)
    return randomNumber

def getComputerChoice(randomNumber):
    if randomNumber == 1:
        computerChoice = 'rock'
    elif randomNumber == 2:
        computerChoice = 'paper'
    elif randomNumber == 3:
        computerChoice = 'scissors'

    return computerChoice

def getUserChoice():
    userChoice = input('Please enter your choice: ')
    return userChoice

def determineWinner(computerChoice, userChoice):
    rock = 'The rock smashes the scissors'
    scissors = 'Scissors cuts paper'
    paper = 'Paper covers rock'
    winner = 'no winner'
    message = ''

    if computerChoice == 'rock' and userChoice == 'scissors':
        winner = 'Computer'
        message = rock
    elif computerChoice == 'scissors' and userChoice == 'rock':
        winner = 'You'
        message = rock
    if computerChoice == 'scissors' and userChoice == 'paper':
        winner = 'Computer'
        message = scissors
    elif computerChoice == 'paper' and userChoice == 'scissors':
        winner = 'You'
        message = scissors
    if computerChoice == 'paper' and userChoice == 'rock':
        winner = 'Computer'
        message = paper
    elif computerChoice == 'rock' and userChoice == 'paper':
        winner = 'You'
        message = paper

    return winner, message

def restart():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print( 'The computer chose', computerChoice)
    winner, message = determineWinner(computerChoice, userChoice)

    if winner != 'no winner':
        print(winner, 'won(', message, ')')

    return winner

def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print()
    print( 'The computer chose', computerChoice)
    print()
    winner, message = determineWinner(computerChoice, userChoice)

    if winner != 'no winner':
        print(winner, 'won(', message, ')')

    while winner == 'no winner':
        print('You both chose the same thing')
        winner = restart()

main()

        
    
        
    
    
