#  > - <  I P O R T S  > - <  #


import random as rdm 


#  > - <  F O N C T I O N S  > - <  #


def basic_roll(max : int):
    '''Dice roll / probabilities equals for each values
    > Return a number upper than 0 and lower or equal than the "max"'''
    nbr = rdm.randint(0, max)
    return nbr

def katsu_roll(cmd : str):
    first = 0
    
    # if first thing is a number, take it
    if cmd[0].isalpha():
        if cmd[0] != 'd':
            return f'CommandError : "{cmd[0]}"'
        
    elif cmd[0].isdigit():
        for i in range(1, len(cmd) - 2):
            if cmd[i].isdigit() and cmd[i + 1].isalpha():
                first = int(cmd[0 : i])
                cmd = cmd[i + 1 : len(cmd) - 1]
            
            elif cmd[i].isalpha() and cmd[i] != 'd':
                return f'CommandError : "{cmd[i]}"'
        
print(katsu_roll("10h"))