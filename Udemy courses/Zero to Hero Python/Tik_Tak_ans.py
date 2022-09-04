
r1 = ['1','2','3']


def print_board(r1):
    print(r1)

r2 = ['4','5','6']
r3 = ['7','8','9']


def user_choice():
    u_choice = "wrong"
    #Repeats till broken with return statement
    while True:
        #Check if choice is an digit
        if u_choice.isdigit():
            #Checks if digit is in range
            if int(u_choice) in range(1,4):
                #Breaks out of loop
                return int(u_choice) - 1
            else:
                #Sets choice again if digit out of range
                u_choice = input("Number between 1 and 9 ")
        else:
            #Sets choice again if choice wasn't a digit
            u_choice = input("Number between 1 and 9 ")
        
def replacement_choice(board,position):
    user_placement = input("Type a string to place ")
    board[position] = user_placement
    return board

def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:

        choice = input("Keep playing? (Y or N)").upper()

        if choice not in ["Y","N"]:
            print("Invalid Choice")

    if choice =="Y":
        return True
    else:
        print("Thanks for playing")
        return False

game_on = True

while game_on:
    print_board(r1)

    r1 = replacement_choice(r1,user_choice())
    print_board(r1)

    game_on = gameon_choice()


