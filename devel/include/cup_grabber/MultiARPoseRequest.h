// Generated by gencpp from file cup_grabber/MultiARPoseRequest.msg
// DO NOT EDIT!


#ifndef CUP_GRABBER_MESSAGE_MULTIARPOSEREQUEST_H
#define CUP_GRABBER_MESSAGE_MULTIARPOSEREQUEST_H


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
struct MultiARPoseRequest_
{
  typedef MultiARPoseRequest_<ContainerAllocator> Type;

  MultiARPoseRequest_()
    {
    }
  MultiARPoseRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }






  typedef boost::shared_ptr< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MultiARPoseRequest_

typedef ::cup_grabber::MultiARPoseRequest_<std::allocator<void> > MultiARPoseRequest;

typedef boost::shared_ptr< ::cup_grabber::MultiARPoseRequest > MultiARPoseRequestPtr;
typedef boost::shared_ptr< ::cup_grabber::MultiARPoseRequest const> MultiARPoseRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::cup_grabber::MultiARPoseRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cup_grabber/MultiARPoseRequest";
  }

  static const char* value(const ::cup_grabber::MultiARPoseRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::cup_grabber::MultiARPoseRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MultiARPoseRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cup_grabber::MultiARPoseRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::cup_grabber::MultiARPoseRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // CUP_GRABBER_MESSAGE_MULTIARPOSEREQUEST_H