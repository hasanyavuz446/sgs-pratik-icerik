#!/usr/bin/env python3
import importlib.util
import os
import unittest


PATH = os.path.join(os.path.dirname(__file__), "manifest_merge.py")
SPEC = importlib.util.spec_from_file_location("manifest_merge", PATH)
manifest_merge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(manifest_merge)


class ManifestMergeTest(unittest.TestCase):
    def test_existing_sources_merge_without_duplicate_keys(self):
        result = manifest_merge.merged()
        keys = [(pack["programIds"][0], pack["file"]) for pack in result["packs"]]
        self.assertEqual(len(keys), len(set(keys)))


if __name__ == "__main__":
    unittest.main()
