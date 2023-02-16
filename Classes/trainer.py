class trainer:
    def __init__(self, name, pokemons = list(), pokeballs = 0) -> None:
        self.name = name
        self.pokemons = pokemons
        self.pokeballs = pokeballs
        pass
    
    def list_pokemons(self):
        #just show all your pokemons
        print(self.pokemons[0].name)
        print(self.pokemons[0].abilities)
        # for pokemon in self.pokemons:
        #     print(pokemon.name)
        #     for i in range(len(pokemon.abilities)):
        #         print(pokemon.abilities[i][0] + "," + pokemon.abilities[i][1])
     
    
    def catch_pokemon(self):
        #check if enough pokeballs
        pass
    
    def greet(self):
        print(f"Welcome {self.name}")
        print("Here are your pokemons: ")
        self.list_pokemons()