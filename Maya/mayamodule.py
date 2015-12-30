"""
import sys

scriptfolder = 'c:\_STORAGE\dev\_all_tests-env\_allprojects\maya'

if scriptfolder not in sys.path:
    sys.path.insert(0, scriptfolder)

import mayascript as ms
reload(ms)

ms.main()
"""


import maya.cmds


def create_sphere(poly=False):
    if poly:
        sphere = maya.cmds.polySphere()

    else:
        sphere = maya.cmds.sphere()

    sphere = maya.cmds.pickWalk(direction='down')
    print(sphere)
    return sphere




def main():
    sphere = create_sphere()
