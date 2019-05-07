
import json
import tuning_metrics.space


def load_kernel_tuner(filename, key="time", ascending_metric=False, name=""):
    with open(filename, "r") as file:
        configurations = json.load(file)
    performance_space = tuning_metrics.space.PerformanceSpace(ascending_metric=ascending_metric, name=name)
    for configuration in configurations:
        performance_space.add_element(configuration[key])
    return performance_space
