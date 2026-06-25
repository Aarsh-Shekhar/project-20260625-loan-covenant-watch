import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import score_record


class DepthCheck14(unittest.TestCase):
    def test_014_scenario_analysis(self):
        record = Record(id="borrower-014", exposure=83359, signal=0.588, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
