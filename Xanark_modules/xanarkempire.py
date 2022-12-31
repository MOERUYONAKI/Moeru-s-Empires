from Xanark_modules.kingdoms import *

xandou = Kingdoms("Xandou", type = "Seigneurie")
Firae = City('Firea', 6, 'capital') # Dirigée par moi
xandou.add_city(Firae)

Kitsune = Kingdom('Kitsune', type = "Duché")
Rusanor = City('Rusanor', 5, 'capital') # Dirigée par moi
Kitsune.add_city2(Rusanor)
xandou.add_kingdom(Kitsune)

Xanark_kd = xandou.show_cities()
print(Xanark_kd)