#lets Keep Track of what we played before in an array
player_move = []
# Starting  with Scissors
intial_move = my_next_move = 'S'
# Keep track of which bot we're playing against
which_bot = [False, False, False, False]

counter_moves = {'P': 'R', 'R': 'S', 'S': 'P'}
quincy_position = -1
my_patterns = [{
    "RR": 0, 
    "RP": 0, 
    "RS": 0, 
    "PR": 0, 
    "PP": 0, 
    "PS": 0, 
    "SR": 0, 
    "SP": 0, 
    "SS": 0, 
}]

def player(opponent_last_move, opponent_moves=[]):
    global player_move, my_next_move, which_bot, counter_moves, quincy_position, my_patterns
    
  
    opponent_moves.append(opponent_last_move)
    player_move.append(my_next_move)

    if(len(set(which_bot)) == 1 and opponent_moves[-5:] == ['R', 'P', 'P', 'S', 'R']):
        which_bot[0] = True
        
    # Strategy for Quincy
    if(which_bot[0]):
     
        if(len(opponent_moves) % 1000 == 0):
            which_bot = [False, False, False, False]
            opponent_moves.clear()

        quincy_counter_moves = ['P', 'S', 'S', 'R', 'P'] 
        quincy_position = (quincy_position + 1) % 5
        return quincy_counter_moves[quincy_position]
    if(len(set(which_bot)) == 1 and opponent_moves[-5:] == ['P', 'P', 'R', 'R', 'R']):
        which_bot[1] = True
        
    # Strategy for Abbey
    if(which_bot[1]): 
    
        last_two_moves = ''.join(player_move[-2:])
        if(len(last_two_moves) == 2):
            my_patterns[0][last_two_moves] += 1
            
      
        possible_next = [
            my_next_move + 'R', 
            my_next_move + 'P', 
            my_next_move + 'S', 
        ]
        
        pattern_counts = {
            k: my_patterns[0][k]
            for k in possible_next if k in my_patterns[0]
        }
    
        abbey_prediction = max(pattern_counts, key=pattern_counts.get)[-1:]

        # Reset after each match
        if(len(opponent_moves) % 1000 == 0):
            which_bot = [False, False, False, False]
            opponent_moves.clear()
            my_patterns = [{
              "RR": 0, 
              "RP": 0, 
              "RS": 0, 
              "PR": 0, 
              "PP": 0, 
              "PS": 0, 
              "SR": 0, 
              "SP": 0, 
              "SS": 0, 
            }]
            
    
        my_next_move = counter_moves[abbey_prediction]
        return my_next_move




    if(len(set(which_bot)) == 1 and opponent_moves[-5:] == ['P', 'R', 'R', 'R', 'R']):
        which_bot[2] = True
        
    # Strategy for Kris
    if(which_bot[2]):

        if(len(opponent_moves) % 1000 == 0):
            which_bot = [False, False, False, False]
            opponent_moves.clear()

        my_next_move = counter_moves[my_next_move]
        return my_next_move
        
    if(len(set(which_bot)) == 1 and opponent_moves[-5:] == ['R', 'R', 'R', 'R', 'R']):
        which_bot[3] = True

    # Strategy for Mrugesh
    if(which_bot[3]):  
        if(len(opponent_moves) == 1000):
            which_bot = [False, False, False, False]
            opponent_moves.clear()

   
        last_ten = player_move[-10:]
        most_common = max(set(last_ten), key=last_ten.count)
        
    
        my_next_move = counter_moves[most_common]
        return my_next_move

    my_next_move = intial_move
    return my_next_move