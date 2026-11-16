def random_pick_with_weight(weights, r):
    # weights: list of positive integers
    # r: float in [0, 1)
    # return the selected index (int)
    target = r * sum(weights)
    cum = 0

    for i, w in enumerate(weights):
        cum += w

        if cum > target:
            return i