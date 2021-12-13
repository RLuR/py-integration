import math
import py_integration
import unittest

class TestApproximatePi(unittest.TestCase):

    # The definite integral of this function between -1 and 1 equals pi/2
    def approximation_function(self, x):
        return math.sqrt(1 - x**2)

    def test_riemann_approximation(self):
        approximate_py_half = py_integration.riemann_integrate(self.approximation_function, -1, 1)

        error = abs(math.pi - approximate_py_half*2)

        # less then 1 percent error
        assert error < math.pi /100

    def test_monte_carlo_approximation(self):
        approximate_py_half = py_integration.monte_carlo_integrate(self.approximation_function, -1, 1)

        error = abs(math.pi - approximate_py_half*2)

        # less then 1 percent error
        assert error < math.pi /100

