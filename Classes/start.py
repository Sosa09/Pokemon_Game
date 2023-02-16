#Class for the Start menu and the choice of the 2 pokemons
from pokemon import pokemon
from trainer import trainer
class start:

    _pokemon = list()
    
    def __init__(self):
        pass
        
    
    def load_pokemons(self):
        
        self._pokemon.append(pokemon("Bulbizar", {"health": 20, "specialAttack":"power leaf special attack", "Attack":"leaf attack","damage": 0.5, "defense":1}))
        self._pokemon.append(pokemon("Charmander", {"health": 20, "specialAttack":"fire blast special attack", "Attack":"fire attack","damage": 0.5, "defense":1}))
        self._pokemon.append(pokemon("Squirtle", {"health": 20, "specialAttack":"water blast special attack", "Attack":"water attack","damage": 0.5, "defense":1}))
        self._pokemon.append(pokemon("Smogon", {"health": 20, "specialAttack":"smog poison special attack", "Attack":"smog attack","damage": 0.5, "defense":1}))
        self._pokemon.append(pokemon("Pikachu", {"health": 20, "specialAttack":"power light charge special attack", "Attack":"charge attack","damage": 0.5, "defense":1}))
        return self._pokemon
        
    
    def _show_start_pokemon(self):
        print("Hello Trainer. \nWelcome on pokechoco. \nTo begin the game choose between the following pokemons (1 or 2) \n\n")
        for i in range(2):
            print(f"{i}: {self._pokemon[i].name}")\
        
        inp = input("Your choice: ")
        print("Your choice is: ")
        print(self._pokemon[int(inp)].name)
        print(self._pokemon[int(inp)].abilities)
        return int(inp)
    
    def select_pokemon(self):
        i = self._show_start_pokemon()
        return self._pokemon[i]
                
