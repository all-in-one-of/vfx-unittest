"""
shelf tool:
    import sys

    modulepath = 'c:/_STORAGE/dev/vfx-unittest/Houdini'

    if modulepath not in sys.path:
        sys.path.append(modulepath)

    import tests_houdinimodule as thm
    reload(thm)

    thm.main()
"""


import unittest
import houdinimodule
import hou


class HoudinimoduleTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_geo_in_root(self):
        geo = houdinimodule.create_geo()

        self.assertEqual(geo.type(), hou.nodeType('Object/geo'))


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(HoudinimoduleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
