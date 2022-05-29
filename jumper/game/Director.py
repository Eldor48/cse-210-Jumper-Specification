from game.Jumper import Jumper
from game.word import words
from game.console import Console



class Director:
        def __init__(self):
            self.keep_playing = True
            self.console = Console()
            self.jump = Jumper()
            self.word  = words
        
        def star_game(self):
            
            while self.keep_playing:
                self.get_inputs()
                self.do_updates()
                self.do_outputs()
        
        def get_inputs(self):
            self.word
        def do_updates(self):
            self.jump.process()
            
        def do_outputs(self):
            pass