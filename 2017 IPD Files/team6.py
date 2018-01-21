import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'McDavitt' # Only 10 chars displayed.
strategy_name = 'Random, but vindictive'
strategy_description = 'Collude first round, then choose at random unless they betrayed last 2 rounds, in which case I will also betray.'
    
def move(my_history, their_history, my_score, their_score):
    '''Collude first round, then choose at random unless they betrayed
    last 2 rounds, in which case I will also betray.
    '''
    if len(my_history)==0: # It's the first round: collude
        return 'c'
    else:  
        # Reference last rounds
        last_round_them = their_history[-1]
        second_last_round_them = their_history[-2]
        last_round_me = my_history[-1]
        second_last_round_me = my_history[-2]
        if last_round_them == 'b' or second_last_round_them == 'b': #if they betrayed in the last 2 rounds
            return 'b' #be vindictive
        else:
            return random.choice(['b','c']) #be random
    
'''
def test_move(my_history, their_history, my_score, their_score, result):
    #calls move(my_history, their_history, my_score, their_score)
    #from this module. Prints error if return value != result.
    #Returns True or False, depending on whether result was as expected.
   
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
              result='b')             '''