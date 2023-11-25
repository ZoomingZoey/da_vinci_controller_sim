class Matrix2:
  def __init__(self, a11=0, a12=0,
               a21=0, a22=0):
    
    self.mat = [
      [a11, a12],
      [a21, a22]
    ]

  def at(self, r, c):
    if (r < 0 or r >= 2) and (c < 0 or c >= 2):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[r][c]