#! /usr/bin/env python
from cup_grabber.srv import *
import rospy
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import Vector3, Quaternion, TransformStamped
from visualization_msgs.msg import Marker

class MultiARService:
    def __init__(self):
        rospy.init_node('fixed_multi_service_node')
        self.id_to_marker={}
        rospy.Subscriber('/fixed_visualization_marker', Marker, self.ar_data_received)
        rospy.Service('fixed_multi_service', ARPose, self.get_ar)
    
    def ar_data_received(self, message):
        self.id_to_marker[message.id]=message
        # print self.id_to_marker.keys()


    def get_ar(self,req):
        print req
        # assumes that arId is in self.id_to_marker
        arId=req.arId
        if arId in self.id_to_marker:
            marker=self.id_to_marker[arId]
            pos=marker.pose.position
            ori=marker.pose.orientation
            arPose = ARPoseResponse(str(arId),pos.x,pos.y,pos.z,ori.x,ori.y,ori.z,ori.w)
            return arPose
        else:
            return ARPoseResponse('notfound',0,0,0,0,0,0,0)
    def run(self):
        rospy.spin()                              

if __name__ == "__main__":
    node = MultiARService()
    print 'fixed_multi_service node initialized'
    node.run()
