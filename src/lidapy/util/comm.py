#!/usr/bin/env python
'''
Created on Apr 21, 2016

@author: Sean Kugele
'''
import rospy


def initialize(name):
    rospy.init_node(name)
    return


def getPublisher(topic, msg_type, queue_size=0):
    return rospy.Publisher(topic, msg_type, queue_size=queue_size)


def registerSubscriber(topic, msg_type, callback, callback_args=[]):
    rospy.Subscriber(topic, msg_type, callback=callback, callback_args=callback_args)
    return


def publishMessage(publisher, msg):
    publisher.publish(msg.serializable_msg)
    return


def run(pubRate):
    # set the message publication rate
    rate = rospy.Rate(pubRate)

    while not rospy.is_shutdown():
        rate.sleep()
    return
