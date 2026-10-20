import numpy as np
def simulate_dice_sum(num_rolls, seed=0):
    rng = np.random.RandomState(seed)
    d1 = rng.randint(1, 7, size=num_rolls)
    d2 = rng.randint(1, 7, size=num_rolls)
    sums = d1 + d2

    # counts for sums 2..12 -> indices 0..10
    counts = np.bincount(sums - 2, minlength=11)
    empirical = counts / num_rolls

    s = np.arange(2, 13)
    theoretical = (6 - np.abs(s - 7)) / 36

    return empirical, theoretical