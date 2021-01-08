import pygame
from projectile import Projectile


# creer un class = joueur

class Player(pygame.sprite.Sprite):
    def __init__(self, game):

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
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.score.local_score = self.game.score.points
            if self.game.score.best_score < self.game.score.points:
                self.game.score.best_score = self.game.score.points
            self.game.game_over()
            self.game.score.points = 0

    def update_health_bar(self, surface):

        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def launch_projectile(self):

        self.all_projectile.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
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
