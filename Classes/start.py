#Class for the Start menu and the choice of the 2 pokemons
from pokemon import pokemon
class start:
    def __init__(self, pokemons):
        self.pokemons = pokemons
        self.load_pokemons()
    
    def load_pokemons(self):
        
        self.pokemons.append(pokemon("bulbizar", {"health": 20, "specialAttack":"power leaf special attack", "Attack":"leaf attack","damage": 0.5, "defense":1}))
        self.pokemons.append(pokemon("charmander", {"health": 20, "specialAttack":"fire blast special attack", "Attack":"fire attack","damage": 0.5, "defense":1}))
        self.pokemons.append(pokemon("squirtle", {"health": 20, "specialAttack":"water blast special attack", "Attack":"water attack","damage": 0.5, "defense":1}))
        self.pokemons.append(pokemon("smogogo", {"health": 20, "specialAttack":"smog poison special attack", "Attack":"smog attack","damage": 0.5, "defense":1}))
        self.pokemons.append(pokemon("pikachu", {"health": 20, "specialAttack":"power charge special attack", "Attack":"charge attack","damage": 0.5, "defense":1}))
        self.show_start_pokemon()
    
    def show_start_pokemon(self):
        print("choose between the following pokemons (1 or 2)")
        for i in range(2):
            print(f"{i}: {self.pokemons[i].name}")
        inp = input("your choice: ")
        print("your choice is: ")
        print(self.pokemons[int(inp)].name)
        print(self.pokemons[int(inp)].abilities)
    
            
pokemons = list()     
start(pokemons)