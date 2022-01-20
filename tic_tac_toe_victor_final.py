import random
import ast
import math
import pickle

def move_row_position(move, n=3):
    if ((move+1) % n) == 0:
        current_row_position = n
    else:
        current_row_position = ((move+1) % n)
    return current_row_position

def move_row(move, n=3):
    return math.ceil((move+1)/n)

def right_space(move, n=3):
    return (n - move_row_position(move, n))

def below_space(move, n=3):
    return (n - move_row(move, n))

def move_from_coordinates(move_row, move_row_position, n=3):
    move = ((move_row-1)*n + move_row_position)-1
    return move
    
def rotate_move_left(move, n=3):
    new_move_row = 1 + right_space(move, n)
    new_row_position = move_row(move, n)
    new_position = move_from_coordinates(new_move_row, new_row_position, n)
    return new_position

def rotate_move_right(move, n=3):
    new_move_row = move_row_position(move, n)
    new_row_position = 1 + below_space(move, n)
    new_position = move_from_coordinates(new_move_row, new_row_position, n)
    return new_position

def move_flip(move, n=3):
    new_row_position = n - move_row_position(move, n) + 1
    current_row = move_row(move, n)
    new_position = move_from_coordinates(current_row, new_row_position, n)
    return new_position
    

def rotate_board_left(current_state):
    new_state = list(current_state)
    for i in range(len(current_state)):
        new_state[rotate_move_left(i)] = current_state[i]
    return new_state

def rotate_board_right(current_state):
    new_state = list(current_state)
    for i in range(len(current_state)):
        new_state[rotate_move_right(i)] = current_state[i]
    return new_state

def board_flip(current_state):
    new_state = list(current_state)
    for i in range(len(current_state)):
        new_state[move_flip(i)] = current_state[i]
    return new_state


def change_board(current_state, rotations, direction = 'left', flip = False):
    new_state = current_state
    rotations = rotations % 4
    if flip:
        new_state = board_flip(new_state)
    if rotations > 0:
        if direction == 'left':
            for i in range(rotations):
                new_state = rotate_board_left(new_state)
        else: 
            for i in range(rotations):
                new_state = rotate_board_right(new_state)
    return new_state


def change_move(move, rotations, direction = 'left', flip = False): 
    new_move = move
    rotations = rotations % 4
    if flip:
            new_move = move_flip(new_move) 
    if rotations > 0:
        if direction == 'left':
            for i in range(rotations):
                new_move = rotate_move_left(new_move)
        else: 
            for i in range(rotations):
                new_move = rotate_move_right(new_move)
    return new_move
        


def is_equivalent(state1, state2):
    equivalent = False
    rotations = 0
    flip = False
    for i in range(4):
        if state1 == change_board(state2, rotations=i):
            equivalent = True
            rotations = i
            flip = False
            break
        elif state1 == change_board(state2, rotations=i, flip = True):
            equivalent = True
            rotations = i
            flip = True
            break
        else:
            continue
    return equivalent, rotations, flip


def check_outcome(state):
    if state[0] == 1 and state[1] == 1 and state[2] == 1:
        return 1
    if state[3] == 1 and state[4] == 1 and state[5] == 1:
        return 1
    if state[6] == 1 and state[7] == 1 and state[8] == 1:
        return 1
    if state[0] == 1 and state[3] == 1 and state[6] == 1:
        return 1
    if state[1] == 1 and state[4] == 1 and state[7] == 1:
        return 1
    if state[2] == 1 and state[5] == 1 and state[8] == 1:
        return 1
    if state[0] == 1 and state[4] == 1 and state[8] == 1:
        return 1
    if state[2] == 1 and state[4] == 1 and state[6] == 1:
        return 1


    if state[0] == 2 and state[1] == 2 and state[2] == 2:
        return 2
    if state[3] == 2 and state[4] == 2 and state[5] == 2:
        return 2
    if state[6] == 2 and state[7] == 2 and state[8] == 2:
        return 2
    if state[0] == 2 and state[3] == 2 and state[6] == 2:
        return 2
    if state[1] == 2 and state[4] == 2 and state[7] == 2:
        return 2
    if state[2] == 2 and state[5] == 2 and state[8] == 2:
        return 2
    if state[0] == 2 and state[4] == 2 and state[8] == 2:
        return 2
    if state[2] == 2 and state[4] == 2 and state[6] == 2:
        return 2

    return 0

def display_move_stats(moves_dictionary, dictionary_state, dictionary_move):
    wins = moves_dictionary[dictionary_state][dictionary_move][0]
    losses = moves_dictionary[dictionary_state][dictionary_move][1]
    draws = moves_dictionary[dictionary_state][dictionary_move][2]
    games = wins + losses + draws
    win_perc = ("{0:.0%}".format(wins/games))
    loss_perc = ("{0:.0%}".format(losses/games))
    draw_perc = ("{0:.0%}".format(draws/games))
    score = moves_dictionary[dictionary_state][dictionary_move][4]
    print("\nLast machine move stats:")
    print("Wins - " + win_perc + ", Losses - " + str(loss_perc) + ", Draws - " + str(draw_perc) + ", Score - " + str(round(score,2)), "\n")




def display_game(state):
    game_state = list(state)
    for i in range(len(game_state)):
        if game_state[i] == 1:
            game_state[i] = "X"
        if game_state[i] == 2:
            game_state[i] = "O"
        if game_state[i] == 0:
            game_state[i] = " "

    line1 = game_state[0:3]
    line2 = game_state[3:6]
    line3 = game_state[6:9]

    print ("  ",line1[0],"  |  ",line1[1],"  |  ", line1[2])
    print ("-------+-------+------")
    print ("  ",line2[0],"  |  ",line2[1],"  |  ", line2[2])
    print ("-------+-------+------")
    print ("  ",line3[0],"  |  ",line3[1],"  |  ", line3[2])

    print ("\nMAP\n")
    print ("  ","0","  |  ","1","  |  ", "2")
    print ("-------+-------+------")
    print ("  ","3","  |  ","4","  |  ", "5")
    print ("-------+-------+------")
    print ("  ","6","  |  ","7","  |  ", "8")


def player_to_move(state):
    if state.count(1) > state.count(2):
        player = 2
    else:
        player = 1
    return player

def possible_next_moves(state):
    next_moves = []
    for i in range(len(state)):
       if state[i] == 0: 
           next_moves.append(i)
    return next_moves


def possible_next_states(state):
    possible_next_states = []
    next_moves = possible_next_moves(state)
    player = player_to_move(state)
    for i in range(len(next_moves)):
        next_state = state[:]
        next_state[next_moves[i]] = player
        possible_next_states.append(next_state)
    return next_moves, possible_next_states

def duplicate_indices(states):
    duplicate_indices = []
    for i in range(len(states)):
        for j in range(i+1, len(states)):
            equivalent, rotation, flip = is_equivalent(states[i], states[j])
            if equivalent: 
                duplicate_indices.append(j)
    return duplicate_indices
    

def remove_duplicate_states(states):
    duplicates = duplicate_indices(states)
    unique_states = []
    for k in range(len(states)):
        if k not in duplicates:
            unique_states.append(states[k])
    return unique_states
    

def unique_next_moves(state):
    next_moves_unique = []
    next_moves, next_states = possible_next_states(state)
    duplicates = duplicate_indices(next_states)
    for i in range(len(next_moves)):
        if i not in duplicates:
            next_moves_unique.append(next_moves[i])
    return next_moves_unique


def random_move(dictionary_state, moves_dictionary):
    dictionary_move = random.choice(list(moves_dictionary[dictionary_state]))
    return dictionary_move

def best_move(dictionary_state, moves_dictionary):
    list_scores = [] 
    for n in range(len(list(moves_dictionary[dictionary_state].values()))):
        score = list(moves_dictionary[dictionary_state].values())[n][4]
        list_scores.append(score) 
    index = list_scores.index(max(list_scores)) 
    dictionary_move = list(moves_dictionary[dictionary_state])[index]
    return dictionary_move


def choose_move(state, moves_dictionary, alpha):
    found_state = False
    for i in range(len(moves_dictionary)):
        dictionary_state = list(moves_dictionary.keys())[i]
        equivalent, state_rotation, state_flip = is_equivalent(state, ast.literal_eval(dictionary_state))
        if equivalent:
            found_state = True
            if random.random() > alpha:
                dictionary_move = random_move(dictionary_state, moves_dictionary)
            else:
                dictionary_move = best_move(dictionary_state, moves_dictionary)
            break
    if found_state == False:
        print("State not found!")
    actual_move = (change_move(int(dictionary_move), state_rotation, flip = state_flip))
    return dictionary_state, dictionary_move, actual_move

def change_score(moves_dictionary, dictionary_state, dictionary_move):
    moves_dictionary[dictionary_state][dictionary_move][4] = moves_dictionary[dictionary_state][dictionary_move][3] / \
        sum(moves_dictionary[dictionary_state][dictionary_move][:3])

def player1_increment_win(moves_dictionary, dictionary_game, player1_alpha, player2_alpha):
    game_length = len(dictionary_game)
    length_bonus = 10 - game_length
    multiplier = 1 + ((player2_alpha - player1_alpha)/2)
    for k in range(len(dictionary_game)):
        dictionary_state = dictionary_game[k][0]
        dictionary_move = dictionary_game[k][1]            
        if k % 2 == 0:
            moves_dictionary[dictionary_state][dictionary_move][0] += 1
            moves_dictionary[dictionary_state][dictionary_move][3] += multiplier*length_bonus
            change_score(moves_dictionary, dictionary_state, dictionary_move)

def player1_increment_loss(moves_dictionary, dictionary_game, player1_alpha, player2_alpha):
    game_length = len(dictionary_game)
    length_bonus = 10 - game_length
    multiplier = 1 + ((player1_alpha - player2_alpha)/2)
    for k in range(len(dictionary_game)):
        dictionary_state = dictionary_game[k][0]
        dictionary_move = dictionary_game[k][1]            
        if k % 2 == 0:      
            moves_dictionary[dictionary_state][dictionary_move][1] += 1
            moves_dictionary[dictionary_state][dictionary_move][3] -= multiplier*length_bonus
            change_score(moves_dictionary, dictionary_state, dictionary_move)
            

    
def player1_increment_draw(moves_dictionary, dictionary_game, player1_alpha, player2_alpha):
    value = (player1_alpha - player2_alpha)/2
    for k in range(len(dictionary_game)):
        dictionary_state = dictionary_game[k][0]
        dictionary_move = dictionary_game[k][1]            
        if k % 2 == 0:
            moves_dictionary[dictionary_state][dictionary_move][2] += 1
            if player1_alpha > player2_alpha:
                moves_dictionary[dictionary_state][dictionary_move][3] -= value
                change_score(moves_dictionary, dictionary_state, dictionary_move)



def player2_increment_win(moves_dictionary, dictionary_game, player1_alpha, player2_alpha):
    game_length = len(dictionary_game)
    length_bonus = 10 - game_length
    multiplier = 1 + ((player1_alpha - player2_alpha)/2)
    for k in range(len(dictionary_game)):
        dictionary_state = dictionary_game[k][0]
        dictionary_move = dictionary_game[k][1]            
        if k % 2 != 0:
            moves_dictionary[dictionary_state][dictionary_move][0] += 1
            moves_dictionary[dictionary_state][dictionary_move][3] += multiplier*length_bonus
            change_score(moves_dictionary, dictionary_state, dictionary_move)

def player2_increment_loss(moves_dictionary, dictionary_game, player1_alpha, player2_alpha):
    game_length = len(dictionary_game)
    length_bonus = 10 - game_length
    multiplier = 1 + ((player2_alpha - player1_alpha)/2)
    for k in range(len(dictionary_game)):
        dictionary_state = dictionary_game[k][0]
        dictionary_move = dictionary_game[k][1]            
        if k % 2 != 0:      
            moves_dictionary[dictionary_state][dictionary_move][1] += 1
            moves_dictionary[dictionary_state][dictionary_move][3] -= multiplier*length_bonus
            change_score(moves_dictionary, dictionary_state, dictionary_move)
    
def player2_increment_draw(moves_dictionary, dictionary_game, player1_alpha, player2_alpha):
    value = (player1_alpha - player2_alpha)/2
    for k in range(len(dictionary_game)):
        dictionary_state = dictionary_game[k][0]
        dictionary_move = dictionary_game[k][1]            
        if k % 2 != 0:
            moves_dictionary[dictionary_state][dictionary_move][2] += 1
            if player1_alpha > player2_alpha:
                moves_dictionary[dictionary_state][dictionary_move][3] += value
                change_score(moves_dictionary, dictionary_state, dictionary_move)

        


def learn(moves_dictionary, dictionary_game, player1_alpha, player2_alpha, outcome):
    if outcome == 1:
        player1_increment_win(moves_dictionary, dictionary_game, player1_alpha, player2_alpha)
        player2_increment_loss(moves_dictionary, dictionary_game, player1_alpha, player2_alpha)
                
    if outcome == 2:
        player1_increment_loss(moves_dictionary, dictionary_game, player1_alpha, player2_alpha)
        player2_increment_win(moves_dictionary, dictionary_game, player1_alpha, player2_alpha)
                
    if outcome == 0:
        player1_increment_draw(moves_dictionary, dictionary_game, player1_alpha, player2_alpha)
        player2_increment_draw(moves_dictionary, dictionary_game, player1_alpha, player2_alpha)
                
    print('New Experience Gained!\n\n')


def self_play(moves_dictionary, alpha1, alpha2):
    current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    dictionary_game = []
    while True:
        player = player_to_move(current_state)
        if player == 1:
            alpha = alpha1
        else:
            alpha = alpha2
        dictionary_state, dictionary_move, actual_move = choose_move(current_state, moves_dictionary, alpha)
        dictionary_game.append([dictionary_state, dictionary_move])
        current_state[actual_move] = player
        outcome = check_outcome(current_state)
        if outcome == 1:
            print("Player 1 Won!")
            return dictionary_game, outcome
            break
        if outcome == 2:
            print("Player 2 Won!")
            return dictionary_game, outcome
            break
        if sum(current_state) == 13:
            print("Draw!")
            return dictionary_game, outcome
            break



                    
######################################################################################################################################
# Get all unique board states in which the game has not ended

def get_unique_states():
    unique_states = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    for i in range(8):
        print('Removing duplicates for step: ', i)
        if i == 0:
            previous_states = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        current_states = []
        
        for j in range(len(previous_states)):
            next_moves, next_states = possible_next_states(previous_states[j])
            for k in range(len(next_states)):
                outcome = check_outcome(next_states[k])
                if outcome == 0:
                    current_states.append(next_states[k])
                
        current_unique_states = remove_duplicate_states(current_states)
        
        previous_states = []
        for j in range(len(current_unique_states)):
            unique_states.append(current_unique_states[j])
            previous_states.append(current_unique_states[j])
    return unique_states


# Make each of the unique states from the previous step a key in a dictionary.
# The values of this dictionary themselves will be also dictionaries.
# The keys for the latter nested dictionary will be all possible moves for the respective state.
# The values will be lists tracking the wins, losses, draws and a derived score for the respective move.
def create_move_dict(unique_states):
    moves_dictionary = {}
    for i in range(len(unique_states)):
        moves_dictionary[str(unique_states[i])] = {}
        next_moves_unique = unique_next_moves(unique_states[i])
        for j in range(len(next_moves_unique)):
            moves_dictionary[str(unique_states[i])][str(next_moves_unique[j])] = [0, 0, 0, 0, 0]
    return moves_dictionary


# Start learning
def start_learning(learn_iterations, moves_dictionary):
    for i in range(learn_iterations):
        print("Self-learning game: ", i)
        ##Random first player versus random second player
        if i < 0.25 * learn_iterations:
            player1_alpha = 0
            player2_alpha = 0
        ##Best first player versus random second player
        elif i < 0.5 * learn_iterations:
            if i % 2 == 0:
                player1_alpha = 0
                player2_alpha = 1
            else:
                player1_alpha = 1
                player2_alpha = 0
        ##Good first player versus good second player
        elif i < 0.75 * learn_iterations:
            if i % 2 == 0:
                player1_alpha = i/learn_iterations
                player2_alpha = 1
            else:
                player1_alpha = 1
                player2_alpha = i/learn_iterations
        else:
            player1_alpha = 0.7
            player2_alpha = 0.7
        print("alpha1: ", player1_alpha, ", alpha2: ", player2_alpha)
        dictionary_game, outcome = self_play(moves_dictionary, player1_alpha, player2_alpha)
        learn(moves_dictionary, dictionary_game, player1_alpha, player2_alpha, outcome)
        
# Save experience
def save_experience(moves_dictionary):
    with open('move_dict.pkl', 'wb') as f:
        pickle.dump(moves_dictionary, f)

# Load Experience
def load_experience(file_name):
    print ("Trying to load move_dict.pkl..")
    with open(file_name, 'rb') as f:
        move_dict = pickle.load(f)
    return move_dict

# Start human play

def start_play(moves_dictionary):
    play_again = 'y'
    while play_again == 'y':
        current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        game_steps = 0
        order_preference = input("Would you like to go first (1) or second (2)?:")
        
        
        while True:
            game_steps += 1
            if game_steps % 2 == 0:
                player_to_move = 2
            else:
                player_to_move = 1
                
            if player_to_move == int(order_preference):
                display_game(current_state)
                actual_move = input('What is your move?:')
            else:
                dictionary_state, dictionary_move, actual_move = choose_move(current_state, moves_dictionary, 1)
                display_move_stats(moves_dictionary, dictionary_state, dictionary_move)
            current_state[int(actual_move)] = player_to_move
            outcome = check_outcome(current_state)
            if outcome == int(order_preference):
                display_game(current_state)
                print("You Won!")
                play_again = input('Would you like to play again? (y/n):')
                break
            elif outcome > 0:
                display_game(current_state)
                print("Machine Won!")
                play_again = input('Would you like to play again? (y/n):')
                break
            if sum(current_state) == 13:
                display_game(current_state)
                print("Draw!")
                play_again = input('Would you like to play again? (y/n):')
                break
######################################################################################################################################

try:
    move_dict = load_experience('move_dict.pkl')
except:
    print ('move_dict.pkl not found')
    unique_states = get_unique_states()
    move_dict = create_move_dict(unique_states)
    start_learning(10000, move_dict)
    save_experience(move_dict)

start_play(move_dict)


    



