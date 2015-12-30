"""
shelf tool:
    import sys

    modulepath = 'c:/_STORAGE/dev/vfx-unittest/Houdini'

    if modulepath not in sys.path:
        sys.path.append(modulepath)

    import houdinimodule as hm
    reload(hm)

    hm.main()
"""


import hou


def create_geo(parent='/obj'):
    geo = hou.node(parent).createNode('geo')

    return geo


def main():
    create_geo()
