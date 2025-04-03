import time
import random
import math

# The board for the game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Function to display the board
def display_board(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Function to check if any player has won
def winner(board):
    # Checking rows
    for i in [0, 3, 6]:
        if board[i] == board[i+1] == board[i+2] != "-":
            return board[i]
        
    # Checking columns
    for i in [0, 1, 2]:
        if board[i] == board[i+3] == board[i+6] != "-":
            return board[i]
        
    # Checking diagonals
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]
    
    # Checking if the game is a tie
    if "-" not in board:
        return "tie"
    
    # If no one has won and the game is not a tie, return None
    return None


# Minimax algorithm with alpha-beta pruning
# TODO: Implement the minimax algorithm with alpha-beta pruning
def minimax(board, alpha, beta, maxLayer, minLayer):
    
    if winner(board):
    
        if winner(board) == "X":
            return -1

        elif winner(board) == "O":
            return 1
    
        elif winner(board) == "tie":
            return 0
         
    if maxLayer:
    
        maxVal = -math.inf
    
        for i in range(9):
    
            if board[i] == "-":
                
                board[i] = "O"
                recursiveCallsResult = minimax(board, alpha, beta, False, True)
                board[i] = "-"
                
                maxVal = max(maxVal, recursiveCallsResult)
                alpha = max(alpha, recursiveCallsResult)
                
                if alpha >= beta:
                    break
    
        return maxVal
        
    if minLayer:
    
        minVal = math.inf
    
        for i in range(9):
    
            if board[i] == "-":
                
                board[i] = "X"
                recursiveCallsResult = minimax(board, alpha, beta, True, False)
                board[i] = "-"
                
                minVal = min(minVal, recursiveCallsResult)
                beta = min(beta, recursiveCallsResult)
                
                if alpha >= beta:
                    break
    
        return minVal
    
# Function to find the best computer's move using minimax with alpha-beta pruning
# TODO: Implement the function to find the best computer's move using minimax with alpha-beta pruning
def computer_move(board):
    
    bestMove = -math.inf
    moveToMake = None
    
    for i in range(9):
    
        if board[i] == "-":
            
            board[i] = "O"
            currMove = minimax(board, -math.inf, math.inf, False, True)
            board[i] = "-"
            
            if currMove > bestMove:
    
                bestMove = currMove
                moveToMake = i
                
    return moveToMake


# Main function to run the game
def main():
    current_player = "X"

    while True:
        # Displaying the board
        display_board(board)
        
        # Checking if the game has ended
        if winner(board) == "tie":
            print("The game has ended in a tie.")
            break
        elif winner(board) == "X":
            print("Congratulations! You have won the game.")
            break
        elif winner(board) == "O":
            print("The computer has won the game.")
            break
        
        if current_player == "X":
            # Getting the user's move
            while True:
                try:
                    user_move = int(input("Enter your move (1-9): ")) - 1
                    if user_move in range(9) and board[user_move] == "-":
                        board[user_move] = "X"
                        break
                    else:
                        print("Invalid move. Try again.")
                except:
                    print("Invalid move. Try again.")
                    
            current_player = "O"
        else:
            # Getting the computer's move
            print("The computer is thinking...")
            time.sleep(0.5) # Sleep for suspense

            computer = computer_move(board)
            board[computer] = "O"
            current_player = "X"

if __name__ == "__main__":
    main()
