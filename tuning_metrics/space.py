
import numpy


class PerformanceSpace:
    """
    The tuning performance space.
    """

    def add_element(self, element):
        """
        Add one element to the performance space.
        """

        self.values = numpy.append(self.values, element)

    def clear(self):
        """
        Clear the space removing all previously added elements.
        """

        self.values = numpy.empty([0], dtype=numpy.float64)
        if self.ascending_metric:
            self.best = numpy.finfo(numpy.float64).min
            self.worst = numpy.finfo(numpy.float64).max
        else:
            self.best = numpy.finfo(numpy.float64).max
            self.worst = numpy.finfo(numpy.float64).min
    
    def size(self):
        """
        Return the size of the performance space.
        """

        return len(self.values)
    
    def top(self):
        """
        Return the optimal performance.
        """

        if self.ascending_metric:
            return self.values.max()
        else:
            return self.values.min()

    def bottom(self):
        """
        Return the worst performance.
        """

        if self.ascending_metric:
            return self.values.min()
        else:
            return self.values.max()
    
    def histogram(self, nbins=10):
        """
        Return the performance histogram of the space.
        """

        if self.ascending_metric:
            return numpy.histogram(self.values, bins=nbins)[0]
        else:
            return numpy.flip(numpy.histogram(self.values, bins=nbins)[0])

    def average(self):
        """
        Return the average performance in the space.
        """

        return numpy.average(self.values)

    def median(self):
        """
        Return the median performance in the space.
        """

        return numpy.median(self.values)

    def standard_deviation(self):
        """
        Return the standard deviation of the performance space.
        """

        return numpy.std(self.values)
    
    def __init__(self, ascending_metric=True, name=""):
        self.ascending_metric = ascending_metric
        self.name = name
        self.values = numpy.empty([0], dtype=numpy.float64)
        if ascending_metric:
            self.best = numpy.finfo(numpy.float64).min
            self.worst = numpy.finfo(numpy.float64).max
        else:
            self.best = numpy.finfo(numpy.float64).max
            self.worst = numpy.finfo(numpy.float64).min
