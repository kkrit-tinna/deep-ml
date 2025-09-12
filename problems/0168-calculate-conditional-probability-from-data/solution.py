def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    x_count = 0
    y_in_x_count = 0

    for xi, yi in data:
        if xi == x:
            x_count += 1
        if xi == x and yi == y:
            y_in_x_count += 1
    if x_count > 0:
        return round(y_in_x_count / x_count, 4)
    else:
        return 0.0