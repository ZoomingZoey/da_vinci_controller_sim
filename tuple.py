import utils as ut

class Tuple:
  def __init__(self, x, y, z, w):
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  def isPoint(self):
    return self.w == 1.0
  
  def isVector(self):
    return self.w == 0.0
  
  def __eq__(self, other):
    return ut.equal(self.x, other.x) and \
           ut.equal(self.y, other.y) and \
           ut.equal(self.z, other.z) and \
           ut.equal(self.w, other.w)
  
  def __add__(self, other):
    return Tuple(self.x + other.x, \
                 self.y + other.y, \
                 self.z + other.z, \
                 self.w + other.w)
  
  def __sub__(self, other):
    return Tuple(self.x - other.x, \
                 self.y - other.y, \
                 self.z - other.z, \
                 self.w - other.w)
  
  def __neg__(self):
    return Tuple(-self.x, \
                 -self.y, \
                 -self.z, \
                 -self.w)
  
  def __mul__(self, other):
    return Tuple(self.x * other, \
                 self.y * other, \
                 self.z * other, \
                 self.w * other)
  
  def __truediv__(self, other):
    return Tuple(self.x / other, \
                 self.y / other, \
                 self.z / other, \
                 self.w / other)