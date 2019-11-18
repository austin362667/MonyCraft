import ffn
import random 
import math


def RandomWalk(code):
    
    prices = ffn.get(str(code))

    init = prices.iloc[-1][0]
    return_daily = []
    n_lst = [init]
    for n in range(250):

        n_lst.append(init*(random.random()-0.5)*math.sqrt(1/250))
        return_daily.append(sum(n_lst))
        
    return return_daily
    
    

if __name__ == '__main__':
    RandomWalk()  