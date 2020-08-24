#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

# This function is called when the subscriber gets the message from the publisher


def callback(data):

    rospy.loginfo("Printing the data sent by publisher")
    rospy.loginfo(data.data)


def listener():

    # Declare the subscriber to subscribe the topic talker which publishes integer
    # message
    rospy.Subscriber('talker', Int16, callback)

    # Initialize the ros node for subscriber
    rospy.init_node("listener_node")

    rospy.loginfo("Listening...")

    # This command keeps python from existing until the node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
