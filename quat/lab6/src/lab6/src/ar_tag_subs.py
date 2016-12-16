#!/usr/bin/env python
import tf
import rospy
import sys
import math
import numpy as np
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Transform, Vector3
import kin_func_skeleton as kfs
import exp_quat_func as eqf

listener = None

def return_rbt(trans, rot):
    """
    Prints out the 4x4 rigid body transformation matrix from quaternions

    Input:
        (3,) array - translation ector
        (4,) array - rotation vector in quaternions
    """

    #YOUR CODE HERE
    rot = np.array(list(rot))
    trans = np.array(list(trans))
    omega, theta = eqf.quaternion_to_exp(rot)
    ans = eqf.create_rbt(omega, theta, trans)
    # print ans
    return ans

def compute_twist(rbt):
    """
    Computes the corresponding twist for the rigid body transform

    Input:
        rbt - (4,4) ndarray 

    Output:
        v - (3,) array
        w - (3,) array
    """
    #YOUR CODE HERE
    rbt = list(rbt)
    print 'here'
    R=np.array([ [rbt[0][0],rbt[0][1],rbt[0][2]] , [rbt[1][0],rbt[1][1],rbt[1][2]] , [rbt[2][0],rbt[2][1],rbt[2][2] ] ])
    # p = np.array([[rbt[0][3]], [rbt[1][3]], [rbt[2][3]]])
    p = np.array([rbt[0][3],rbt[1][3],rbt[2][3]])
    omega,theta = eqf.find_omega_theta(R)
    v = eqf.find_v(omega, theta, p)
    return (v,omega)

if __name__=='__main__':
    rospy.init_node('ar_tags_subs')
    if len(sys.argv) < 4:
        print('Use: ar_tag_subs.py [ AR tag number ] [ AR tag number ] [ AR tag number ] ')
        sys.exit()
    ar_tags = {}
    ar_tags['ar0'] = 'ar_marker_' + sys.argv[1]
    ar_tags['ar1'] = 'ar_marker_' + sys.argv[2]
    ar_tags['arZ'] = 'ar_marker_' + sys.argv[3]

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['arZ'], ar_tags['ar1'], rospy.Time(0))
            rbt = return_rbt(trans=trans, rot=rot)
            print('gab between ' + ar_tags['arZ'] + ' and ' + ar_tags['ar1'])
            print rbt
            twist = compute_twist(rbt=rbt)
            print('twist between ' + ar_tags['arZ'] + ' and ' + ar_tags['ar1'])
            print twist
        except:
            1

        try:
            (trans, rot) = listener.lookupTransform(ar_tags['ar0'], ar_tags['ar1'], rospy.Time(0))
            rbt = return_rbt(trans=trans, rot=rot)
            print('gab between ' + ar_tags['ar0'] + ' and ' + ar_tags['ar1'])
            print rbt
            twist = compute_twist(rbt=rbt)
            print('twist between ' + ar_tags['ar0'] + ' and ' + ar_tags['ar1'])
            print twist
        except:
            1
            
        try:
            (trans, rot) = listener.lookupTransform(ar_tags['ar0'], ar_tags['arZ'], rospy.Time(0))
            rbt = return_rbt(trans=trans, rot=rot)
            print('gab between ' + ar_tags['ar0'] + ' and ' + ar_tags['arZ'])
            print rbt
            twist = compute_twist(rbt=rbt)
            print('twist between ' + ar_tags['ar0'] + ' and ' + ar_tags['arZ'])
            print twist
        except:
            1

        rate.sleep()
