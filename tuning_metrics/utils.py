
import json
import tuning_metrics.space


def load_kernel_tuner(filename, key="time", ascending_metric=False, name=""):
    """
    Load JSON files produced by kernel_tuner.

    :param filename: JSON file containing the tuning results.
    :param key: The key of the metric used for performance results; the default is "time".
    :param ascending_metric: True if the metric is ascending, False otherwise; the default is False.
    :param name: The name of the performance space; the default is "".
    :return: A PerformanceSpace object.
    """

    with open(filename, "r") as file:
        configurations = json.load(file)
    performance_space = tuning_metrics.space.PerformanceSpace(ascending_metric=ascending_metric, name=name)
    for configuration in configurations:
        performance_space.add_element(configuration[key])
    return performance_space
