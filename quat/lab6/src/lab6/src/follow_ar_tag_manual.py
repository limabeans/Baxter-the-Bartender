#!/usr/bin/env python
import tf
import rospy
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3, Twist
import exp_quat_func as eqf
import ar_tag_subs as ar # return_rbt(trans,rot)->4x4 rbt, compute_twist(rbt)->(v,w)

listener = None

def follow_ar_tag(zumy, ar_tags):

    listener = tf.TransformListener()
    zumy_vel = rospy.Publisher('/%s/cmd_vel' % zumy, Twist, queue_size=2)
    rate = rospy.Rate(10)
    
    print "FACING TO AR TAG"
    error_old = None
    # turn to face the AR tag
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
        except:
            continue
        # YOUR CODE HERE
        #  orient the Zumy to face the tag
        v_vec3 = Vector3()
        v_vec3.x = trans[0]
        v_vec3.y = trans[1]
        v_vec3.z = trans[2]
        w_vec3 = Vector3()
        w_vec3.x = rot[0]
        w_vec3.y = rot[1]
        w_vec3.z = rot[2]

        twist = Twist()
        twist.linear = v_vec3
        twist.angular = w_vec3

        zumy_vel.publish(twist)












#### ignore rest of code
    print "MOVING TO AR TAG"
    error_old = None
    # move towards the AR tag
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
        except:
            continue
        # YOUR CODE HERE
        #  drive the zumy forward (forward is the X direction) close to the AR tag
        #  you can also fix deviations on the trajectory by adjusting the rotation
        #  as it moves forward
        
    print "ORIENTING TO AR TAG"
    # move towards the AR tag
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
        except:
            continue
        # YOUR CODE HERE
        #  orient the final orientation to the AR tag


    # Stop the zumy
    cmd = Twist()
    cmd.linear.x = 0
    cmd.linear.y = 0
    cmd.linear.z = 0
    cmd.angular.x = 0
    cmd.angular.y = 0
    cmd.angular.z = 0
    zumy_vel.publish(cmd)

if __name__=='__main__':
    rospy.init_node('follow_ar_tag_manual')
    if len(sys.argv) < 4:
        print('Use: follow_ar_tag_manual.py [ zumy name ] [ AR tag number for goal] [ AR tag number for Zumy] ')
        sys.exit()
    ar_tags = {}
    zumy_name = sys.argv[1]
    ar_tags['ar1'] = 'ar_marker_' + sys.argv[2]
    ar_tags['arZ'] = 'ar_marker_' + sys.argv[3]

    follow_ar_tag(zumy=zumy_name, ar_tags=ar_tags)
    rospy.spin()
