
import numpy as np


class PerformanceSpace:
    """
    This class represents the tuning performance space.
    """

    def add_element(self, element):
        """
        Add one element to the performance space.
        """

        self.values.append(element)
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

        self.values.clear()
        self.best = 0.0
        self.worst = 0.0
    
    def size(self):
        """
        Return the size of the performance space.
        """

        return len(self.values)
    
    def optimum(self):
        """
        Return the value of the optimal performance.
        """

        return self.best
    
    def histogram(self, nbins=10):
        """
        Returns the performance histogram of the space.
        """

        return np.histogram(self.values, bins=nbins)
    
    def __init__(self, ascending_metric=True, name=""):
        self.ascending_metric = ascending_metric
        self.name = name
        self.values = []
        self.best = 0.0
        self.worst = 0.0
