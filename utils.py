import math


EPSILON = 0.00001

def equal(a: float, b: float) -> bool:
  if abs(a - b) < EPSILON:
    return True
  
  return False

def radians(degrees: float) -> float:
  return round((math.pi / 180) * degrees, 3)