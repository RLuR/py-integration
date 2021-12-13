import math
import py_integration
import unittest

class TestApproximatePi(unittest.TestCase):

    def approximation_function(self, x):
        return math.sqrt(1 - x**2)

    def test_riemann_approximation(self):
        approximate_py_half = py_integration.riemann_integrate(self.approximation_function, -1, 1)

        error = abs(math.pi - approximate_py_half*2)

        # less then 1 percent error
        assert error < math.pi /100

