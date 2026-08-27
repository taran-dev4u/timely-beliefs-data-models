"""Unit tests for DataFrame belief alignment."""
import unittest
from timely_beliefs_models.sources import BeliefSource
from timely_beliefs_models.dataframe_utils import align_belief_series

class TestDFUtils(unittest.TestCase):
    def test_alignment_no_nans(self):
        s = [BeliefSource("B"), BeliefSource("A")]
        res = align_belief_series(s, [2.0, 1.0])
        self.assertEqual(list(res.index), ["A", "B"])
        self.assertFalse(res.isna().any())
