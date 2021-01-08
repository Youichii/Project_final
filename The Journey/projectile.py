import pygame




class Projectile(pygame.sprite.Sprite):
    # héritage qui nous permet de prendre la classe comment élément graphique du jeu


    def __init__(self, player):
        """Constructor of the class
        PRE:/
        POST: Take player as parameter. Build the constructor
        """
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('im/laser.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 0
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        """Rotate movment for the projectile
        PRE:/
        POST: Apply a pygame function to allaw the attribut image to rotate with a given angle
        """

        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        """Delete the projectile
        PRE:/
        POST: Removing the group projectile from the player
        """
        self.player.all_projectile.remove(self)

    def move(self):
        """Moving the projectile
        PRE:/
        POST: Adding the velocity to the x position and applying the rotate method.
              When the projectile and the monster collide, apply method remove() to the projectile.
              Monster of the group will have damage.

        """
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)


        if self.rect.x > 1080:
            self.remove()
