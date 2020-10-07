
from collections.abc import Callable
import json
import tuning_metrics.space


def load_kernel_tuner(filename: str, key: str, ascending_metric: bool, name: str, transform: Callable) \
        -> tuning_metrics.space.PerformanceSpace:
    """
    Load JSON files produced by kernel_tuner.

    :param filename: JSON file containing the tuning results.
    :param key: The key of the metric used for performance results; the default is "time".
    :param ascending_metric: True if the metric is ascending, False otherwise; the default is False.
    :param name: The name of the performance space; the default is "".
    :param transform: Function to be applied to all values loaded from file.
    :return: A PerformanceSpace object containing the specified metric.
    """

    if not key:
        key = "time"
    if not ascending_metric:
        ascending_metric = False
    if not name:
        name = ""
    if not transform:
        transform = None
    with open(filename, "r") as file:
        configurations = json.load(file)
    performance_space = tuning_metrics.space.PerformanceSpace(ascending_metric=ascending_metric, name=name)
    for configuration in configurations:
        if transform is not None:
            performance_space.add_element(transform(configuration[key]))
        else:
            performance_space.add_element(configuration[key])
    return performance_space
