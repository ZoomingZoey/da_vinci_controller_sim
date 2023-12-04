from tuple3d import Tuple3D

class Point3D(Tuple3D):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 1.0)