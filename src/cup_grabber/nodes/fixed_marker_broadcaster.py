#!/usr/bin/env python

import roslib
roslib.load_manifest('cup_grabber')
import rospy
import tf


if __name__ == '__main__':
    rospy.init_node('fixed_marker_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        br.sendTransform( (0.0,0.0,0.0),
                          (0.122,0.0,0.0,.993),
                          rospy.Time.now(),
                          'fixed_head_camera',
                          'head_camera')
        rate.sleep()
