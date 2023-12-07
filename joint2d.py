from point2d import Point2D
from matrix3 import Matrix3

class Joint2D():
  def __init__(self, origin: Point2D=Point2D(0, 0, 0), pitch: float=0, child: "Joint2D"=None, type: str="fixed", isBase: bool=True) -> None:
    self.transform = Matrix3().identity().translation(origin.x, origin.y).rotationZ(pitch)
    self.child = child
    self.type = type
    self.isBase = isBase

  