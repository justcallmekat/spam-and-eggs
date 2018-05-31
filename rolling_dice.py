#This is a roll the dice game

#Import from modules
from random import randint
from time import sleep

#User's guess
def get_user_guess():
  guess = int(raw_input('Guess a number: \n'))
  return guess

#Use to simulate rolling dice
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(2, number_of_sides)
  max_val = number_of_sides * 2
  print 'The maxium value is: %d' % max_val
  guess = get_user_guess()
  if guess > max_val:
    print 'No guess higher than the allowed maxium value of %d' % max_val
  else:
    print 'Rolling... \n'
    sleep(2)
    print 'Your first roll is: %d \n' % first_roll
    sleep(1)
    print 'Your second roll is: %d' % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print 'Result...'
    sleep(1)
    if guess > total_roll:
      print 'Hmm, luck was on your side.. you\'ve won!'
    else:
      print 'Ha! You\'ve lost sucker!'

roll_dice(6)
