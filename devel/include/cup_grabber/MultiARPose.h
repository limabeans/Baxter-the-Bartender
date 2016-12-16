// Generated by gencpp from file cup_grabber/MultiARPose.msg
// DO NOT EDIT!


#ifndef CUP_GRABBER_MESSAGE_MULTIARPOSE_H
#define CUP_GRABBER_MESSAGE_MULTIARPOSE_H

#include <ros/service_traits.h>


#include <cup_grabber/MultiARPoseRequest.h>
#include <cup_grabber/MultiARPoseResponse.h>


namespace cup_grabber
{

struct MultiARPose
{

typedef MultiARPoseRequest Request;
typedef MultiARPoseResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MultiARPose
} // namespace cup_grabber


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::cup_grabber::MultiARPose > {
  static const char* value()
  {
    return "4e57c6af3767990e7d901ffab9a7321a";
  }

  static const char* value(const ::cup_grabber::MultiARPose&) { return value(); }
};

template<>
struct DataType< ::cup_grabber::MultiARPose > {
  static const char* value()
  {
    return "cup_grabber/MultiARPose";
  }

  static const char* value(const ::cup_grabber::MultiARPose&) { return value(); }
};


// service_traits::MD5Sum< ::cup_grabber::MultiARPoseRequest> should match 
// service_traits::MD5Sum< ::cup_grabber::MultiARPose > 
template<>
struct MD5Sum< ::cup_grabber::MultiARPoseRequest>
{
  static const char* value()
  {
    return MD5Sum< ::cup_grabber::MultiARPose >::value();
  }
  static const char* value(const ::cup_grabber::MultiARPoseRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::cup_grabber::MultiARPoseRequest> should match 
// service_traits::DataType< ::cup_grabber::MultiARPose > 
template<>
struct DataType< ::cup_grabber::MultiARPoseRequest>
{
  static const char* value()
  {
    return DataType< ::cup_grabber::MultiARPose >::value();
  }
  static const char* value(const ::cup_grabber::MultiARPoseRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::cup_grabber::MultiARPoseResponse> should match 
// service_traits::MD5Sum< ::cup_grabber::MultiARPose > 
template<>
struct MD5Sum< ::cup_grabber::MultiARPoseResponse>
{
  static const char* value()
  {
    return MD5Sum< ::cup_grabber::MultiARPose >::value();
  }
  static const char* value(const ::cup_grabber::MultiARPoseResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::cup_grabber::MultiARPoseResponse> should match 
// service_traits::DataType< ::cup_grabber::MultiARPose > 
template<>
struct DataType< ::cup_grabber::MultiARPoseResponse>
{
  static const char* value()
  {
    return DataType< ::cup_grabber::MultiARPose >::value();
  }
  static const char* value(const ::cup_grabber::MultiARPoseResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CUP_GRABBER_MESSAGE_MULTIARPOSE_H
