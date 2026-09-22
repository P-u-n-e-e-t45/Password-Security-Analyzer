import unittest
from app.analyzer import check_password
from app.entropy import calculate_entropy
from app.crack_time import search_space

class TestPasswordAnalyzer(unittest.TestCase):
    def test_common_password(self):
        result = check_password("password")
        self.assertTrue(result["is_common"])
        self.assertIn("BLACKLISTED", result["strength"])

    def test_strong_mixed_password(self):
        result = check_password("T9!mQ7#zLp2@xK8")
        self.assertEqual(result["score"], 6)
        self.assertFalse(result["is_common"])
        self.assertGreater(result["entropy"], 0)

    def test_entropy_increases_with_length(self):
        self.assertGreater(calculate_entropy("Ab12xyz"), calculate_entropy("Ab1!"))

    def test_search_space(self):
        self.assertEqual(search_space(3, 26), 17576)

if __name__ == "__main__":
    unittest.main()
