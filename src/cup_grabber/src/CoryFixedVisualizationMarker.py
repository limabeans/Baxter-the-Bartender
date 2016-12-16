#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from visualization_msgs.msg import Marker
import Quaternion as Q
import numpy as np

class VisualSub:
    def __init__(self):
        rospy.init_node('fixed_visual_marker_node')
        rospy.Subscriber('/visualization_marker', Marker, self.vis_marker_received)
        self.pub = rospy.Publisher('/fixed_visualization_marker', Marker, queue_size=100)
        self.markerSeen=None
        self.angle=-14.0*np.pi/180
        self.cache={}
        self.seen=set()
        self.allowed=set([3,4,8,9])
    def vis_marker_received(self, markerInfo):
        markerId, position, orientation = markerInfo.id, markerInfo.pose.position, markerInfo.pose.orientation
        # if int(markerId) not in self.allowed: return
        # print markerInfo.id
        px,py,pz=tuple([position.x,position.y,position.z])
        # print distFromCamera
        position.z=np.cos(self.angle)*pz-np.sin(self.angle)*py
        position.y=np.sin(self.angle)*pz+np.cos(self.angle)*py
        q=(orientation.x,orientation.y,orientation.z,orientation.w)

        if q in self.cache:
          ori=self.cache[q]
          markerInfo.pose.orientation.x=ori[0]
          markerInfo.pose.orientation.y=ori[1]
          markerInfo.pose.orientation.z=ori[2]
          markerInfo.pose.orientation.w=ori[3]
        else:
          originalQuat = Q.Quat(Q.normalize(list(q)))
          quatOffsetFix = Q.Quat([0,0,-1*self.angle])
          fixed=originalQuat*quatOffsetFix
          x,y,z,w=tuple(fixed._get_q())
          markerInfo.pose.orientation.x=x
          markerInfo.pose.orientation.y=y
          markerInfo.pose.orientation.z=z
          markerInfo.pose.orientation.w=w
          self.cache[q]=[x,y,z,w]

        self.markerSeen=markerInfo

    def run(self):
      while not rospy.is_shutdown():
        if self.markerSeen is not None:
          self.pub.publish(self.markerSeen)
          print self.markerSeen.id

      
# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
    sub=VisualSub()
    sub.run()
