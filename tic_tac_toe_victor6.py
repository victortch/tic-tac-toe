import random
import ast


learn_iterations = 10000

def rotate_board_left(current_state):
 
    new_state = list(current_state)
    new_state[6] = current_state[0]
    new_state[0] = current_state[2]
    new_state[2] = current_state[8]
    new_state[8] = current_state[6] 
    
    new_state[3] = current_state[1]
    new_state[1] = current_state[5]
    new_state[5] = current_state[7]
    new_state[7] = current_state[3]

    return new_state

def rotate_board_right(current_state):
    new_state = list(current_state)
    new_state[0] = current_state[6]
    new_state[2] = current_state[0]
    new_state[8] = current_state[2]
    new_state[6] = current_state[8]

    new_state[1] = current_state[3]
    new_state[5] = current_state[1]
    new_state[7] = current_state[5]
    new_state[3] = current_state[7]

    return new_state

def board_flip(current_state):
    new_state = list(current_state)
    new_state[2] = current_state [0]
    new_state[5] = current_state [3]
    new_state[8] = current_state [6]
    
    new_state[0] = current_state [2]
    new_state[3] = current_state [5]
    new_state[6] = current_state [8]

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

def rotate_move_left(move):
    if move == 0: new_move = 6
    elif move == 2: new_move = 0
    elif move == 8: new_move = 2
    elif move == 6: new_move = 8
    elif move == 1: new_move = 3
    elif move == 5: new_move = 1
    elif move == 7: new_move = 5
    elif move == 3: 
        new_move = 7
    else:
        new_move = 4
    return new_move
    
def rotate_move_right(move):
    if move == 6: new_move = 0
    elif move == 0: new_move = 2
    elif move == 2: new_move = 8
    elif move == 8: new_move = 6
    elif move == 3: new_move = 1
    elif move == 1: new_move = 5
    elif move == 5: new_move = 7
    elif move == 7: 
        new_move = 3
    else:
        new_move = 4
    return new_move

def move_flip(move):
    new_move = move
    if move == 2: new_move = 0
    if move == 5: new_move = 3
    if move == 8: new_move = 6
    if move == 0: new_move = 2
    if move == 3: new_move = 5
    if move == 6: new_move = 8
    return new_move

def transform_move(move, rotations, direction = 'left', flip = False):
    
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

def check_consecutive_states(states1, states2):
    for i in range(9):
        if states1[i] != 0 and states1[i] != states2[i]:
            return False
    if (sum(states2) - sum(states1)) > 2:
        return False
    else:
        return True

def check_next_move(states1, states2):
    if check_consecutive_states(states1, states2):
        for i in range(9):
            if states2[i] > states1[i]:
                return[i]
    else:
        print("Moves not consecutive!")
        
        


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
    print ("----------------------")
    print ("  ",line2[0],"  |  ",line2[1],"  |  ", line2[2])
    print ("----------------------")
    print ("  ",line3[0],"  |  ",line3[1],"  |  ", line3[2])

    print ("\n\nMAP\n\n")
    print ("  ","0","  |  ","1","  |  ", "2")
    print ("----------------------")
    print ("  ","3","  |  ","4","  |  ", "5")
    print ("----------------------")
    print ("  ","6","  |  ","7","  |  ", "8")
    


# Get all unique board states in which the game has not ended

unique_states = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(8):
    print('Removing duplicates for step: ', i)
    if i == 0:
        previous_step = [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    if i % 2 == 0:
        player = 1
    else: player = 2
    current_step = []
    for j in range(len(previous_step)):
        previous_step_state = previous_step[j]
        for k in range(len(previous_step_state)):
            current_step_state = previous_step_state[:]
            if previous_step_state[k] == 0:
                current_step_state[k] = player
                if check_outcome(current_step_state) == 0:
                    current_step.append(current_step_state)
    # remove duplicates from current step
    duplicate_indices = []
    for l in range(len(current_step)):
        for m in range(l+1, len(current_step)):
            equivalent, rotation, flip = is_equivalent(current_step[l], current_step[m])
            if equivalent: 
                duplicate_indices.append(m)
    
    previous_step = []
    for n in range(len(current_step)):
        if n not in duplicate_indices:
            unique_states.append(current_step[n])
            previous_step.append(current_step[n])


# Make each of the unique states from the previous step a key in a dictionary.
# The values of this dictionary themselves will be also dictionaries.
# The keys for the latter nested dictionary will be all possible moves for the respective state.
# The values will be lists tracking the wins, losses, draws and a derived score for the respective move.

move_dict = {}

for i in range(len(unique_states)):
    print("Adding non-duplicate moves for state:", " ", i, " / ", len(unique_states))
    move_dict[str(unique_states[i])] = {}
    possible_moves = []
    if sum(unique_states[i][j] == 1 for j in range(len(unique_states[i]))) > \
            sum(unique_states[i][j] == 2 for j in range(len(unique_states[i]))):
            player_to_move = 2
    else: 
        player_to_move = 1
    possible_next_states = []
    possible_moves = []
    for k in range(len(unique_states[i])):
        possible_next_state = unique_states[i][:]
        if unique_states[i][k] == 0:
            possible_next_state[k] = player_to_move
            possible_next_states.append(possible_next_state)
            possible_moves.append(k)
    duplicate_indices = []
    for l in range(len(possible_next_states)):
        for m in range(l+1, len(possible_next_states)):
            equivalent, rotation, flip = is_equivalent(possible_next_states[l], possible_next_states[m])
            if equivalent:
                duplicate_indices.append(m)
    for n in range(len(possible_moves)):
        if n not in duplicate_indices:
            move_dict[str(unique_states[i])][str(possible_moves[n])] = [0, 0, 0, 0]
            
        




# Start learning

for i in range(learn_iterations):
    print("Self-learning game: ", i)
    ##Random first player versus random second player
    if i < 0.25 * learn_iterations:
        player_1_alpha = 0
        player_2_alpha = 0
    ##Best first player versus random second player
    elif i < 0.5 * learn_iterations:
        player_1_alpha = 1
        player_2_alpha = 0
    ##Best second player versus random first player
    elif i < 0.75 * learn_iterations:
        player_1_alpha = 0
        player_2_alpha = 1
    ##Good first player versus good second player
    else:
        player_1_alpha = 0.5
        player_2_alpha = 0.5
        
    current_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game_steps = 0
    dictionary_states_moves = []
    while True:
        game_steps += 1
        if game_steps % 2 == 0:
            player_to_move = 2
            alpha = player_2_alpha
        else:
            player_to_move = 1
            alpha = player_1_alpha
        found_state = False
        for j in range(len(move_dict)):
            dictionary_state = list(move_dict.keys())[j]
            equivalent, state_rotation, state_flip = is_equivalent(current_state, ast.literal_eval(dictionary_state))
            if equivalent:
                found_state = True
                if random.random() > alpha:
                    dictionary_move = random.choice(list(move_dict[dictionary_state]))
                else:
                    list_scores = [] 
                    for n in range(len(list(move_dict[dictionary_state].values()))):
                        score = list(move_dict[dictionary_state].values())[n][3]
                        list_scores.append(score) 
                    index = list_scores.index(max(list_scores)) 
                    dictionary_move = list(move_dict[dictionary_state])[index]
                break
        if found_state == False:
            print("State not found!")
            break
        dictionary_states_moves.append([dictionary_state, dictionary_move])
        
        actual_move = (transform_move(int(dictionary_move), state_rotation, flip = state_flip))
        current_state[actual_move] = player_to_move
        outcome = check_outcome(current_state)
        if outcome == 1:
            for k in range(len(dictionary_states_moves)):
                if k % 2 == 0:
                    move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][0] += 1
                    move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][3] = \
                        (move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][0] - \
                            move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][1]) / \
                            sum(move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][:3])
                else:
                    move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][1] += 1
                    move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][3] = \
                        (move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][0] - \
                            move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][1]) / \
                            sum(move_dict[dictionary_states_moves[k][0]][dictionary_states_moves[k][1]][:3])
            break
        if outcome == 2:
            for l in range(len(dictionary_states_moves)):
                if l % 2 == 0:
                    move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][1] += 1
                    move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][3] = \
                        (move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][0] - \
                            move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][1]) / \
                            sum(move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][:3])
                else:
                    move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][0] += 1
                    move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][3] = \
                        (move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][0] - \
                            move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][1]) / \
                            sum(move_dict[dictionary_states_moves[l][0]][dictionary_states_moves[l][1]][:3])
            break
        if sum(current_state) == 13:
            for m in range(len(dictionary_states_moves)):
                move_dict[dictionary_states_moves[m][0]][dictionary_states_moves[m][1]][2] += 1
            move_dict[dictionary_states_moves[m][0]][dictionary_states_moves[m][1]][3] = \
            (move_dict[dictionary_states_moves[m][0]][dictionary_states_moves[m][1]][0] - \
             move_dict[dictionary_states_moves[m][0]][dictionary_states_moves[m][1]][1]) / \
             sum(move_dict[dictionary_states_moves[m][0]][dictionary_states_moves[m][1]][:3])
            break
            
 
        
                    
            
        
    
        
            


    
    
        
    
    

    
    


    



