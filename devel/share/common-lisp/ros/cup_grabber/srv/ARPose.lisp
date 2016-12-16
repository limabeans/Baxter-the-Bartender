; Auto-generated. Do not edit!


(cl:in-package cup_grabber-srv)


;//! \htmlinclude ARPose-request.msg.html

(cl:defclass <ARPose-request> (roslisp-msg-protocol:ros-message)
  ((arId
    :reader arId
    :initarg :arId
    :type cl:integer
    :initform 0))
)

(cl:defclass ARPose-request (<ARPose-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ARPose-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ARPose-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cup_grabber-srv:<ARPose-request> is deprecated: use cup_grabber-srv:ARPose-request instead.")))

(cl:ensure-generic-function 'arId-val :lambda-list '(m))
(cl:defmethod arId-val ((m <ARPose-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:arId-val is deprecated.  Use cup_grabber-srv:arId instead.")
  (arId m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ARPose-request>) ostream)
  "Serializes a message object of type '<ARPose-request>"
  (cl:let* ((signed (cl:slot-value msg 'arId)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ARPose-request>) istream)
  "Deserializes a message object of type '<ARPose-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'arId) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ARPose-request>)))
  "Returns string type for a service object of type '<ARPose-request>"
  "cup_grabber/ARPoseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ARPose-request)))
  "Returns string type for a service object of type 'ARPose-request"
  "cup_grabber/ARPoseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ARPose-request>)))
  "Returns md5sum for a message object of type '<ARPose-request>"
  "912562d6fca199e1e3b0bb6f5dd85bf1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ARPose-request)))
  "Returns md5sum for a message object of type 'ARPose-request"
  "912562d6fca199e1e3b0bb6f5dd85bf1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ARPose-request>)))
  "Returns full string definition for message of type '<ARPose-request>"
  (cl:format cl:nil "int64 arId~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ARPose-request)))
  "Returns full string definition for message of type 'ARPose-request"
  (cl:format cl:nil "int64 arId~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ARPose-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ARPose-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ARPose-request
    (cl:cons ':arId (arId msg))
))
;//! \htmlinclude ARPose-response.msg.html

(cl:defclass <ARPose-response> (roslisp-msg-protocol:ros-message)
  ((tag_name
    :reader tag_name
    :initarg :tag_name
    :type cl:string
    :initform "")
   (pos_x
    :reader pos_x
    :initarg :pos_x
    :type cl:float
    :initform 0.0)
   (pos_y
    :reader pos_y
    :initarg :pos_y
    :type cl:float
    :initform 0.0)
   (pos_z
    :reader pos_z
    :initarg :pos_z
    :type cl:float
    :initform 0.0)
   (or_x
    :reader or_x
    :initarg :or_x
    :type cl:float
    :initform 0.0)
   (or_y
    :reader or_y
    :initarg :or_y
    :type cl:float
    :initform 0.0)
   (or_z
    :reader or_z
    :initarg :or_z
    :type cl:float
    :initform 0.0)
   (or_w
    :reader or_w
    :initarg :or_w
    :type cl:float
    :initform 0.0))
)

(cl:defclass ARPose-response (<ARPose-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ARPose-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ARPose-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cup_grabber-srv:<ARPose-response> is deprecated: use cup_grabber-srv:ARPose-response instead.")))

(cl:ensure-generic-function 'tag_name-val :lambda-list '(m))
(cl:defmethod tag_name-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:tag_name-val is deprecated.  Use cup_grabber-srv:tag_name instead.")
  (tag_name m))

(cl:ensure-generic-function 'pos_x-val :lambda-list '(m))
(cl:defmethod pos_x-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:pos_x-val is deprecated.  Use cup_grabber-srv:pos_x instead.")
  (pos_x m))

(cl:ensure-generic-function 'pos_y-val :lambda-list '(m))
(cl:defmethod pos_y-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:pos_y-val is deprecated.  Use cup_grabber-srv:pos_y instead.")
  (pos_y m))

(cl:ensure-generic-function 'pos_z-val :lambda-list '(m))
(cl:defmethod pos_z-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:pos_z-val is deprecated.  Use cup_grabber-srv:pos_z instead.")
  (pos_z m))

(cl:ensure-generic-function 'or_x-val :lambda-list '(m))
(cl:defmethod or_x-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:or_x-val is deprecated.  Use cup_grabber-srv:or_x instead.")
  (or_x m))

(cl:ensure-generic-function 'or_y-val :lambda-list '(m))
(cl:defmethod or_y-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:or_y-val is deprecated.  Use cup_grabber-srv:or_y instead.")
  (or_y m))

(cl:ensure-generic-function 'or_z-val :lambda-list '(m))
(cl:defmethod or_z-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:or_z-val is deprecated.  Use cup_grabber-srv:or_z instead.")
  (or_z m))

(cl:ensure-generic-function 'or_w-val :lambda-list '(m))
(cl:defmethod or_w-val ((m <ARPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cup_grabber-srv:or_w-val is deprecated.  Use cup_grabber-srv:or_w instead.")
  (or_w m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ARPose-response>) ostream)
  "Serializes a message object of type '<ARPose-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'tag_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'tag_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pos_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pos_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'pos_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'or_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'or_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'or_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'or_w))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ARPose-response>) istream)
  "Deserializes a message object of type '<ARPose-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tag_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'tag_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pos_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'or_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'or_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'or_z) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'or_w) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ARPose-response>)))
  "Returns string type for a service object of type '<ARPose-response>"
  "cup_grabber/ARPoseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ARPose-response)))
  "Returns string type for a service object of type 'ARPose-response"
  "cup_grabber/ARPoseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ARPose-response>)))
  "Returns md5sum for a message object of type '<ARPose-response>"
  "912562d6fca199e1e3b0bb6f5dd85bf1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ARPose-response)))
  "Returns md5sum for a message object of type 'ARPose-response"
  "912562d6fca199e1e3b0bb6f5dd85bf1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ARPose-response>)))
  "Returns full string definition for message of type '<ARPose-response>"
  (cl:format cl:nil "string tag_name~%float64 pos_x~%float64 pos_y~%float64 pos_z~%float64 or_x~%float64 or_y~%float64 or_z~%float64 or_w~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ARPose-response)))
  "Returns full string definition for message of type 'ARPose-response"
  (cl:format cl:nil "string tag_name~%float64 pos_x~%float64 pos_y~%float64 pos_z~%float64 or_x~%float64 or_y~%float64 or_z~%float64 or_w~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ARPose-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'tag_name))
     8
     8
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ARPose-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ARPose-response
    (cl:cons ':tag_name (tag_name msg))
    (cl:cons ':pos_x (pos_x msg))
    (cl:cons ':pos_y (pos_y msg))
    (cl:cons ':pos_z (pos_z msg))
    (cl:cons ':or_x (or_x msg))
    (cl:cons ':or_y (or_y msg))
    (cl:cons ':or_z (or_z msg))
    (cl:cons ':or_w (or_w msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ARPose)))
  'ARPose-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ARPose)))
  'ARPose-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ARPose)))
  "Returns string type for a service object of type '<ARPose>"
  "cup_grabber/ARPose")