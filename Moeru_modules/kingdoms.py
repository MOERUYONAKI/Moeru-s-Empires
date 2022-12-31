# - - - - - I M P O R T S - - - - -


from random import *


# - - - - - C L A S S E S - - - - -


class City():
    """Permet de créer une ville"""
    def __init__(self, name : str = 'My city', lvl : int = 1, stat : str = 'city'):
        self.c_name = name
        if lvl >= 0:
            self.level = lvl - 1

        if stat == 'prefecture':
            self.status = 1

        elif stat == 'capital':
            self.status = 2

        else:
            self.status = 0

    def get_infos(self, excepts : str = 'nothing'):
        if excepts == 'all':
            return f'{self.c_name}'

        elif excepts == 'level':
            return f'{self.c_name} - {City.Status.check_stat(self)}'

        elif excepts == 'status':
            return f'{self.c_name} - {City.Levels.check_lvl(self)}'

        else:
            return f'{self.c_name} - {City.Levels.check_lvl(self)} - {City.Status.check_stat(self)}'

    def add_lvl(self, nbr : int = 1):
        self.level += nbr

    def remove_lvl(self, nbr : int = 1):
        self.level -= nbr

    def rank_upgrade(self):
        if self.status + 1 <= 2:
            self.status += 1

        else:
            print('La ville possède déjà le niveau de statut maximal')

    def rank_downgrade(self):
        if self.status - 1 >= 0:
            self.status -= 1

        else:
            print('La ville possède déjà le niveau de statut minimal')

    def upgrade_price(self):
        lvl = City.Levels.check_lvl(self)
        price = City.Levels.levels[lvl]['gold_product']
        return price

    # - - - - - S O U S - C L A S S E S - - - - -

    class Levels():
        """Définit le niveau d'amélioration de la ville"""
        def __init__(self):
            self.level = self.lvl 

        levels = [{'hp' : 150, 'defense' : 100, 'gold_product' : 5, 'troopers_product' : 10},
            {'hp' : 250, 'defense' : 102, 'gold_product' : 8, 'troopers_product' : 12},
            {'hp' : 400, 'defense' : 104, 'gold_product' : 12, 'troopers_product' : 16},
            {'hp' : 650, 'defense' : 106, 'gold_product' : 17, 'troopers_product' : 22},
            {'hp' : 1050, 'defense' : 108, 'gold_product' : 23, 'troopers_product' : 30}]

        def check_lvl(self):
            return self.level + 1

        def stats_lvl(self):
            hp = City.Levels.levels[self.level]['hp']
            defs = City.Levels.levels[self.level]['defense']
            gold = City.Levels.levels[self.level]['gold_product']
            troops = City.Levels.levels[self.level]['troopers_product']
            return f'hp : {hp}\ndefense : {defs}\ngold : {gold}\ntroops : {troops}'
    
    class Status():
        """Définit le type de ville"""
        def __init__(self):
            self.status = self.stat

        status = ['city', 'prefecture', 'capital']

        def check_stat(self):
            return City.Status.status[self.status]

    # - - - - - - - - - - - - - - - - - - - - 

class Kingdom():
    """Groupe de villes (class City)"""
    def __init__(self, name : str = 'Mon royaume', cities : list = [], type : str = "Seigneurie"):
        self.cities = cities
        self.name = name
        self.gold = 10
        self.troops = 25

        types = ["Seignerie", "Duché", "Marquisat", "Comté", "Baronnie"]

        if type in types:
            self.type = type

        else:
            self.type = "Seigneurie"

        self.k_name = f'{self.type} {name}'

    def has_capitale(self):
        for city in self.cities:
            if isinstance(city, City):
                if City.Status.check_stat(city) == 'capital':
                    return True

            else:
                self.cities.remove(city)

        return False

    def show_cities(self):
        texte = f'**{self.k_name} :**'
        for city in self.cities:
            if isinstance(city, City):
                texte += f'\n{city.get_infos()}'

            else:
                self.cities.remove(city)

        return texte

    def add_city(self, city : City()):
        if City.Status.check_stat(city) == 'capital':
            if self.has_capitale():
                print('Ce royaume possède déjà une capitale')

        else:
            self.cities.append(city)

    def add_city2(self, city : City()):
        self.cities.append(city)

    def remove_city(self, city : City()):
        if city in self.cities:
            self.cities.remove(city)

        else:
            print('Aucune ville correspondante')

    def inventory(self):
        return f'**Or =** {self.gold}\n**Troupes =** {self.troops}'

class Kingdoms():
    """Groupe de royaumes (class Kingdom)"""
    def __init__(self, name : str = 'Mon royaume', cities : list = [], type : str = "Seigneurie"):
        self.cities = cities
        self.kingdoms = []
        
        types = ["Seignerie", "Duché", "Marquisat", "Comté", "Baronnie"]

        if type in types:
            self.type = type

        else:
            self.type = "Seigneurie"

        self.ks_name = f'{self.type} {name}'

    def add_city(self, city : City()):
        self.cities.append(city)

    def add_kingdom(self, kingdom : Kingdom()):
        kingdom = Kingdoms(kingdom.name, kingdom.cities, type = kingdom.type)
        self.kingdoms.append(kingdom)

    def show_cities(self, symb : str = ''):
        texte = self.ks_name + ' :' 
        for kdm in self.kingdoms:
            self.cities.append(kdm)

        for city in self.cities:
            if isinstance(city, City):
                texte += '\n' + symb + city.get_infos('level')

            elif isinstance(city, Kingdoms):
                if city.type == "Duché":
                    symb = "╰─ "
                    
                elif city.type == "Marquisat":
                    symb = "╰── "

                elif city.type == "Comté":
                    symb = "╰─── "

                elif city.type == "Baronnie":
                    symb = "╰──── "

                texte += f'\n{symb}{city.show_cities(symb)}'   

            else:
                self.cities.remove(city)

        return texte
    
    
# - - - - - F O N C T I O N S - - - - -


