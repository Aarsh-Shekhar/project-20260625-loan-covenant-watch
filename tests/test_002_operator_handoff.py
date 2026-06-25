import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="borrower-002", exposure=13767, signal=0.328, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
