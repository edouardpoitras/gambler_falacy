import random

# Constants
BLACK = -1
RED = 1
ZERO = 0

# Standard american roulette wheel
NUM_BLACKS = 18
NUM_REDS = 18
NUM_COLORS = NUM_BLACKS + NUM_REDS
NUM_ZEROS = 2
NUM_OPTIONS = NUM_COLORS + NUM_ZEROS

def get_roll():
    """
    Simulates a round of roulette.
    Assumes an un-biased table :)
    """
    num = random.randint(1, NUM_OPTIONS)
    if num <= NUM_BLACKS: return BLACK
    elif num <= NUM_COLORS: return RED
    return ZERO

def check_odds(iterations=1000000):
    """
    Just a sanity check to ensure the odds are in-deed accurate.
    A standard american roulette table has the following odds:
        BLACK: 46.37%
        RED: 46.37%
        House Edge: 5.26%
        [http://www.rouletteonline.net/odds/]

    Ensure you get similar results with high iterations.
    """
    results = {BLACK: 0, RED: 0, ZERO: 0, 'total': 0}
    for _ in range(iterations):
        roll = get_roll()
        results[roll] += 1
        results['total'] += 1
    black_odds = float(results[BLACK]) / results['total'] * 100
    red_odds = float(results[RED]) / results['total'] * 100
    zero_odds = float(results[ZERO]) / results['total'] * 100
    print 'Black Odds: %s%%' %black_odds
    print 'Red Odds: %s%%' %red_odds
    print 'Zero Odds: %s%%' %zero_odds

def mean_reversion(num_rolls=1000000, streak=10, betting_rounds=5):
    """
    Attempts a mean reversion betting strategy (gambler's falacy) where we
    wait for an abnormal streak of blacks or reds and then bet the opposite
    for X number of bets.
    """
    print 'Simulating %s rolls' %num_rolls
    print 'Starting to bet after a streak of %s reds or blacks' %streak
    print 'Betting for %s rounds following the streak' %betting_rounds
    roll_history = []
    currently_betting = None
    currently_betting_rounds = 0
    bets = 0
    wins = 0
    losses = 0
    for _ in range(num_rolls):
        roll = get_roll()
        roll_history.append(roll)
        if currently_betting is not None:
            # We have already hit our streak and are in the process of betting
            currently_betting_rounds += 1
            bets += 1
            if roll == currently_betting: # We won the bet
                wins += 1
            else: # We lost the bet
                losses += 1
            if currently_betting_rounds == betting_rounds:
                # We've bet enough times since the streak
                currently_betting_rounds = 0
                currently_betting = None
        else:
            # We're still waiting on an abnormal streak of blacks or reds.
            check = roll_history[-streak:]
            if len(check) < streak:
                # Not enough rolls yet
                continue
            if ZERO not in check: # Only care about color streaks
                if BLACK not in check: # Red streak
                    currently_betting = BLACK
                elif RED not in check: # Black streak
                    currently_betting = RED
    # Print the results
    print 'Placed %s bets' %bets
    print 'Won %s' %wins
    print 'Lost %s' %losses
    if bets > 0: print 'Percent won: %s%%' %(float(wins) / bets * 100)

if __name__ == '__main__':
    # Spin the wheel 1 million times
    rolls = 1000000
    # Wait for a 10 black or 10 red streak
    streak = 10
    # Once we have a streak, bet the opposite for 5 rounds
    betting_rounds = 5
    mean_reversion(rolls, streak, betting_rounds)
