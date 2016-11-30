# Gambler's Falacy

A simple simulation for a mean reversion betting strategy at a roulette table (HINT: It loses horribly).

Assumes you want to bet red after a streak of blacks and bet black after a streak of reds.
You can specify the number of rolls, the streak required before starting to bet, and the number of bets in a row you want to place after the streak.

See the bottom of the ```gambler_falacy.py``` to tweak those options.

```
$ python gambler_falacy.py
Simulating 1000000 rolls
Starting to bet after a streak of 10 reds or blacks
Betting for 5 rounds following the streak
Placed 3100 bets
Won 1476
Lost 1624
Percent won: 47.6129032258%
```
