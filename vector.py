import tuple as tp
import math

class Vector(tp.Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 0.0)

  @classmethod
  def magnitude(cls, v):
    return math.sqrt(math.pow(v.x, 2) + math.pow(v.y, 2) + math.pow(v.z, 2) + math.pow(v.w, 2))
  
  @classmethod
  def normalize(cls, v):
    return tp.Tuple(v.x / Vector.magnitude(v),
                    v.y / Vector.magnitude(v),
                    v.z / Vector.magnitude(v),
                    v.w / Vector.magnitude(v))
  
  @classmethod
  def dot(cls, a, b):
    return a.x * b.x + \
           a.y * b.y + \
           a.z * b.z + \
           a.w * b.w
  
  @classmethod
  def cross(cls, a, b):
    return Vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)