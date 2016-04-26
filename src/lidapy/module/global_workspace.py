#!/usr/bin/env python
'''
Created on Apr 20, 2016

@author: Sean Kugele
'''
from lidapy.framework.module import FrameworkModule
from lidapy.framework.msg import Coalition, ConsciousContent


class GlobalWorkspaceModule(FrameworkModule):
    def __init__(self):
        super(GlobalWorkspaceModule, self).__init__("GlobalWorkspaceModule")

    def add_publishers(self):
        pubs = [{"topic": "/lida/global_broadcast", "msg_type": ConsciousContent.msg_type()}]
        for pub in pubs:
            super(GlobalWorkspaceModule, self)._add_publisher(pub["topic"], pub["msg_type"])

    def add_subscribers(self):
        subs = [{"topic": "/lida/workspace_coalitions", "msg_type": Coalition.msg_type()}]
        for sub in subs:
            super(GlobalWorkspaceModule, self)._add_subscriber(sub["topic"], sub["msg_type"])



if __name__ == '__main__':

    try:
        module = GlobalWorkspaceModule()
        module.run()

    except Exception as e:
        print e

    finally:
        pass
