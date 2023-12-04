import utils as ut

class Tuple2D:
  def __init__(self, x=0.0, y=0.0, w=0.0):
    self.x = x
    self.y = y
    self.w = w

  def isPoint(self):
    return self.w == 1.0
  
  def isVector(self):
    return self.w == 0.0
  
  def __eq__(self, other):
    return ut.equal(self.x, other.x) and \
           ut.equal(self.y, other.y) and \
           ut.equal(self.w, other.w)
  
  def __add__(self, other):
    return Tuple2D(self.x + other.x, \
                   self.y + other.y, \
                   self.w + other.w)
  
  def __sub__(self, other):
    return Tuple2D(self.x - other.x, \
                   self.y - other.y, \
                   self.w - other.w)
  
  def __neg__(self):
    return Tuple2D(-self.x, \
                   -self.y, \
                   -self.w)
  
  def __mul__(self, other):
    return Tuple2D(self.x * other, \
                   self.y * other, \
                   self.w * other)
  
  def __truediv__(self, other):
    return Tuple2D(self.x / other, \
                   self.y / other, \
                   self.w / other)
  
  def componentAt(self, index):
    match index:
      case 0:
        return self.x
      case 1:
        return self.y
      case 2:
        return self.w
      case _:
        return None
  
  def setComponentAt(self, index, value):
    match index:
      case 0:
        self.x = value
      case 1:
        self.y = value
      case 2:
        self.w = value
      case _:
        return
      
  def asArray(self):
    return [self.x, self.y, self.w]