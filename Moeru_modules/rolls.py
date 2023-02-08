#  > - <  I P O R T S  > - <  #


import random as rdm 


#  > - <  F O N C T I O N S  > - <  #


def basic_roll(max : int):
    '''Dice roll / probabilities equals for each values
    > Return a number upper than 0 and lower or equal than the "max"'''
    nbr = rdm.randint(0, max)
    return nbr

