
import numpy as np


class PerformanceSpace:
    """
    The tuning performance space.
    """

    def add_element(self, element):
        """
        Add one element to the performance space.
        """

        np.append(self.values, element)
        if self.ascending_metric:
            # The performance metric is ascending (higher is better)
            if element > self.best:
                self.best = element
            if element < self.worst:
                self.worst = element
        else:
            # The performance metric is descending (lower is better)
            if element < self.best:
                self.best = element
            if element > self.worst:
                self.worst = element
    
    def clear(self):
        """
        Clear the space removing all previously added elements.
        """

        self.values = np.array()
        self.best = 0.0
        self.worst = 0.0
    
    def size(self):
        """
        Return the size of the performance space.
        """

        return len(self.values)
    
    def optimum(self):
        """
        Return the optimal performance.
        """

        return self.best

    def bottom(self):
        """
        Return the worst performance.
        """

        return self.worst
    
    def histogram(self, nbins=10):
        """
        Return the performance histogram of the space.
        """

        return np.histogram(self.values, bins=nbins)
    
    def __init__(self, ascending_metric=True, name=""):
        self.ascending_metric = ascending_metric
        self.name = name
        self.values = np.array()
        self.best = 0.0
        self.worst = 0.0
