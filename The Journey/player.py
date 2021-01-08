import pygame
from projectile import Projectile

# creer un class = joueur

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        """
        Constructor of the class
        PRE:/
        POST: Take game as parameter. Build the constructor of the class

        """

        super().__init__()
        self.y = 500
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectile = pygame.sprite.Group()
        self.image = pygame.image.load('im/tank-2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 450
        self.is_jumping = 0
        self.jump_count = 1

    def damage(self, amount):
        """Define a damage for the class
       PRE:/
       POST: Substract the parameter to the attribut health

       """
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.score.local_score = self.game.score.points
            if self.game.score.best_score < self.game.score.points:
                self.game.score.best_score = self.game.score.points
            self.game.game_over()
            self.game.score.points = 0

    def update_health_bar(self, surface):
        """Draw a health bar
        PRE:/
        POST: Drawing with a pygame modul a health bar with attributs healt and max_healt as parameters
        """

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def launch_projectile(self):
        """Launch projectiles
        PRE:/
        POST: Use object of the class and add it to the attribut group
        """

        self.all_projectile.add(Projectile(self))

    def move_right(self):
        """Moving the player to the right
        PRE:/
        POST: If there is no collision between player and monster group, the player will add to his x position a velocity
        """
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        """Moving the player to the left
        PRE:/
        POST: Adding to the x position of the player his velocity
        """
        self.rect.x -= self.velocity

    def jump(self):
        """Allow the player to jump
        PRE:/
        POST:Change the state of the attribut is_jumping to 1
        """
        self.is_jumping = 1

    def jump_update(self):
        if self.is_jumping or self.is_jumping == "max_height":
            self.jump_count = 0
            if self.rect.y > 100 and self.is_jumping != "max_height":
                self.rect.y -= 1
                if self.rect.y == 100:
                    self.is_jumping = "max_height"
            elif self.is_jumping == "max_height":
                self.rect.y += 2
                if self.rect.y == 450:
                    self.is_jumping = 0
                    self.jump_count = 1
                elif self.game.check_collision(self, self.game.all_monsters):
                    self.is_jumping = 0
                    self.jump_count = 1

    def attack_up(self):
        self.attack += 10
