import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    threeballs = 0
    for i in range(numTrials):
        balls = [1,1,1,0,0,0]
        hand = []
        while len(balls)>3:
            pull = random.choice(balls)
            balls.remove(pull)
            hand.append(pull)
        if all(x == hand[0] for x in hand):
            threeballs += 1
    return float(threeballs)/numTrials
            
                    
            
            
            
            
        
