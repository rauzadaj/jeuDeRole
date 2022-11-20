import random

my_life = 50
enemy_life = 50
potion = random.randint(15, 50)
potion_count = 3
my_attack = random.randint(5, 10)
enemy_attack = random.randint(5, 15)
option1 = "attaquer (1)"
option2 = "utiliser une potion (2)"
choix = ""
while my_life > 0 or enemy_life > 0:
    choix = input(f'Voulez vous {option1} ou {option2} ?')
    if choix == "1":
        print(f"Vous infligez une attaque de {my_attack}.")
        enemy_life = enemy_life - my_attack
        print(f"Les points de vie de votre ennemie sont desormais de {enemy_life}.")
    if choix == "2":
        if my_life == 50:
            print("Vous ne pouvez pas utiliser de potion. Vos points de vie sont au maximum.")
        else:
            my_life = my_life + potion
            potion_count = potion_count - 1
            print(f"La potion vous ajoute {potion_count} points de vie. Vos points de vie sont desormais de {my_life}.")