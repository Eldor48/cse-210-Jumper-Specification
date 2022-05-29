from game.Jumper import Jumper
from game.word import words
from game.console import Console



class Director:
        def __init__(self):
                self.jumper = Jumper()
                self.console = Console()
                self.console.set_jumper(self.jumper)
                self.console.set_words(words)
                self.console.set_director(self)
                self.console.start_game()