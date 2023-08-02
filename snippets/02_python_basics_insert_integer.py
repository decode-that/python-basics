# Inserting an integer into a string
# Feierabend Countdown
import time
steps = 5

for i in range(steps):
    if i < 4:
        print('{}s bis Feierabend'.format(steps-(i+1)))
        time.sleep(1)
    else:
        print('Feierabend!!!')