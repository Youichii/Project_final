import pygame
from player import Player
from monster import Monster
from score import Score
from coin import Coin


# classe du jeu
class Game:
    def __init__(self):

        # definir si notre jeu a commencé
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.coin = Coin(self)
        self.all_coins = pygame.sprite.Group()
        self.all_coins.add(self.coin)
        self.score = Score(game=Game)
        self.all_players.add(self.player)
        self.monster = Monster(self)
        self.all_monsters = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}

    # pour relancer le jeu avec les monstres quand on meurt
    def start(self):
        self.is_playing = True
        self.spawn_monster()  # appel de la methode
        self.score.points = 0
        self.player.rect.y = 450
        self.player.rect.x = 400

    def game_over(self):
        # remettre le jeu à 0
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = "transition"

    def update(self, screen):
        # appliquer image du joueur
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.coin.image, self.coin.rect)

        # afficher le score
        font = pygame.font.Font(None, 30)
        scores = font.render("Score : " + str(self.score.points), True, (255, 255, 255))
        best_current = font.render("Best score : " + str(self.score.best_score), True, (255, 255, 255))
        screen.blit(scores, (0, 0))
        screen.blit(best_current, (0, 50))

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joueeurs
        for projectile in self.player.all_projectile:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.coin.collide_player()

        # appliquer les images projectiles
        self.player.all_projectile.draw(screen)

        # appliquer ensemble des images des monstres
        self.all_monsters.draw(screen)

        # verifier déplacement du joueur

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.jump_count:
            self.player.jump()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)  # ajoute un monstre au groupe de monstres
