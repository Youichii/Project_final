from player import Player





class Score:
    """Constructor of the class"""
    """PRE:/
       POST: Build the constructor of the class
    """
    def __init__(self, game):
        self.local_score = 0
        self.best_score = 0
        self.points = 0
        self.game = game
        self.player = Player(self)

    def update_score(self):
        """Udpate the score of the player"""
        """PRE:/
           POST: Initilise the attribut point if the game begin or if we lose
        """

        if self.game.start():
            self.points = 0

        elif self.game.player.damage():
            self.best_score = self.points
            self.points = 0

    def increase_score(self):
        """Increase the score"""
        """PRE:/
           POST: Incerement the int points inisialized to 0
        """
        self.points += 1
        if self.points >= 1:
            self.player.attack_up()

