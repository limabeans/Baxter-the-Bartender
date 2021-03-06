# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cup_grabber/MultiARPoseRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MultiARPoseRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "cup_grabber/MultiARPoseRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MultiARPoseRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cup_grabber/MultiARPoseResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MultiARPoseResponse(genpy.Message):
  _md5sum = "4e57c6af3767990e7d901ffab9a7321a"
  _type = "cup_grabber/MultiARPoseResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string tag1
float64 pos_x1
float64 pos_y1
float64 pos_z1
float64 or_x1
float64 or_y1
float64 or_z1
float64 or_w1
string tag2
float64 pos_x2
float64 pos_y2
float64 pos_z2
float64 or_x2
float64 or_y2
float64 or_z2
float64 or_w2
string tag3
float64 pos_x3
float64 pos_y3
float64 pos_z3
float64 or_x3
float64 or_y3
float64 or_z3
float64 or_w3
string tag4
float64 pos_x4
float64 pos_y4
float64 pos_z4
float64 or_x4
float64 or_y4
float64 or_z4
float64 or_w4
"""
  __slots__ = ['tag1','pos_x1','pos_y1','pos_z1','or_x1','or_y1','or_z1','or_w1','tag2','pos_x2','pos_y2','pos_z2','or_x2','or_y2','or_z2','or_w2','tag3','pos_x3','pos_y3','pos_z3','or_x3','or_y3','or_z3','or_w3','tag4','pos_x4','pos_y4','pos_z4','or_x4','or_y4','or_z4','or_w4']
  _slot_types = ['string','float64','float64','float64','float64','float64','float64','float64','string','float64','float64','float64','float64','float64','float64','float64','string','float64','float64','float64','float64','float64','float64','float64','string','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tag1,pos_x1,pos_y1,pos_z1,or_x1,or_y1,or_z1,or_w1,tag2,pos_x2,pos_y2,pos_z2,or_x2,or_y2,or_z2,or_w2,tag3,pos_x3,pos_y3,pos_z3,or_x3,or_y3,or_z3,or_w3,tag4,pos_x4,pos_y4,pos_z4,or_x4,or_y4,or_z4,or_w4

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MultiARPoseResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.tag1 is None:
        self.tag1 = ''
      if self.pos_x1 is None:
        self.pos_x1 = 0.
      if self.pos_y1 is None:
        self.pos_y1 = 0.
      if self.pos_z1 is None:
        self.pos_z1 = 0.
      if self.or_x1 is None:
        self.or_x1 = 0.
      if self.or_y1 is None:
        self.or_y1 = 0.
      if self.or_z1 is None:
        self.or_z1 = 0.
      if self.or_w1 is None:
        self.or_w1 = 0.
      if self.tag2 is None:
        self.tag2 = ''
      if self.pos_x2 is None:
        self.pos_x2 = 0.
      if self.pos_y2 is None:
        self.pos_y2 = 0.
      if self.pos_z2 is None:
        self.pos_z2 = 0.
      if self.or_x2 is None:
        self.or_x2 = 0.
      if self.or_y2 is None:
        self.or_y2 = 0.
      if self.or_z2 is None:
        self.or_z2 = 0.
      if self.or_w2 is None:
        self.or_w2 = 0.
      if self.tag3 is None:
        self.tag3 = ''
      if self.pos_x3 is None:
        self.pos_x3 = 0.
      if self.pos_y3 is None:
        self.pos_y3 = 0.
      if self.pos_z3 is None:
        self.pos_z3 = 0.
      if self.or_x3 is None:
        self.or_x3 = 0.
      if self.or_y3 is None:
        self.or_y3 = 0.
      if self.or_z3 is None:
        self.or_z3 = 0.
      if self.or_w3 is None:
        self.or_w3 = 0.
      if self.tag4 is None:
        self.tag4 = ''
      if self.pos_x4 is None:
        self.pos_x4 = 0.
      if self.pos_y4 is None:
        self.pos_y4 = 0.
      if self.pos_z4 is None:
        self.pos_z4 = 0.
      if self.or_x4 is None:
        self.or_x4 = 0.
      if self.or_y4 is None:
        self.or_y4 = 0.
      if self.or_z4 is None:
        self.or_z4 = 0.
      if self.or_w4 is None:
        self.or_w4 = 0.
    else:
      self.tag1 = ''
      self.pos_x1 = 0.
      self.pos_y1 = 0.
      self.pos_z1 = 0.
      self.or_x1 = 0.
      self.or_y1 = 0.
      self.or_z1 = 0.
      self.or_w1 = 0.
      self.tag2 = ''
      self.pos_x2 = 0.
      self.pos_y2 = 0.
      self.pos_z2 = 0.
      self.or_x2 = 0.
      self.or_y2 = 0.
      self.or_z2 = 0.
      self.or_w2 = 0.
      self.tag3 = ''
      self.pos_x3 = 0.
      self.pos_y3 = 0.
      self.pos_z3 = 0.
      self.or_x3 = 0.
      self.or_y3 = 0.
      self.or_z3 = 0.
      self.or_w3 = 0.
      self.tag4 = ''
      self.pos_x4 = 0.
      self.pos_y4 = 0.
      self.pos_z4 = 0.
      self.or_x4 = 0.
      self.or_y4 = 0.
      self.or_z4 = 0.
      self.or_w4 = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.tag1
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x1, _x.pos_y1, _x.pos_z1, _x.or_x1, _x.or_y1, _x.or_z1, _x.or_w1))
      _x = self.tag2
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x2, _x.pos_y2, _x.pos_z2, _x.or_x2, _x.or_y2, _x.or_z2, _x.or_w2))
      _x = self.tag3
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x3, _x.pos_y3, _x.pos_z3, _x.or_x3, _x.or_y3, _x.or_z3, _x.or_w3))
      _x = self.tag4
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x4, _x.pos_y4, _x.pos_z4, _x.or_x4, _x.or_y4, _x.or_z4, _x.or_w4))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag1 = str[start:end].decode('utf-8')
      else:
        self.tag1 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x1, _x.pos_y1, _x.pos_z1, _x.or_x1, _x.or_y1, _x.or_z1, _x.or_w1,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag2 = str[start:end].decode('utf-8')
      else:
        self.tag2 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x2, _x.pos_y2, _x.pos_z2, _x.or_x2, _x.or_y2, _x.or_z2, _x.or_w2,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag3 = str[start:end].decode('utf-8')
      else:
        self.tag3 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x3, _x.pos_y3, _x.pos_z3, _x.or_x3, _x.or_y3, _x.or_z3, _x.or_w3,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag4 = str[start:end].decode('utf-8')
      else:
        self.tag4 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x4, _x.pos_y4, _x.pos_z4, _x.or_x4, _x.or_y4, _x.or_z4, _x.or_w4,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.tag1
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x1, _x.pos_y1, _x.pos_z1, _x.or_x1, _x.or_y1, _x.or_z1, _x.or_w1))
      _x = self.tag2
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x2, _x.pos_y2, _x.pos_z2, _x.or_x2, _x.or_y2, _x.or_z2, _x.or_w2))
      _x = self.tag3
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x3, _x.pos_y3, _x.pos_z3, _x.or_x3, _x.or_y3, _x.or_z3, _x.or_w3))
      _x = self.tag4
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.pos_x4, _x.pos_y4, _x.pos_z4, _x.or_x4, _x.or_y4, _x.or_z4, _x.or_w4))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag1 = str[start:end].decode('utf-8')
      else:
        self.tag1 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x1, _x.pos_y1, _x.pos_z1, _x.or_x1, _x.or_y1, _x.or_z1, _x.or_w1,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag2 = str[start:end].decode('utf-8')
      else:
        self.tag2 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x2, _x.pos_y2, _x.pos_z2, _x.or_x2, _x.or_y2, _x.or_z2, _x.or_w2,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag3 = str[start:end].decode('utf-8')
      else:
        self.tag3 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x3, _x.pos_y3, _x.pos_z3, _x.or_x3, _x.or_y3, _x.or_z3, _x.or_w3,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tag4 = str[start:end].decode('utf-8')
      else:
        self.tag4 = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pos_x4, _x.pos_y4, _x.pos_z4, _x.or_x4, _x.or_y4, _x.or_z4, _x.or_w4,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_7d = struct.Struct("<7d")
class MultiARPose(object):
  _type          = 'cup_grabber/MultiARPose'
  _md5sum = '4e57c6af3767990e7d901ffab9a7321a'
  _request_class  = MultiARPoseRequest
  _response_class = MultiARPoseResponse
