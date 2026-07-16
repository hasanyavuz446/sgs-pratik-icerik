#!/usr/bin/env python3
import importlib.util
import os
import unittest


AUDIT_PATH = os.path.join(os.path.dirname(__file__), "..", "audit.py")
SPEC = importlib.util.spec_from_file_location("sgs_audit", AUDIT_PATH)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class SgsAuditTest(unittest.TestCase):
    def test_short_nonperiodic_sequence_is_allowed(self):
        self.assertFalse(audit.letter_pattern("ABCDEBACDE"))

    def test_repeating_sequence_is_rejected(self):
        self.assertTrue(audit.letter_pattern("ABCDEABCDEABCDE"))


if __name__ == "__main__":
    unittest.main()
