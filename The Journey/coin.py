import pygame
import random

#test

class Coin(pygame.sprite.Sprite):  # Création d'une calsse pour les "Coins"

    def __init__(self, game):

        super().__init__()
        self.game = game
        self.image = pygame.image.load('im/money.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 1050)
        self.rect.y = random.randint(250, 525)

    def collide_player(self):
        if self.game.check_collision(self, self.game.all_players):
            self.rect.x = random.randint(20, 1050)
            self.rect.y = random.randint(250, 525)
            self.game.score.increase_score()
