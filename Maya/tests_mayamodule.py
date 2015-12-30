"""
import sys

scriptfolder = 'c:\_STORAGE\dev\_all_tests-env\_allprojects\maya'

if scriptfolder not in sys.path:
    sys.path.insert(0, scriptfolder)

import test_mayascript as t_ms
reload(t_ms)

t_ms.main()
"""

import unittest
import mayascript
import maya.cmds

class ObjectCreateTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_sphere(self):
        sphere = mayascript.create_sphere()

        self.assertTrue(sphere)

    def test_create_poly_sphere(self):
        polysphere = mayascript.create_sphere(poly=True)
        self.assertEqual(maya.cmds.nodeType(polysphere), 'mesh')

def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ObjectCreateTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
