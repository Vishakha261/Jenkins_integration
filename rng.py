from random import randint

min_number = 143
max_number = 300

if (max_number < min_number): 
  print('Invalid input - shutting down...'
else:
  rnd_number = randint(min_number, max_number)
  print(rnd_number)

