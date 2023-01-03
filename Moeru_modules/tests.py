from kingdoms import *

test = City('test')
Yona = Kingdom("Yona", type = "Seigneurie", cities = [test])
Firae = City('Firae', 6, 'capital')
Yona.add_city2(Firae)

Test = Kingdom("Test", type = "Seigneurie")
cap = City('Capitale', 5, 'capital')
Test.add_city2(cap)

print(Yona.show_cities(), '\n', Test.show_cities())

get_city(test, Yona, Test)

print('\n', Yona.show_cities(), '\n', Test.show_cities())