import random 
from game.word import words
from game.Shoot import glider

"Welcome to the game"
"Here we have the logic that will show a certain picture if the wrong word is chosen"

class Jumper: 
    
    def __init__(self):
        self.word = words
        self.guess = []
        #self.word = [self.words.word(self)]
        self.reveal = list(len(self.word)*'_')
        self.lives = 4
        self.won = False
        self.lose = False
    
    def letter_check(self, letter, word): 
        "Verifies if the word contains the letter"
        
        for i in range(0, len(self.word)):
            letter = self.word[i]
            if self.guess == letter:
                self.reveal[i] = self.guess
        if '_' not in self.reveal:
            return True
        else: 
            return False
        
    def show(self):
        """shows the picture and it changes it depending on the lives count"""
        print(glider[4 - self.lives])
        print(self.reveal)
    def process(self):
        """This is the guessing logic of the game"""
        while self.won == False and self.lives > 0:
            self.show()
            self.guess = input('guess letter: ')
            self.guess = self.guess.upper()
            
        if  self.guess == self.word:
            self.won == True
            self.reveal = self.word
            
        if len(self.guess) == 1 and self.guess in self.word: 
               self.won = self.letter_check(self.guess, self.word)
        else: 
            self.lives -= 1
        """This is the win message."""
        if self.won == True:
            print(f"Congratulations you won! The word was {self.word}, you are amazing, keep up the good work!")
            print("")
        else:
            print(f"Sorry you lost, the word was {self.word}, good luck for next time ':/ ")
            print("")
            
        if self.lives == 0:
           self.lose = True
        if self.lose == True:
            print(glider[4])
            print("You've lost, better luck next time!")
            self.lost = False
            print(self.word)
            
            
            
        
        
