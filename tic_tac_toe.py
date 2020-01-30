# Introduction, difficulty and pick letters

# define empty the board
board =\
'''
1  |2  |3
   |   |
-----------
4  |5  |6
   |   |
-----------
7  |8  |9
   |   |
'''

print ("The game is Tic Tac Toe!")

# function to show empty board
def show_empty_board(board):
    print ("\nBoard:\n{}".format(board))
    
# show empty board
show_empty_board(board)

# let user pick his letter
user_letter = input("Pick a letter: x | o\n")

while (user_letter != 'x' and user_letter !='o'):
    user_letter = input("Pick normal fuckin' letter :D : x | o\n")

# let user pick difficulty
difficulty = input("Pick difficulty: 0 (fo pussiez) | 1 (meh) | 9000 (god mode)\n")
while (difficulty != '0' and difficulty != '1' and difficulty !='9000'):
    difficulty = input("Did. I. Stutter.? : 0 | 1 | 9000\n")
    
    if difficulty == 9000:
        print ("You know you can't win, right?")
    
    
# define CPU letter
if user_letter == 'x':
    cpu_letter = 'o'
else:
    cpu_letter = 'x'
    
    
###############################################################################
    

# Decide turns function

from random import randrange

# define who goes first
def decide_turns():
    
    user_turn = randrange(2) + 1

    if user_turn == 1 :
        print ("You go 1st!")
        cpu_turn = 2
    else:
        print ("You go 2nd!")
        cpu_turn = 1
        
    return (user_turn, cpu_turn)


###############################################################################


# define functions for CPU and user moves
    
def user_plays():
    user_move = input("Pick a position...\n")
    
    check_range = False
    check_empty = False
    
    
    while not(check_range and check_empty):
        if not user_move.isnumeric():
            check_range = False
            check_empty = False
            user_move = input("Pick a real fuckin' position :D ...\n")
        elif int(user_move) > 9 or int(user_move) < 1 :
            check_range = False
            user_move = input("Pick a real fuckin' position :D ...\n")
        elif (board_dict[int(user_move)] != ' '):
            check_empty = False
            user_move = input("You have to pick an empty position. Try again ...\n")
            check_range = True
        else:
            check_range = True
            check_empty = True        
    
    if int(user_move) in [1,3,7,9]:
        user_last_corner == user_move
    
    board_dict[int(user_move)] = user_letter
        
    return (int(user_move))

from random import choice

def cpu_plays(difficulty):
    
    # current state of board
    current_board = list(board_dict.values())
    # keep only empty positions indeces
    empty_board_indeces = []
    i = 0
    for x in current_board:
        i = i+1
        if x == ' ':
            empty_board_indeces.append(i)
            
    if difficulty == '0':  # easy
        cpu_move = choice(empty_board_indeces)
    elif difficulty == '1':  # moderate  
        if count_moves == 1 :
            cpu_move = choice([1,3,7,9])
        else:
            # check for winning moves
            can_win, cpu_move = make_win_move(current_board, empty_board_indeces)
        
            # if there are no winning moves
            if not can_win :
                # protect from losing moves
                can_lose, cpu_move = make_defend_move(current_board, empty_board_indeces)
            
            # if you can't win nor lose 
            if ((not can_win) and (not can_lose)) :
                #just pick randomly
                cpu_move = choice(empty_board_indeces)
            
    else: # god mode
        cpu_move = find_best_move(current_board, empty_board_indeces)
        
    board_dict[cpu_move] = cpu_letter
            
    return (int(cpu_move))


###############################################################################
    

# function to check and return wining move
    
def make_win_move(current_board, empty_board_indices):
    can_win = False
    cpu_move = 404
    
    # horizontal wins
    for i in [0, 3, 6]:
        if current_board[i] == current_board[i+1] == cpu_letter :
            if (i+3) in empty_board_indices:
                cpu_move = i+2
                can_win = True
    for i in [1, 4, 7]:
        if current_board[i] == current_board[i+1] == cpu_letter :
            if (i) in empty_board_indices:
                cpu_move = i-1
                can_win = True
    for i in [0, 3, 6]:
        if current_board[i] == current_board[i+2] == cpu_letter :
            if (i+2) in empty_board_indices:
                cpu_move = i+1
                can_win = True
    # vertical wins
    for i in [0, 1, 2]: # xx-
        if current_board[i] == current_board[i+3] == cpu_letter :
            if (i+7) in empty_board_indices:
                cpu_move = i+6
                can_win = True
    for i in [3, 4, 5]: # -xx
        if current_board[i] == current_board[i+3] == cpu_letter :
            if (i-2) in empty_board_indices:
                cpu_move = i-3
                can_win = True
    for i in [0, 1, 2]: #x-x
        if current_board[i] == current_board[i+6] == cpu_letter :
            if (i+4) in empty_board_indices:
                cpu_move = i+3
                can_win = True
    # diagonal wins
    for i in [0, 2]:
        if current_board[i] == current_board[4] == cpu_letter :
            if (9-i) in empty_board_indices:
                cpu_move = 8-i
                can_win = True
    for i in [0, 2]:
        if current_board[4] == current_board[8-i] == cpu_letter :
            if (i+1) in empty_board_indices:
                cpu_move = i
                can_win = True
    for i in [0, 2]:
        if current_board[i] == current_board[8-i] == cpu_letter :
            if (5) in empty_board_indices:
                cpu_move = 4
                can_win = True

    return (can_win, cpu_move+1)


###############################################################################
    

# function to check and return wining move
    
def make_defend_move(current_board, empty_board_indices):            
    can_lose = False
    cpu_move = -1
    
    #print (current_board)
    #print (empty_board_indices)
    
    # horizontal wins
    for i in [0, 3, 6]: # xx-
        if current_board[i] == current_board[i+1] == user_letter :
            if (i+3) in empty_board_indices:
                cpu_move = i+2
                can_lose = True
    for i in [1, 4, 7]: # -xx
        if current_board[i] == current_board[i+1] == user_letter :
            if (i) in empty_board_indices:
                cpu_move = i-1
                can_lose = True
    for i in [0, 3, 6]: # x-x
        if current_board[i] == current_board[i+2] == user_letter :
            if (i+2) in empty_board_indices:
                cpu_move = i+1
                can_lose = True
    # vertical wins
    for i in [0, 1, 2]: # xx-
        if current_board[i] == current_board[i+3] == user_letter :
            if (i+7) in empty_board_indices:
                cpu_move = i+6
                can_lose = True
    for i in [3, 4, 5]: # -xx
        if current_board[i] == current_board[i+3] == user_letter :
            if (i-2) in empty_board_indices:
                cpu_move = i-3
                can_lose = True
    for i in [0, 1, 2]: #x-x
        if current_board[i] == current_board[i+6] == user_letter :
            if (i+4) in empty_board_indices:
                cpu_move = i+3
                can_lose = True
    # diagonal wins
    for i in [0, 2]:
        if current_board[i] == current_board[4] == user_letter :
            if (9-i) in empty_board_indices:
                cpu_move = 8-i
                can_lose = True
    for i in [0, 2]:
        if current_board[4] == current_board[8-i] == user_letter :
            if (i+1) in empty_board_indices:
                cpu_move = i
                can_lose = True
    for i in [0, 2]:
        if current_board[i] == current_board[8-i] == user_letter :
            if (5) in empty_board_indices:
                cpu_move = 4
                can_lose = True
        
    return (can_lose, cpu_move+1)


###############################################################################
  
   
# function that finds possible open corner    
def free_corner(current_board):
    l = []
    
    for i in [0, 2, 6, 8]:
        if current_board[i] == ' ':
            l.append(i)
            
    if not l : # list is empty
        return (404) 
    else:
        return (choice(l)+1)
   
# function that finds possible open space
def free_space(current_board):
    l = []
    
    for i in [0,1,2,3,4,5,6,7,8]:
        if current_board[i] == ' ':
            l.append(i)   
            
    if not l : # list is empty
        return (404) 
    else:
        return (choice(l)+1)
    
# function that finds possible open edge
def free_edge(current_board):
    l = []
    
    for i in [1,3,5,7]:
        if current_board[i] == ' ':
            l.append(i)   
            
    if not l : # list is empty
        return (404) 
    else:
        return (choice(l)+1)

# function that check if user holds oposite corners
def opp_corners(current_board):
    op = False
    
    if current_board[0] == current_board[8] == user_letter:
        op = True
    if current_board[2] == current_board[6] == user_letter:
        op = True
            
    return (op)    


###############################################################################


# function that finds the best move
    
def find_best_move(current_board, empty_board_indeces):
    
    # if CPU goes first
    if count_moves == 1 :
        cpu_move = 1
        
    if count_moves == 3:
        if 9 in empty_board_indeces:
            cpu_move = 9
        else:
            cpu_move = 3    
            
    if count_moves == 5:
        can_win, cpu_move = make_win_move(current_board, empty_board_indeces)
        if (not can_win):
            can_lose, cpu_move = make_defend_move(current_board, empty_board_indeces)
            if (not can_win) and (not can_lose) :
                c = free_corner(current_board)
                if (c != 404):
                    cpu_move = c
                    if (not can_win) and (not can_lose) and (c==404) :
                        s = free_space(current_board)        
                        cpu_move = s
        
    if count_moves == 7:
        can_win, cpu_move = make_win_move(current_board, empty_board_indeces)
        if (not can_win):
            can_lose, cpu_move = make_defend_move(current_board, empty_board_indeces)
            if ((not can_win) and (not can_lose)) :
                c = free_corner(current_board)
                if (c != 404):
                    cpu_move = c
                    if ((not can_win) and (not can_lose) and (c==404)) :
                        s = free_space(current_board)        
                        cpu_move = s
            
    if count_moves == 9:
        s = free_space(current_board)
        cpu_move = s
        
    # if CPU goes second
    if count_moves == 2 :
        if current_board[4] == ' ' :
            cpu_move = 5
        else:
            c = free_corner(current_board)
            cpu_move = c
            
    if count_moves == 4 :
        can_lose, cpu_move = make_defend_move(current_board, empty_board_indeces)
        if (not can_lose):
            op = opp_corners(current_board)
            if op:
                cpu_move = free_edge(current_board)
        if ((not can_lose) and (not op)):
            if (user_last_corner != 404):
                h = 10 - user_last_corner
                if (h in empty_board_indeces):
                    cpu_move = h
        if ( (not can_lose) and (not op) and ((user_last_corner == 404) or ((10-user_last_corner)not in empty_board_indeces)) ):
            c = free_corner(current_board)
            cpu_move = c
            
    if count_moves == 6 :
        can_win, cpu_move = make_win_move(current_board, empty_board_indeces)
        if (not can_win):
            can_lose, cpu_move = make_defend_move(current_board, empty_board_indeces)
            if ((not can_win) and (not can_lose)) :
                c = free_corner(current_board)
                cpu_move = c
                if ((not can_win) and (not can_lose) and (c==404)) :
                    s = free_space(current_board)
            
    if count_moves == 8 :
        can_win, cpu_move = make_win_move(current_board, empty_board_indeces)
        if (not can_win):
            can_lose, cpu_move = make_defend_move(current_board, empty_board_indeces)
            if ((not can_win) and (not can_lose)) :
                c = free_corner(current_board)
                cpu_move = c
                if ((not can_win) and (not can_lose) and (c==404)) :
                    s = free_space(current_board)
                    cpu_move = s
    
    return (cpu_move)


###############################################################################

    
# define function to print updated board
    
def show_updated_board():
    #print ("\nBoard:\n")
    print ('''
           {}  |{}  |{}  
              |   |   
           -----------
           {}  |{}  |{}  
              |   |   
           -----------
           {}  |{}  |{}  
              |   |   
           '''.format(board_dict[1], board_dict[2], board_dict[3], 
           board_dict[4], board_dict[5], board_dict[6], 
           board_dict[7], board_dict[8], board_dict[9]))
    

###############################################################################


# define function to check if someone won or we have a tie

def check_win():
    
    x_win = False
    o_win = False
    win = False
    
    for letter in ['x', 'o']:
        
        # check row win
        for i in [1, 4, 7]:
            
            if board_dict[i] == board_dict[i+1] == board_dict[i+2] == letter:
                win = True
                if letter == 'x':
                    x_win = True
                else:
                    o_win = True
                
        # check column win
        for i in [1, 2, 3]:
            
            if board_dict[i] == board_dict[i+3] == board_dict[i+6] == letter:
                win = True
                if letter == 'x':
                    x_win = True
                else:
                    o_win = True
                    
        # check diagonal win
        for i in [1, 3]:
            
            if board_dict[i] == board_dict[5] == board_dict[10-i] == letter:
                win = True
                if letter == 'x':
                    x_win = True
                else:
                    o_win = True
                   
    if x_win:
        print ("~~~~~~ X's win this game ~~~~~~ ")
    if o_win:
        print ("~~~~~~ O's win this game ~~~~~~ ")
        
    return (win)


###############################################################################


# check if the board if full
def check_full():
    
    full = True
    
    for i in board_dict :
        if board_dict[i] == ' ' :
            full = False
    
    return (full)
    

###############################################################################
          

# check if the player wants to start again
def start_over():
    
    play_again = input ("Wanna play some more of this shit?\n 'Y' for yes | 'N' for no\n")
    while ((play_again != 'Y' and play_again !='y') and (play_again !='N' and play_again!='n')):
        play_again = input("\tPick a normal fuckin' option :D : Y | N\n")
    
    if play_again == 'Y' or play_again == 'y':
        print ("\nReally? Get a life...\n")
        again = True
    elif play_again == 'N' or play_again == 'n':
        again = False
    
    return again
    

###############################################################################


# pattern loops

def user_loop():
    print ("\t\t\t\tUser's turn:")
    user_plays()
    show_updated_board()
    win = check_win()
    full = check_full()
    return (win, full)

def cpu_loop(difficulty):
    print ("\t\t\t\tCPU's turn:")
    cpu_plays(difficulty)
    show_updated_board()
    win = check_win()
    full = check_full()
    return (win, full)


###############################################################################


# new game starts
new_game = True

# main game pattern
while new_game: 
    
    # deciding turns 1 <- 1st, 2 <- 2nd
    print("\nTurns are decided by the Goddess of Luck\n... \n")
    user_turn, cpu_turn = decide_turns()
    
    # initialize new empty board
    board_dict = {1:' ', 2:' ', 3:' ', 4:' ',
              5:' ', 6:' ', 7:' ', 8:' ', 9:' ',}

    # initialize moves counter
    count_moves = 0
    
    # initialize variable that holds user's last corner move
    user_last_corner = 404

    if user_turn == 1:
        count_moves += 1
        win, full = user_loop()
        if win or full:
            again = start_over()
            if again:
                print (">NEW ROUND<!")
            else:
                print ("\nTHE END!")
                new_game = False
    while(True):        
        count_moves += 1
        win, full = cpu_loop(difficulty)
        if win or full:
            again = start_over()
            if again:
                print (">NEW ROUND<!")
            else:
                print ("\nTHE END!")
                new_game = False
            break
        count_moves += 1
        win, full = user_loop()
        if win or full:
            again = start_over()
            if again:
                print (">NEW ROUND<!")
            else:
                print ("\nTHE END!")
                new_game = False
            break
    
    
# if we are here that means that the player doesnt want to play again

print ("\n\nThank you for playing my stupid game :D ! Have a great life my friend!\n")







