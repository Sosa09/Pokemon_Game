class pokemon:
    #define the constructor of the class
    def __init__(self, name, abilities):
        self.name = name
        #abilities will be dictionary with following elements: health, SpecialAttack, Attack, Defence, x, y
        self.abilities = abilities
        
        
    #define the attack method to execute in a battle, the player can select between attack or specialattack
    def attack(self, isSpecialAttack):
        pass
    
    #define the defend method to execute in a battle, the pokemon will get less damage / 0.1
    def defend(self, damage):
        pass
    
    #define a run megthod the trainer can be a pussy and run away from the battle
    def run():
        pass
    