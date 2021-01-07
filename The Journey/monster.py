import pygame


# créer une classe qui gère les monstres

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        """Constructor of the class"""
        """PRE:/
           POST: Buils the constructor of the class
        """

        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('im/robot-4.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1400
        self.rect.y = 450
        self.velocity = 1

    def damage(self, amount):
        """Define a damage for the class
       PRE:/
       POST: Substract the parameter to the attribut health. If health <= initilise with the attribut max_health

       """
        self.health -= amount

        if self.health <= 0:

            print(self.rect.x)
            self.rect.x = 1400
            self.health = self.max_health
            self.game.score.increase_score()


    def update_health_bar(self, surface):
        """Draw a health bar
        PRE:/
        POST: Drawing with a pygame modul a health bar with attributs healt and max_healt as parameters
        """


        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        """Moving the monster forward
        PRE:/
        POST: If there is no collision between the monster and player the monster will move
              else, we apply the method damage() 
        """

        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            if self.rect.x < -100:
                self.rect.x = -100
                self.velocity = -1
            if self.rect.x > 1400:
                self.rect.x = 1400
                self.velocity = 1

        else:
            self.game.player.damage(self.attack)
