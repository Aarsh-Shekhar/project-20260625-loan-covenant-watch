import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="borrower-017", exposure=15115, signal=0.681, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
