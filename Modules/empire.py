from Modules.kingdoms import *

Yona = Kingdoms("Yona", type = "Seigneurie")
Firae = City('Firea', 6, 'capital') # Dirigée par Lord Moeru
Yona.add_city(Firae)

Kitsune = Kingdom('Kitsune', type = "Duché")
Rusanor = City('Rusanor', 5, 'capital') # Dirigée par Ser Rusano
Kitsune.add_city2(Rusanor)
Yona.add_kingdom(Kitsune)

Moerus_kd = Yona.show_cities()
print(Moerus_kd)