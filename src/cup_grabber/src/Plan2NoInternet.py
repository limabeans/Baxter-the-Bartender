#!/usr/bin/env python
import rospy
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg
from std_msgs.msg import String
from visualization_msgs.msg import Marker
from cup_grabber.srv import MultiARPose, ARPose
import os

import baxter_interface
import baxter_external_devices

baxter_gripper=baxter_interface.gripper
CHECK_VERSION=baxter_interface.CHECK_VERSION

from copy import copy
import actionlib


def requestIK(link_name,group_name,p,o,compute_ik):
    px,py,pz=p
    ox,oy,oz,ow=o
    request = GetPositionIKRequest()
    request.ik_request.group_name = group_name
    request.ik_request.ik_link_name = link_name
    request.ik_request.attempts = 10000
    request.ik_request.pose_stamped.header.frame_id = "head_camera"
    request.ik_request.pose_stamped.pose.position.x = px
    request.ik_request.pose_stamped.pose.position.y = py
    request.ik_request.pose_stamped.pose.position.z = pz
    request.ik_request.pose_stamped.pose.orientation.x = ox
    request.ik_request.pose_stamped.pose.orientation.y = oy
    request.ik_request.pose_stamped.pose.orientation.z = oz
    request.ik_request.pose_stamped.pose.orientation.w = ow
    try:
        # print request
        print 'finding ik....'
        response = compute_ik(request)
        print 'moveIt succeeded'
        # print(response)
        group = MoveGroupCommander(group_name)
        group.set_pose_target(request.ik_request.pose_stamped)
        group.go()
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

########################################################################################


def main():
    tags={}
    cup_tags=[]

    #Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    rospy.init_node('service_query')
    right_gripper = baxter_gripper.Gripper('right')
    left_gripper = baxter_gripper.Gripper('left')
    right_gripper.calibrate()
    left_gripper.calibrate()

    #Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
    rospy.wait_for_service('fixed_multi_service')
    get_ar=rospy.ServiceProxy('fixed_multi_service', ARPose)

    tag3=get_ar(3)
    tag4=get_ar(4)
    cup_tags.append(tag3)
    cup_tags.append(tag4)

    def get_closest_cup_tag(ar_tag, cup_tags):
        def dist(x1,y1,z1,x2,y2,z2): return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        minDist=float('inf')
        minTag=None
        for T in cup_tags:
            d=dist(ar_tag.pos_x,ar_tag.pos_y,ar_tag.pos_z,T.pos_x,T.pos_y,T.pos_z)
            print d,T.tag_name
            if d<minDist:
                minDist=d
                minTag=T
        return minTag



    tag6=None
    # wait until we see tag6
    while tag6 is None or tag6.tag_name=='notfound':  
        print 'hasnt seen human yet'
        tag6=get_ar(6)

    print tag6

    os.system('cd ~/Desktop/baxter-waiter/src/cup_grabber/src')
    os.system('cd ~/Desktop/baxter-waiter/src/cup_grabber/src')
    os.system('rosrun cup_grabber joint_trajectory_file_playback.py -f get_cup')

    # starting position
    os.system('rosrun cup_grabber joint_trajectory_file_playback.py -f starting_position')

    left = baxter_interface.Limb('left')
    right = baxter_interface.Limb('right')
    grip_left = baxter_interface.Gripper('left', CHECK_VERSION)
    grip_right = baxter_interface.Gripper('right', CHECK_VERSION)
    lj = left.joint_names()
    rj = right.joint_names()


    def move(curr,trans):
        a=14*np.pi/180
        cx,cy,cz=curr
        tx,ty,tz=trans
        nz=tz*np.cos(a)-ty*np.sin(a)
        ny=tz*np.sin(a)+ty*np.cos(a)
        return (cx+tx,cy+ny,cz+nz)

    def explore(currxyz,currori):
        
        right_gripper.open()
        currxyz=move(currxyz,(-.1,.1+.03,-.1))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        currxyz=move(currxyz,(0,0,.17))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        right_gripper.close()
        currxyz=move(currxyz,(0,.5,0))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        currxyz=move(currxyz,(-.3,0,0))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        currxyz=move(currxyz,(.3,0,0))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        currxyz=move(currxyz,(0,-.5,0))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        right_gripper.open()
        currxyz=move(currxyz,(0,0,-.17))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        return (currxyz,currori)



    def pourMotion(currxyz,currori):
        right_gripper.open()
        currxyz=move(currxyz,(-.1,.1+.03,-.1))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        currxyz=move(currxyz,(0,0,.17))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        right_gripper.close()
        currxyz=move(currxyz,(0,.5,0))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        os.system('cd ~/Desktop/baxter-waiter/src/cup_grabber/src')
        os.system('rosrun cup_grabber joint_trajectory_file_playback.py -f right_pouring')
        currxyz=move(currxyz,(0,-.5,0))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        right_gripper.open()
        currxyz=move(currxyz,(0,0,-.17))
        requestIK('right_gripper','right_arm',currxyz,currori,compute_ik)
        return (currxyz,currori)



    #### end of custom functions



    
    # INITIAL TARGET POSITION at TAG3
    currxyz=(tag3.pos_x,tag3.pos_y,tag3.pos_z)
    currori=(-.083,-.02,-.697,.712)

    ## explore tag3
    currxyz,currori=explore(currxyz,currori)

    tag8=get_ar(8)
    tag9=get_ar(9)
    if tag8.tag_name!='notfound': tags[8]=tag8
    if tag9.tag_name!='notfound': tags[9]=tag9


    ## explore tag4
    currxyz=(tag4.pos_x,tag4.pos_y,tag4.pos_z)
    currxyz,currori=explore(currxyz,currori)

    tag8=get_ar(8)
    tag9=get_ar(9)
    if tag8.tag_name!='notfound': tags[8]=tag8
    if tag9.tag_name!='notfound': tags[9]=tag9



    ############################################# done sensing the environment



    os.system('cd ~/Desktop/baxter-waiter/src/cup_grabber/src')
    os.system('rosrun cup_grabber joint_trajectory_file_playback.py -f left_starting_position')


    ##tag8 is ice, tag9 is lemonade

    if 8==8:
        cup_tag_near_8=get_closest_cup_tag(tag8, cup_tags)
        curr=None
        if cup_tag_near_8.tag_name=='3':
            currxyz=(tag3.pos_x,tag3.pos_y,tag3.pos_z)
            curr=3
        elif cup_tag_near_8.tag_name=='4':
            currxyz=(tag4.pos_x,tag4.pos_y,tag4.pos_z)
            curr=4
        currxyz,currori=pourMotion(currxyz,currori)

    if 9==9:
        cup_tag_near_9=get_closest_cup_tag(tag9, cup_tags)
        if cup_tag_near_9.tag_name=='3':
            currxyz=(tag3.pos_x,tag3.pos_y,tag3.pos_z)
            curr=3
        elif cup_tag_near_9.tag_name=='4':
            currxyz=(tag4.pos_x,tag4.pos_y,tag4.pos_z)
            curr=4
        currxyz,currori=pourMotion(currxyz,currori)


    ## finale
    os.system('cd ~/Desktop/baxter-waiter/src/cup_grabber/src')
    os.system('rosrun cup_grabber joint_trajectory_file_playback.py -f serve')
    os.system('cd ~/Desktop/baxter-waiter/src/cup_grabber/src')
    os.system('rosrun cup_grabber joint_trajectory_file_playback.py -f dab')


#Python's syntax for a main() method
if __name__ == '__main__':
    main()





