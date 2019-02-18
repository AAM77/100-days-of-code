#######################################
# TIC-TAC-TOE USING PROCEDURAL PYTHON #
#######################################

# GLOBAL VALUES
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
players = ["",""]
count = 0

# ALL OF THE WINNING COMBINATIONS
def winning_combos():
    return [
    [0,1,2],            # Top-row
    [0,3,6],            # Left column
    [0,4,8],            # T-left-B-right
    [1,4,7],            # Middle column
    [2,5,8],            # Right column
    [2,4,6],            # T-right-B-left
    [3,4,5],            # Middle row
    [6,7,8],            # Bottom row
    ]

# STARTS THE GAME
def play_game():
    print_game_logo()
    print('')
    greet_player()
    print('')
    choose_x_or_o()
    print('')
    print_board()
    initiate_turn()


# DETERMINES WHO THE CURRENT PLAYER IS ('X' or 'O')
def current_player():
    if count % 2 == 0:
        return players[1]
    else:
        return players[0]


# GREETS THE PLAYER
def greet_player():
    print("Welcome to Tic-Tac-Toe")

# PRINTS THE GAME LOGO
def print_game_logo():

    title = """
    #######  #######   ######
       #        #      #
       #        #      #
       #        #      #
       #     #######   ######

    #######   ####     ######
       #     #    #    #
       #     ######    #
       #     #    #    #
       #     #    #    ######

    #######   ####     ######
       #     #    #    #
       #     #    #    ######
       #     #    #    #
       #      ####     ######
    """

    print(title)


# ASKS THE PLAYER TO CHOOSE X or O
def choose_x_or_o():

    player_choice = input("Do you want to be 'X' or 'O'?").upper()

    if player_choice == 'X':
        print('')
        print("You are now 'X', Player One.")
        print('')
        print("Player two is 'O'.")
        print('')
        print("Starting the game.")


    elif player_choice == 'O':
        print('')
        print("You are now 'O', Player One.")
        print('')
        print("Player two is 'X'.")
        print('')
        print("Starting the game.")

    else:
        print("Incorrect choice. Choose 'X' or 'O'")
        choose_x_or_o()

    set_players(player_choice)


# SETS THE PLAYERS_1 and PLAYER_2 to
def set_players(player_choice):

    if player_choice.upper() == 'X':
        players[0] = 'X'
        players[1] = 'O'
    else:
        players[0] = 'O'
        players[1] = 'X'


# PRINTS THE BOARD

def print_board():

    print('')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print('')

# GETS USER INPUT AND DETERMINES IF VALID
def position_choice():
    desired_position = input("Choose an open position. (1-9)")

    if desired_position.isdigit():
        if ((1 <= int(desired_position)) and (int(desired_position) <= 9)):
            return int(desired_position) - 1
        else:
            print("Invalid choice. You must choose a position from 1 - 9")
            position_choice()
    else:
        print("Invalid choice. You must choose a position from 1 - 9")
        position_choice()


# CHECKS IF THE CHOSEN POSITION IS VALID
def is_valid(pos_choice):

    if board[pos_choice] == 'X' or board[pos_choice] == 'O':
        return False
    else:
        return True

# UPDATES THE BOARD ARRAY WITH THE NEW POSITION
def update_board(pos_choice):
    board[pos_choice] = current_player()


# CHECKS IF THERE IS A WINNER AND WHO THAT WINNER IS
def winner():
    for combo in winning_combos():
        if all(board[pos] == current_player() for pos in combo):
            return current_player()

# CHECKS THE BOARD TO SEE IF THERE IS A WINNER OR TIE
def win_or_tie():
    if winner():
        print('')
        print( "########################################")
        print(f"# CONGRATULATIONS [-> {winner()} <-]! YOU WIN!! #")
        print( "########################################")
    elif all(item == 'X' or item == 'O' for item in board):
        print('')
        print("It's a tie!")
    else:
        return False

    replay_or_quit()
    return True

# INITIATES A TURN SEQUENCE: TAKE TURN IF NO WIN or TIE
def initiate_turn():
    if not win_or_tie():
        next_turn()

# UPDATES THE COUNT
def update_count():
    global count
    count += 1

# UPDATES COUNT AND
def next_turn():
    update_count()
    print('')
    print(f"{current_player()}'S TURN.")
    take_turn()

# TAKES TURN IF POSITION CHOICE IS VALID
def take_turn():
    board_pos = position_choice()

    if is_valid(board_pos):
        update_board(board_pos)
        print_board()
        initiate_turn()
    else:
        print("That position is taken.")
        take_turn()

# INITIATES END GAME SEQUENCE: ASKS THE USER TO REPLAY OR QUIT
def replay_or_quit():
    replay = (input("Do you want to play again? (y/n)")).lower()
    if replay == 'y':
        reset_values()
        play_game()
    elif replay == 'n':
        print('Thank you for playing!')
        exit()
    else:
        print('Invalid choice!')
        replay_or_quit()

def reset_values():
    global board
    global players
    global count

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    players = ["",""]
    count = 0
