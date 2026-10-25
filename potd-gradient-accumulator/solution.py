def gradient_accumulator(
    theta: float, eta: float, microbatches: list[tuple[int, float]]
) -> tuple[float, float]:
    """
    microbatches: list of (n_j, g_j) pairs, n_j examples with mean
    gradient g_j.

    g = sum(n_j * g_j) / sum(n_j)   (example-weighted mean, NOT the mean
    of the microbatch means).
    theta' = theta - eta * g.

    Return (g, theta_prime).
    """
    # TODO: weight by example count, divide exactly once.
    num = 0
    den = 0
    for mb in microbatches:
        # mb1 -> 5, 3
        # mb2 -> 3, 4
        # (5*3 + 3*4) / (5+3)
        num += mb[0] * mb[1]
        den += mb[0]
    g = num/den
    theta_prime = theta - eta * g
    return (g, theta_prime)
