from termcolor import colored

'''
Project: Tic Tac Toe

This program uses Python to create an engine which is unbeatable at Tic Tac Toe.
Users will be able to play Tic Tac Toe against the engine, while the engine plays to win, or the worst case scenario being a draw.
This project makes uses of Artificial Intelligence.
'''

board = {'1': colored(1, 'blue'), '2': colored(2, 'blue'), '3': colored(3, 'blue'),
         '4': colored('4', 'blue'), '5': colored('5', 'blue'), '6': colored('6', 'blue'), 
         '7': colored('7', 'blue'), '8': colored('8', 'blue'), '9': colored('9', 'blue')}

# def printExampleBoard():
#   print('1' + ' | ' + '2' + ' | ' + '3')
#   print('–' + ' | ' + '–' + ' | ' + '–')
#   print('4' + ' | ' + '5' + ' | ' + '6')
#   print('–' + ' | ' + '–' + ' | ' + '–')
#   print('7' + ' | ' + '8' + ' | ' + '9')

def printBoard(board):
  print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
  print('–' + ' | ' + '–' + ' | ' + '–')
  print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
  print('–' + ' | ' + '–' + ' | ' + '–')
  print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def isWinner(board, playerTurn):
  return (board['1'] == playerTurn and board['2'] == playerTurn and board['3'] == playerTurn) or (board['4'] == playerTurn and board['5'] == playerTurn and board['6'] == playerTurn) or (board['7'] == playerTurn and board['8'] == playerTurn and board['9'] == playerTurn) or (board['1'] == playerTurn and board['4'] == playerTurn and board['7'] == playerTurn) or (board['2'] == playerTurn and board['5'] == playerTurn and board['8'] == playerTurn) or (board['3'] == playerTurn and board['6'] == playerTurn and board['9'] == playerTurn) or (board['1'] == playerTurn and board['5'] == playerTurn and board['9'] == playerTurn) or (board['7'] == playerTurn and board['5'] == playerTurn and board['3'] == playerTurn)


def run():
  print('** TIC TAC TOE **')
  print('')
  print('Please select the mode you would like to play:')
  print('A/a: Play against another player')
  print('')
  userModeSelection = input('Please enter your selection: ')
  print('')
  if userModeSelection == 'A' or 'a':
    print('You have selected to play against another player!')
  print('')
  print('A board will be displayed, and you enter your mark (X or O) using the numbers on your keyboard.')
  print('This is how the grid would look like and these are the number associated with each spots:')
  print('')
  printBoard(board)
  print('')
  startGameInput = input('Please hit Enter to start the game')
  print('')
  playerTurn = 'X'
  if (startGameInput == ''):
    lookingForValidInput = True
    gameIsActive = True
    numRound = 1
    count = 1
    printBoard(board)
    while gameIsActive:
      print('-–––––––––––––––––––––')
      print('')
      print('Round ' + str(numRound))
      print('')

      while lookingForValidInput:
        try:
          userInput = int(input('Where would you like to move, player ' + playerTurn + '? '))
          print('')
          if board[str(userInput)] != 'X' and board[str(userInput)] != 'O':
            count += 1
            board[str(userInput)] = playerTurn
            printBoard(board)
            print('')
            if (isWinner(board, playerTurn)):
                print(colored('Player ' + playerTurn + ' has won the game!', 'green'))
                print('')
                gameIsActive = False
                break
            
            if playerTurn == 'X':
                playerTurn = 'O'
            else:
              playerTurn = 'X'

          else:
            print(colored('This spot is already taken, please try again!', 'red'))
            print('')
    

        except ValueError:
          print('')
          print(colored('That is not a valid spot to move to...Please try again!', 'red'))
          print('')

        if count == 10:
          gameIsActive = False
          break
    
    if count == 10:
      print(colored('Game has Tied!', 'yellow'))
      print('')
  
      

    



if __name__ == '__main__':
  run()