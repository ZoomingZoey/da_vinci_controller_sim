from tuple2d import Tuple2D

class Point2D(Tuple2D):
  def __init__(self, x: float, y: float) -> None:
    super().__init__(x, y, 1.0)