#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def talker():

    # Create a publisher object -> Publisher(<topic name>, <message type>, queue_size)
    publisher = rospy.Publisher("talker", String, queue_size=10)

    # Initialize the ros node -> init_node(<node name>)
    rospy.init_node("talker_node")

    # publisher rate in Hz
    rate = rospy.Rate(10)

    # Publish until the node is not closed
    while not rospy.is_shutdown():

        message = "Hello this is the message from talker"

        # publish the message
        publisher.publish(message)

        # Logging the info in the console
        rospy.loginfo("Message published successfully")

        # Wait until the rate defined
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
