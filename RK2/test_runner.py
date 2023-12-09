import TDD_tests
import unittest

suite = unittest.TestLoader().loadTestsFromModule(TDD_tests)
results = unittest.TextTestRunner(verbosity=2).run(suite)