
EPSILON = 0.00001

def equal(a: float, b: float) -> bool:
  if abs(a - b) < EPSILON:
    return True
  
  return False