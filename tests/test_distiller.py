"""Unit tests for diff-aware-code-distiller."""
import unittest
from diff_aware_code_distiller.distiller import DiffAwareCodeDistiller


class TestDiffAwareCodeDistiller(unittest.TestCase):
    def test_distill_functions(self):
        d = DiffAwareCodeDistiller()
        diff = """--- a/mod.py
+++ b/mod.py
+def compute_sum(a, b):
+    return a + b
"""
        res = d.distill(diff)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].filename, "mod.py")
        self.assertIn("compute_sum", res[0].modified_symbols)
        self.assertEqual(res[0].added_lines, 2)
