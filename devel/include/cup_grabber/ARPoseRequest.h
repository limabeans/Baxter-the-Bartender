// Generated by gencpp from file cup_grabber/ARPoseRequest.msg
// DO NOT EDIT!


#ifndef CUP_GRABBER_MESSAGE_ARPOSEREQUEST_H
#define CUP_GRABBER_MESSAGE_ARPOSEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cup_grabber
{
template <class ContainerAllocator>
struct ARPoseRequest_
{
  typedef ARPoseRequest_<ContainerAllocator> Type;

  ARPoseRequest_()
    : arId(0)  {
    }
  ARPoseRequest_(const ContainerAllocator& _alloc)
    : arId(0)  {
  (void)_alloc;
    }



   typedef int64_t _arId_type;
  _arId_type arId;




  typedef boost::shared_ptr< ::cup_grabber::ARPoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cup_grabber::ARPoseRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ARPoseRequest_

typedef ::cup_grabber::ARPoseRequest_<std::allocator<void> > ARPoseRequest;

typedef boost::shared_ptr< ::cup_grabber::ARPoseRequest > ARPoseRequestPtr;
typedef boost::shared_ptr< ::cup_grabber::ARPoseRequest const> ARPoseRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cup_grabber::ARPoseRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cup_grabber

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cup_grabber::ARPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cup_grabber::ARPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cup_grabber::ARPoseRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f9fa3a18063829850381aa28ccfd270a";
  }

  static const char* value(const ::cup_grabber::ARPoseRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf9fa3a1806382985ULL;
  static const uint64_t static_value2 = 0x0381aa28ccfd270aULL;
};

template<class ContainerAllocator>
struct DataType< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cup_grabber/ARPoseRequest";
  }

  static const char* value(const ::cup_grabber::ARPoseRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 arId\n\
";
  }

  static const char* value(const ::cup_grabber::ARPoseRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.arId);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ARPoseRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cup_grabber::ARPoseRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cup_grabber::ARPoseRequest_<ContainerAllocator>& v)
  {
    s << indent << "arId: ";
    Printer<int64_t>::stream(s, indent + "  ", v.arId);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CUP_GRABBER_MESSAGE_ARPOSEREQUEST_H