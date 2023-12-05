from tuple3d import Tuple3D
import math

class Vector3D(Tuple3D):
  def __init__(self, x: float, y: float, z: float) -> None:
    super().__init__(x, y, z, 0.0)

  @classmethod
  def magnitude(cls, v: "Vector3D") -> float:
    return math.sqrt(math.pow(v.x, 2) + math.pow(v.y, 2) + math.pow(v.z, 2) + math.pow(v.w, 2))
  
  @classmethod
  def normalize(cls, v: "Vector3D") -> Tuple3D:
    return Tuple3D(v.x / Vector3D.magnitude(v),
                    v.y / Vector3D.magnitude(v),
                    v.z / Vector3D.magnitude(v),
                    v.w / Vector3D.magnitude(v))
  
  @classmethod
  def dot(cls, a: "Vector3D", b: "Vector3D") -> float:
    return a.x * b.x + \
           a.y * b.y + \
           a.z * b.z + \
           a.w * b.w
  
  @classmethod
  def cross(cls, a: "Vector3D", b: "Vector3D") -> "Vector3D":
    return Vector3D(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)