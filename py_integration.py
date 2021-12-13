import argparse
import random
import numpy as np
import math

MONTE_CARLO = 0
RIEMANN = 1

def integrate_string(functionstring, lower_boundry, upper_boundry, method=1, iterations=10000):
    function = _parse_Function(functionstring)

    if method == 0:
        return monte_carlo_integrate(function, lower_boundry, upper_boundry, iterations)
    if method == 1:
        return riemann_integrate(function, lower_boundry, upper_boundry, iterations)

def riemann_integrate(function, lower_boundry, upper_boundry, iterations=10000):
    step_size = (upper_boundry - lower_boundry)/iterations
    steps = np.arange(lower_boundry, upper_boundry, step_size)
    function_array = np.vectorize(function)
    results = function_array(steps)
    return np.mean(results) * (upper_boundry - lower_boundry)

def monte_carlo_integrate(function, lower_boundry, upper_boundry, iterations, min_height = None, max_height= None):

    if min_height is None or max_height is None:
        min_height, max_height = _generate_y_boundries(function, lower_boundry, upper_boundry, iterations)

    results = 0
    for step in range(1, iterations):
        random_point = _generate_random_point(lower_boundry, upper_boundry, min_height, max_height)
        stepresult = _monte_Carlostep(function, random_point)
        if stepresult:
            results += 1

    minresult = (upper_boundry - lower_boundry) * (min_height)
    return minresult + (upper_boundry - lower_boundry) * (max_height - min_height) * results / iterations

def _generate_random_point(lower_boundry, upper_boundry, min_height, max_height):
    return [random.uniform(lower_boundry,upper_boundry), random.uniform(min_height, max_height)]


def _parse_Function(expression):
    funcstr= '''\
def f(x):
    return {e}'''.format(e=expression)
    exec(funcstr, globals())
    return f


def _generate_y_boundries(function, lower_x_boundry, upper_x_boundry, iterations=1000):
    step_size = (upper_x_boundry - lower_x_boundry) / iterations
    steps = np.arange(lower_x_boundry, upper_x_boundry, step_size)
    function_array = np.vectorize(function)
    results = function_array(steps)
    return np.min(results), np.max(results)


def _monte_Carlostep(function, point):
    if point[1] < function(point[0]):
        return True
    else:
        return False


if __name__ == '__main__':
    argumentparser = argparse.ArgumentParser()
    argumentparser.add_argument("function", type=str)
    argumentparser.add_argument("lower_boundry", type=float)
    argumentparser.add_argument("upper_boundry", type=float)
    args=argumentparser.parse_args()

    iterations = 10000

    print(f"Monte Carlo approximation: {integrate_string(args.function, args.lower_boundry, args.upper_boundry, MONTE_CARLO, iterations)}")
    print(f"Riemann approximation: {integrate_string(args.function, args.lower_boundry, args.upper_boundry, RIEMANN, iterations)}")
