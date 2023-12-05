import utils as ut
class Matrix2:
  def __init__(self, a11: float=1, a12: float=0,
                     a21: float=0, a22: float=1) -> None:
    
    self.mat = [
      [a11, a12],
      [a21, a22]
    ]

  def at(self, row: int, col: int) -> float:
    if (row < 0 or row >= 2) and (col < 0 or col >= 2):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[row][col]
  
  def determinant(self) -> float:
    return (self.mat[0][0] * self.mat[1][1]) - (self.mat[0][1] * self.mat[1][0])
  
  def __eq__(self, other: "Matrix2") -> bool:
    return(
      ut.equal(self.mat[0][0], other.mat[0][0]) and
      ut.equal(self.mat[0][1], other.mat[0][1]) and
      ut.equal(self.mat[1][0], other.mat[1][0]) and
      ut.equal(self.mat[1][1], other.mat[1][1])
    )