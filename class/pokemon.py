# Created and managed by Soufiane
import pygame

class Pokemon(pygame.sprite.Sprite):
    _healthBar = 830;
    def __init__(self, name, type, hp, at, df, spa, spdef, spd, img):
        super().__init__()
        self.name = name
        self.img = img,
        self.type = type
        self.hp = hp
        self.at = at
        self.df = df
        self.spa = spa
        self.spdef = spdef
        self.spd = spd
        self.pos = ()
        self.groups = []
        self._load_image()


    
    def _load_image(self):
        self.image = pygame.image.load(f'{self.img[0]}').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))      
    def set_healthBarValue(self, hb):
        self._healthBar = self._healthBar - hb
    def get_healthBarValue(self):
        return self._healthBar
    def get_name(self):
        return self.name       
    
    def set_name(self, name):
        self.name = name
    
    def attack(self):
        return self.at
    
    def defense(self):
        return self.df 
    
    def special_attack(self):
        #will return attack + special attack and also give the special attack name
        return self.spdef 
    
    def special_defense(self):
        #will return defense + special defense and also give the special defense name
        return self.spa             
    def recover(self):
        #check if potion available
        #add 10hp
        if(self._healthBar < 820):
            self._healthBar = self._healthBar + 10
    def set_position(self,pos):
        self.pos = pos
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def set_groups(self, groups):
        self.groups = groups
    
    def __str__(self):
        return f"Name:              {self.name}\nPokemon Type:      {self.type}\nHealth Power:      {self.hp}\nAttack:            {self.at}\nDefense:           {self.df}\nSpecial Attack:    {self.spa}\nSepcial Defense:   {self.spdef}\nSpeed:             {self.spd}"

        
