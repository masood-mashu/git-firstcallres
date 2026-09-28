"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitFirstCallRes.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.fcr_eligibility_calculator import *
from tools.repeat_contact_detector import *
from tools.kb_article_matcher import *

class TestGitFirstCallResPredictability(unittest.TestCase):

    def test_fcr_eligibility_calculator(self):
        res = calculate_fcr('{"agent_replies_count": 1, "was_reopened": false}')
        self.assertTrue(res["fcr_achieved"])
        self.assertEqual(res["status"], "FCR_VERIFIED")

    def test_repeat_contact_detector(self):
        res = detect_repeat_contact(24.0)
        self.assertTrue(res["repeat_contact"])
        self.assertEqual(res["status"], "REPEAT_CONTACT_DETECTED")

    def test_kb_article_matcher(self):
        res = match_kb_article("Password reset")
        self.assertTrue(res["kb_article_exists"])
        self.assertEqual(res["status"], "KB_DOCUMENTED")


if __name__ == "__main__":
    unittest.main()
