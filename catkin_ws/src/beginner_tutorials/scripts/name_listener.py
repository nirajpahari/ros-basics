#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# This function is called when the subscriber gets the message from the publisher


def callback(data):

    rospy.loginfo("Printing the data sent by publisher")
    rospy.loginfo(data.data)


def name_listener():

    # Declare the subscriber to subscribe the topic talker which publishes string
    # message
    rospy.Subscriber('talker', String, callback)

    # Initialize the ros node for subscriber
    rospy.init_node("listener_node")

    rospy.loginfo("Listening...")

    # This command keeps python from existing until the node is stopped
    rospy.spin()


if __name__ == '__main__':
    name_listener()
