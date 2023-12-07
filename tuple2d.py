import utils as ut
from tuple3d import Tuple3D

class Tuple2D:
  def __init__(self, x: float=0.0, y: float=0.0, w: float=0.0) -> None:
    self.x = x
    self.y = y
    self.w = w

  def isPoint(self) -> bool:
    return self.w == 1.0
  
  def isVector(self) -> bool:
    return self.w == 0.0
  
  def __eq__(self, other: "Tuple2D") -> bool:
    return ut.equal(self.x, other.x) and \
           ut.equal(self.y, other.y) and \
           ut.equal(self.w, other.w)
  
  def __add__(self, other: "Tuple2D") -> "Tuple2D":
    return Tuple2D(self.x + other.x, \
                   self.y + other.y, \
                   self.w + other.w)
  
  def __sub__(self, other: "Tuple2D") -> "Tuple2D":
    return Tuple2D(self.x - other.x, \
                   self.y - other.y, \
                   self.w - other.w)
  
  def __neg__(self) -> "Tuple2D":
    return Tuple2D(-self.x, \
                   -self.y, \
                   -self.w)
  
  def __mul__(self, other: "Tuple2D"):
    return Tuple2D(self.x * other, \
                   self.y * other, \
                   self.w * other)
  
  def __truediv__(self, other: "Tuple2D") -> "Tuple2D":
    return Tuple2D(self.x / other, \
                   self.y / other, \
                   self.w / other)
  
  def componentAt(self, index: int) -> float:
    match index:
      case 0:
        return self.x
      case 1:
        return self.y
      case 2:
        return self.w
      case _:
        return None
  
  def setComponentAt(self, index: int, value: float) -> None:
    match index:
      case 0:
        self.x = value
      case 1:
        self.y = value
      case 2:
        self.w = value
      case _:
        return
      
  def asArray(self) -> list:
    return [self.x, self.y, self.w]