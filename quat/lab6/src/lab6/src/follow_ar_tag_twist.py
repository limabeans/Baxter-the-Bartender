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
    zumy_vel = rospy.Publisher('%s/cmd_vel' % zumy, Twist, queue_size=2)
    rate = rospy.Rate(10)
    print ar_tags
    
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
        except:
            continue

        # YOUR CODE HERE
        #  The code should compute the twist given 
        #  the translation and rotation between arZ and ar1
        #  Then send it publish it to the zumy
        v,w = ar.compute_twist(ar.return_rbt(trans,rot))
        print v
        print w
        v_vec3 = Vector3()
        v_vec3.x = v[0]
        v_vec3.y = v[1]
        v_vec3.z = v[2]
        w_vec3 = Vector3()
        w_vec3.x = w[0]
        w_vec3.y = w[1]
        w_vec3.z = w[2]

        twist = Twist()
        twist.linear = v_vec3
        twist.angular = w_vec3

        zumy_vel.publish(twist)
        
  
if __name__=='__main__':
    rospy.init_node('follow_ar_tag_twist')
    if len(sys.argv) < 4:
        print('Use: follow_ar_tag_manual.py [ zumy name ] [ AR tag number for goal] [ AR tag number for Zumy] ')
        sys.exit()
    ar_tags = {}
    zumy_name = sys.argv[1]
    ar_tags['ar1'] = 'ar_marker_' + sys.argv[2]
    ar_tags['arZ'] = 'ar_marker_' + sys.argv[3]

    follow_ar_tag(zumy=zumy_name, ar_tags=ar_tags)
    rospy.spin()
