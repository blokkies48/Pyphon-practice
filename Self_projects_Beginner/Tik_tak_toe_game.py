from tkinter import Y


board1 = [1,2,3,4,5,6,7,8,9]
#Prints the board to console
def display_board(b1):
    
    s1 = ""
    i = 0
    for item in b1:
        s1 = s1 + " " + str(item)
        i += 1
        if i == 3:
            s1 = s1 + " ".join("\n")
        if i == 6:
            s1 = s1 + " ".join("\n")
    print(s1)
    

def user_choice():
    u_choice = "wrong"
    #Repeats till broken with return statement
    while True:
        #Check if choice is an digit
        if u_choice.isdigit():
            #Checks if digit is in range
            if int(u_choice) in range(1,10):
                #Breaks out of loop
                return int(u_choice) - 1
            else:
                #Sets choice again if digit out of range
                u_choice = input("Number between 1 and 9 ")
                

        else:
            #Sets choice again if choice wasn't a digit
            u_choice = input("Number between 1 and 9 ")
            

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:

        choice = input("Do you want to play? (Y or N)").upper()

        if choice not in ["Y","N"]:
            print("Invalid Choice")

    if choice =="Y":
        return True
    else:
        print("Thanks for playing")
        return False
	
def replacement_choice(board,position,player):
    if player == True:
        board[position] = "X"
        return board
    elif player == False:
        board[position] = "O"
        return board

def win_conditions(board,player):
    if player == True:
        return ((board[7] == "X" and board[8] == "X" and board[9] == "X") or # across the top
        (board[3] == "X" and board[4] == "X" and board[5] == "X") or # across the middle
        (board[0] == "X" and board[1] == "X" and board[2] == "X") or # across the bottom
        (board[6] == "X" and board[3] == "X" and board[0] == "X") or # down the middle
        (board[7] == "X" and board[4] == "X" and board[1] == "X") or # down the middle
        (board[8] == "X" and board[5] == "X" and board[2] == "X") or # down the right side
        (board[6] == "X" and board[4] == "X" and board[2] == "X") or # diagonal
        (board[8] == "X" and board[4] == "X" and board[0] == "X")) # diagonal
        
    else:
        return ((board[7] == "X" and board[8] == "X" and board[9] == "X") or # across the top
        (board[3] == "O" and board[4] == "O" and board[5] == "O") or # across the middle
        (board[0] == "O" and board[1] == "O" and board[2] == "O") or # across the bottom
        (board[6] == "O" and board[3] == "O" and board[0] == "O") or # down the middle
        (board[7] == "O" and board[4] == "O" and board[1] == "O") or # down the middle
        (board[8] == "O" and board[5] == "O" and board[2] == "O") or # down the right side
        (board[6] == "O" and board[4] == "O" and board[2] == "O") or # diagonal
        (board[8] == "O" and board[4] == "O" and board[0] == "O")) # diagonal
        

player1 = False


while True:
    game_on = gameon_choice()

    if game_on == True:
        board1 = [1,2,3,4,5,6,7,8,9]
        i = 0
        print("X turn")
    while game_on:
            
        display_board(board1)
        if i == 9:
            print("Draw")
            break
            
        if win_conditions(board1,player1) == True:
            print("Game over ")
            if player1 == True:
                print("X won")
            else:
                print("O won")
            break
                
        player_choice = user_choice()
        if board1[player_choice] != "X" and board1[player_choice] != "O":
            if player1 == True:
                print("X turn ")
                player1 = False
            elif player1 == False:
                print("O turn ")
                player1 = True
            i += 1
            
            replacement_choice(board1,player_choice,player1)
            
        else:
            print("position already taken")
                
        
    
    
    if game_on == False:
        print("Game Over!")
        break
    