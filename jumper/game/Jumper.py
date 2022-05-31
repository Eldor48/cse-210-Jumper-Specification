
import random
from game.word import words
from game.Shoot import glider



"""We need the logic to choose which picture gets displayed
If they get a correct letter or a wrong one."""






class Jumper:
    

    def __init__(self):
      self.word = words
      self.guess = ""
      #self.word = [self.words.word(self)]
      self.reveal = list(len(self.word)*'_')
      self.lives = 4
      self.won = False
      self.lose = False

    def letter_check(self, letter, word):
      """Checks the word to see is the letter guessed is in the word."""

      for i in range(0,len(self.word)):
          letter = self.word[i]
          if self.guess == letter:
              self.reveal[i] = self.guess
      if '_' not in self.reveal:
          return True
      else:
          return False


    def show(self):
      """prints out the picture and uses the logic needed to change depending on the lives count."""
      print(glider[4 - self.lives])
      print(self.reveal)
    def process(self):
      """This is the logic while trying to get the guessing game to work
      It checks the letter"""
      while self.won == False and self.lives > 0:
          self.show()
          self.guess = input('guess letter: ')
          self.guess = self.guess.upper()
          
          if self.guess == self.word:
              self.won = True
              self.reaveal = self.word
          if len(self.guess) == 1 and self.guess in self.word:
              self.won = self.letter_check(self.guess, self.word)   
          else:
              self.lives-=1
          """When win is official this prints Congratulations message"""
          if self.won == True:
              print(f"nice! you guessed {self.word}")
              print("")
          else:
              print("sorry, loser")
              print(" ")
          """When loss is official this prints last picture"""
          if self.lives == 0:
              self.lose = True
          if self.lose == True:
              print(glider[4])
              print("You've lost")
              self.lost = False
              print(self.word)