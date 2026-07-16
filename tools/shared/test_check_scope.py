#!/usr/bin/env python3
import importlib.util
import os
import unittest


PATH = os.path.join(os.path.dirname(__file__), "check_scope.py")
SPEC = importlib.util.spec_from_file_location("check_scope", PATH)
check_scope = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_scope)


class ScopeOwnershipTest(unittest.TestCase):
    def test_sgs_paths(self):
        self.assertEqual(check_scope.owner("tools/sgs/audit.py"), "sgs")
        self.assertEqual(check_scope.owner("content/finansal_muhasebe/a.json"), "sgs")
        self.assertEqual(check_scope.owner("content/v2/manifests/sgs.json"), "sgs")

    def test_smmm_paths(self):
        self.assertEqual(check_scope.owner("tools/smmm/audit/audit.py"), "smmm")
        self.assertEqual(check_scope.owner("content/yeterlilik/a.json"), "smmm")
        self.assertEqual(check_scope.owner("content/v2/manifests/smmm.json"), "smmm")

    def test_shared_paths(self):
        self.assertEqual(check_scope.owner("tools/shared/manifest_merge.py"), "shared")
        self.assertEqual(check_scope.owner("content/v2/manifest.json"), "shared")


if __name__ == "__main__":
    unittest.main()
