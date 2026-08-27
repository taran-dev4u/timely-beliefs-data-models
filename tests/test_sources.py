"""Unit tests verifying strict total ordering and sort stability."""

import unittest
from timely_beliefs_models.sources import BeliefSource

class TestBeliefSourceOrdering(unittest.TestCase):
    def test_strict_ordering(self):
        s1 = BeliefSource("Model_Alpha")
        s2 = BeliefSource("Model_Beta")
        self.assertTrue(s1 < s2)
        self.assertFalse(s2 < s1)

    def test_duplicate_name_tiebreaker(self):
        s1 = BeliefSource("DuplicateName")
        s2 = BeliefSource("DuplicateName")
        # Ordering must be deterministic and total: either s1 < s2 or s2 < s1
        self.assertTrue((s1 < s2) or (s2 < s1))
        self.assertFalse((s1 < s2) and (s2 < s1))

    def test_list_sorting(self):
        sources = [BeliefSource("Sensor_C"), BeliefSource("Sensor_A"), BeliefSource("Sensor_B")]
        sorted_sources = sorted(sources)
        self.assertEqual([s.name for s in sorted_sources], ["Sensor_A", "Sensor_B", "Sensor_C"])

if __name__ == "__main__":
    unittest.main()
