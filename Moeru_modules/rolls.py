#  > - <  I P O R T S  > - <  #


import random as rdm 


#  > - <  F O N C T I O N S  > - <  #


def basic_roll(max : int):
    '''Dice roll / probabilities equals for each values
    > Return a number upper than 0 and lower or equal than the "max"'''
    nbr = rdm.randint(0, max)
    return nbr

def Katsu_roll(cmd : str):
    '''100 roll with bonus and malus
    > Return a number upper than 0 and lower or equal than 100 with malus or bonus'''
    command = []
    cmd_size = len(cmd) - 1
    
    # cmd spliting in command
    for elt in cmd:
        if elt.isdigit():
            command.append(int(elt))
            
        else:
            if elt in ["d", "+", "-"]:
                if elt != "d":
                    if "d" not in command:
                        return f'CommandError : "{elt}"'
                    
                    else:
                        command.append(elt)
                    
                else:
                    if "d" not in command:
                        command.append(elt)
                    
                    else:
                        return f'CommandError : "{elt}"'
                
            elif elt == " ":
                break
            
            else:
                return f'CommandError : "{elt}"'
            
    # split assembling
    if "d" not in command:
        return f'CommandError : "d" is required tu use this roll'
    
    else:
        i = command.index("d")
        
        # first assembling (rolls number)
        if i > 0:
            first = ""
            for idx in range(i):
                elt = command[idx]
                if type(elt) is int:
                    first += str(elt)
                    
                else:
                    break
                
            first = int(first)
            
        else:
            first = 1
        
        # roll check (if number after "d" is 100)
        if cmd_size > i:
            size = ""
            for idx in range(i + 1, len(command)):
                elt = command[idx]
                if type(elt) is int:
                    size += str(elt)
                    
                else:
                    break
            
            if int(size) != 100:
                return f'CommandError : invalide dice size, size must be "100"'
                
            if cmd_size > i + 3:
                if type(command[i + 4]) is int:
                    return f'CommandError : invalide dice size, size must be "100"'
                
        else:
            return f'CommandError : cannot find any dice size'
            
        # bonus assembling (with "+" and "-")
        def bonus_check(bns : list, i : int): # return the bonus value (without use "+" or "-")
            bonus = ""
            for idx in range(i + 1, len(command)):
                elt = command[idx]
                if type(elt) is int:
                    bonus += str(elt)
                    
                else:
                    break
                
            return int(bonus)
                
        bonus = 0        
        if len(command) - 1 > i + 4:
            i += 4
            bonus_index = []
            for i in range(len(command)):
                if command[i] in ["+", "-"] and type(command[i + 1]) is int:
                    bonus_index.append(i)
            
            for idx in bonus_index:
                if command[idx] == "+":
                    bonus += bonus_check(command, idx)
                  
                if command[idx] == "-":
                    bonus -= bonus_check(command, idx)
        
        # final command (assembled)
        if bonus > 0:
            command = [first, "d", 100, f'+{bonus}']
            
        elif bonus < 0:
            command = [first, "d", 100, bonus]
            
        else:
            command = [first, "d", 100, None]
        
        finals = []
        for i in range(first):
            roll = basic_roll(100)
            result = roll + bonus
            finals.append([roll, result])
            
        return [command, finals]
   
def roll_pourcents(arg1 : int = 50, arg2 : int = 50):
    total = arg1 + arg2
    if total == 100:
        nbr = rdm.randint(0,100)
        if nbr <= arg1:
            return f'Réussite *({arg1}%)*'
            
        else:
            return f'Échec *({arg1}%)*'
            
        print(f'{ctx.message.author} tente un roll !')
            
    elif (arg1 < 0 and arg2 > 0) or (arg1 > 0 and arg2 < 0):
        if arg1 < 0 and arg2 > 0:
            arg1 = -arg1
            roll_pourcents(arg1, arg2)  
            
        else:
            arg2 = -arg2
            roll_pourcents(arg1, arg2)  
            
    elif arg1 < 0 and arg2 < 0:
        arg1 = -arg1
        arg2 = -arg2
        roll_pourcents(arg1, arg2)  
        
    elif arg1 == 0 and arg2 == 0:
        return 'Valeurs incorrectes'
        
    else:
        arg1 = round(arg1 * 100 / total, 0)
        arg2 = round(arg2 * 100 / total, 0)
        total = arg1 + arg2
        if total == 99:
            arg1 += 0.5
            arg2 += 0.5
            
        elif total == 101:
            arg1 += 0.5
            arg2 += 0.5
            
        roll_pourcents(arg1, arg2)  

# tests
# print(Katsu_roll("d100-5"))