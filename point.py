import tuple as tp
from vector import Vector

class Point(tp.Tuple):
  def __init__(self, x, y, z):
    super().__init__(x, y, z, 1.0)