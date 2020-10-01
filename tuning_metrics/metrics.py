

import math


def tuning_score_distribution(performance_space, nbins=10):
    """
    Computes TS_d, the tuning score based on the distribution of configurations in the performance space.
    """

    histogram = performance_space.histogram(nbins)
    if (histogram[9] / performance_space.size()) >= 0.1:
        return ((0.5 / 0.9) * (histogram[9] / performance_space.size())) + 1 - (0.5 / 0.9)
    else:
        return (0.5 / 0.1) * (histogram[9] / performance_space.size())


def tuning_score_size(performance_space, peak):
    """
    Computes TS_s, the tuning score based on the size of the performance space compared to the achievable performance.
    """

    return math.sqrt(performance_space.top() / peak)
