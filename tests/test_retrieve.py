import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from training_llm.retrieve import answer_with_citations

PASSAGES = [
    {"doc_id": "sample_manual", "section": "1.2", "text": "Inspect the hydraulic line for leaks before each flight."},
    {"doc_id": "sample_manual", "section": "4.1", "text": "Record completed maintenance in the logbook."},
]


class RetrieveTest(unittest.TestCase):
    def test_answer_carries_citation(self):
        result = answer_with_citations("How do I inspect the hydraulic line?", PASSAGES)
        self.assertFalse(result["abstained"])
        self.assertEqual(result["answer"][0]["citation"], "sample_manual 1.2")

    def test_abstains_without_support(self):
        result = answer_with_citations("What is the weather on Mars?", PASSAGES)
        self.assertTrue(result["abstained"])


if __name__ == "__main__":
    unittest.main()
