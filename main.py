from RockPaperCissors import RPSGame


if __name__ == '__main__':
    selections = ["1", "2", "3"]
    while True:
        selection = input("Enter a number between 1, 2 or 3 to pick a game: ")
        if selection not in selections:
            print("Invalid input. Please pick a number between 1, 2 or 3")
        elif selection == "1":    
            print("you have selected Rock Paper Cissors game!")
            RPSGame()
        elif selection == "2": 
           print("you have selected Tic Tac Toe game!")
           break
        else:
           print("you have selected Number Guess game!")
           break    
        
