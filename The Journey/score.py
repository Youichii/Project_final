class Score:
    def __init__(self, game):
        self.local_score = 0
        self.best_score = 0
        self.points = 0
        self.game = game


    def update_score(self):

        # quand le jeu commence
        if self.game.start():
            self.points = 0
        # si le monstre n'a plus de point de vie
        elif self.game.player.damage():
            self.best_score = self.points
            self.points = 0

    def increase_score(self):
        self.points += 1
        # si le joueur n'a plus de point de vie
