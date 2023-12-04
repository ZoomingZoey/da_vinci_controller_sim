from tuple2d import Tuple2D
import math

class Vector2D(Tuple2D):
  def __init__(self, x, y):
    super().__init__(x, y, 0.0)

  @classmethod
  def magnitude(cls, v):
    return math.sqrt(math.pow(v.x, 2) + math.pow(v.y, 2) + math.pow(v.w, 2))
  
  @classmethod
  def normalize(cls, v):
    return Tuple2D(v.x / Vector2D.magnitude(v),
                    v.y / Vector2D.magnitude(v),
                    v.w / Vector2D.magnitude(v))
  
  # @classmethod
  # def dot(cls, a, b):
  #   return a.x * b.x + \
  #          a.y * b.y + \
  #          a.z * b.z + \
  #          a.w * b.w
  
  # @classmethod
  # def cross(cls, a, b):
  #   return Vector2D(a.y * b.z - a.z * b.y,
  #                 a.z * b.x - a.x * b.z,
  #                 a.x * b.y - a.y * b.x)