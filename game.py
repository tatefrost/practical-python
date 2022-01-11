import random

computer_number = random.randint(1, 100)
attempt_counter = 0

user_name = input('What is your name?\n(type your name) ')
print(user_name + ", I'm thinking of a number between 1 and 100. Try to guess my number.")

def guess_num():
  global attempt_counter

  print('Attempts:', attempt_counter)
  user_guess = int(input('What number do you guess? '))
  if user_guess > computer_number:
    print('Your guess is too high, please try again.')
    attempt_counter += 1
    guess_num()
  elif user_guess < computer_number:
    print('Your guess is too low, please try again.')
    attempt_counter += 1
    guess_num()
  else:
    attempt_counter += 1
    print('Well done,', user_name, "! You found my number in", attempt_counter, "tries!")

guess_num()
