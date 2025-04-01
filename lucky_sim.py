import random

hort =random.random(1,2)

if hort == 1:
    hort = 'heads'

if hort == 2:
    hort = 'tails'

ask= input("Heads or Tails?")

if ask == "Heads" or "heads" and hort == 'heads':
    print('congrats')