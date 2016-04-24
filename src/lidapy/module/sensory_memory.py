#!/usr/bin/env python
'''
Created on Apr 20, 2016

@author: Sean Kugele
'''
from lidapy.framework.module import FrameworkModule


class SensoryMemoryModule(FrameworkModule):

    def __init__(self):
        FrameworkModule.__init__(self, "SensoryMemoryModule")
        return



if __name__ == '__main__':

    try:
        module = SensoryMemoryModule()
        module.run(10)

    except Exception as e:
        print e

    finally:
        pass
