####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Fire Breathing Rubber Duckies' # Only 10 chars displayed.
strategy_name = 'Red Hot Oompa-Loompas'
strategy_description = 'we do 5 colludes followed by 5 betrayals(IT IS A TRAP!) then use the average score of each trial to decide if we should betray or collude.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    total_b = 0#variable assignment
    average_b = 0
    total_c = 0
    average_c = 0
    if my_history == 'bbbbb':#calculates betray average
        total_b = my_score
        average_b = (total_b)/5
    if my_history == 'bbbbbccccc':#calculates collude average
        total_c = my_score - total_b
        average_c = (total_c)/5
    if my_history == '':#checks the iterations of the code in order to set the first ten collude or betrays.
        return 'b'
    elif my_history == 'b':
        return 'b'
    elif my_history == 'bb':
        return 'b'
    elif my_history == 'bbb':
        return 'b'
    elif my_history == 'bbbb':
        return 'b'
    elif my_history == 'bbbbb':
        return 'c'
    elif my_history == 'bbbbbc':
        return 'c'
    elif my_history == 'bbbbbcc':
        return 'c'
    elif my_history == 'bbbbbccc':
        return 'c'
    elif my_history == 'bbbbbcccc':#end of iteration
        return 'c'
    else:#returns collude or betray from then on based on the average scores of betray or collude.
        if average_b >= average_c:
            return 'b'
        elif average_c < average_b:
            return 'c'
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             