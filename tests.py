import unittest
import math

import utils as ut
from tuple2d import Tuple2D
from tuple3d import Tuple3D
from point2d import Point2D
from vector2d import Vector2D
from point3d import Point3D
from vector3d import Vector3D
from matrix2 import Matrix2
from matrix3 import Matrix3
from matrix4 import Matrix4

class TestTuple(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls): ### run once before all test cases ###
    pass
  
  @classmethod
  def tearDownClass(cls): ### run once after all test cases ###
    pass
  
  def setUp(self): ### run before each test case ###
    pass
  
  def tearDown(self): ### run after each test case ###
    pass
  
  ### make sure to add => test_ <= as prefix to all test cases otherwise they won't work ###
  def test_3d_tuple_is_point(self):
    '''Test case function for checking if a 3D tuple with w=1.0 is a point'''
    self.a = Tuple3D(4.3, -4.2, 3.1, 1.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.z, 3.1)
    self.assertEqual(self.a.w, 1.0)
    self.assertEqual(self.a.isPoint(), True)
    self.assertEqual(self.a.isVector(), False)

  def test_2d_tuple_is_point(self):
    '''Test case function for checking if a 2D tuple with w=1.0 is a point'''
    self.a = Tuple2D(4.3, -4.2, 1.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.w, 1.0)
    self.assertEqual(self.a.isPoint(), True)
    self.assertEqual(self.a.isVector(), False)

  def test_3d_tuple_is_vector(self):
    '''Test case function for checking if a 3D tuple with w=0.0 is a vector'''
    self.a = Tuple3D(4.3, -4.2, 3.1, 0.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.z, 3.1)
    self.assertEqual(self.a.w, 0.0)
    self.assertEqual(self.a.isPoint(), False)
    self.assertEqual(self.a.isVector(), True)

  def test_2d_tuple_is_vector(self):
    '''Test case function for checking if a 2D tuple with w=0.0 is a vector'''
    self.a = Tuple2D(4.3, -4.2, 0.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.w, 0.0)
    self.assertEqual(self.a.isPoint(), False)
    self.assertEqual(self.a.isVector(), True)

  def test_adding_two_3d_tuples(self):
    '''Test case function for adding two 3D tuples'''
    self.a1 = Tuple3D(3, -2, 5, 1)
    self.a2 = Tuple3D(-2, 3, 1, 0)
    result = self.a1 + self.a2
    self.assertTrue(result == Tuple3D(1, 1, 6, 1))

  def test_adding_two_2d_tuples(self):
    '''Test case function for adding two 2D tuples'''
    self.a1 = Tuple2D(3, -2, 1)
    self.a2 = Tuple2D(-2, 3, 0)
    result = self.a1 + self.a2
    self.assertTrue(result == Tuple2D(1, 1, 1))

  def test_negating_a_3d_tuple(self):
    '''Test case function for negating a 3D tuple'''
    self.a = Tuple3D(1, -2, 3, -4)
    self.assertTrue(-self.a == Tuple3D(-1, 2, -3, 4))

  def test_negating_a_2d_tuple(self):
    '''Test case function for negating a 2D tuple'''
    self.a = Tuple2D(1, -2, -4)
    self.assertTrue(-self.a == Tuple2D(-1, 2, 4))

  def test_multiplying_a_3d_tuple_by_a_scalar(self):
    '''Test case function for multiplying a 3D tuple by a scalar'''
    self.a = Tuple3D(1, -2, 3, -4)
    result = self.a * 3.5
    self.assertTrue(result == Tuple3D(3.5, -7, 10.5, -14))

  def test_multiplying_a_2d_tuple_by_a_scalar(self):
    '''Test case function for multiplying a 2D tuple by a scalar'''
    self.a = Tuple2D(1, -2, -4)
    result = self.a * 3.5
    self.assertTrue(result == Tuple2D(3.5, -7, -14))

  def test_multiplying_a_3d_tuple_by_a_fraction(self):
    '''Test case function for multiplying a 3D tuple by a fraction'''
    self.a = Tuple3D(1, -2, 3, -4)
    result = self.a * 0.5
    self.assertTrue(result == Tuple3D(0.5, -1, 1.5, -2))

  def test_multiplying_a_2d_tuple_by_a_fraction(self):
    '''Test case function for multiplying a 2D tuple by a fraction'''
    self.a = Tuple2D(1, -2, -4)
    result = self.a * 0.5
    self.assertTrue(result == Tuple2D(0.5, -1, -2))

  def test_dividing_a_3d_tuple_by_a_scalar(self):
    '''Test case function for dividing a 3D tuple by a scalar'''
    self.a = Tuple3D(1, -2, 3, -4)
    result = self.a / 2
    self.assertTrue(result == Tuple3D(0.5, -1, 1.5, -2))

  def test_dividing_a_2d_tuple_by_a_scalar(self):
    '''Test case function for dividing a 2D tuple by a scalar'''
    self.a = Tuple2D(1, -2, -4)
    result = self.a / 2
    self.assertTrue(result == Tuple2D(0.5, -1, -2))

  def test_dot_product_of_two_3d_tuples(self):
    '''Test case function for the dot product of two 3D tuples'''
    self.a = Vector3D(1, 2, 3)
    self.b = Vector3D(2, 3, 4)
    result = Vector3D.dot(self.a, self.b)
    self.assertTrue(result == 20)

class TestPoint(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    pass
  
  @classmethod
  def tearDownClass(cls):
    pass
  
  def setUp(self):
    pass
  
  def tearDown(self):
    pass

  def test_3d_point_creates_correct_3d_tuple(self):
    '''Test case function for checking that Point3D() creates 3D tuples with w=1.0'''
    self.p = Point3D(4, -4, 3)
    self.assertTrue(self.p == Tuple3D(4, -4, 3, 1))

  def test_2d_point_creates_correct_2d_tuple(self):
    '''Test case function for checking that Point2D() creates 2D tuples with w=1.0'''
    self.p = Point2D(4, -4)
    self.assertTrue(self.p == Tuple2D(4, -4, 1))

  def test_subtracting_two_3d_points(self):
    '''Test case function for subtracting two 3D points'''
    self.p1 = Point3D(3, 2, 1)
    self.p2 = Point3D(5, 6, 7)
    result = self.p1 - self.p2
    self.assertTrue(result == Vector3D(-2, -4, -6))

  def test_subtracting_two_2d_points(self):
    '''Test case function for subtracting two 2D points'''
    self.p1 = Point2D(3, 2)
    self.p2 = Point2D(5, 6)
    result = self.p1 - self.p2
    self.assertTrue(result == Vector2D(-2, -4))

  def test_subtracting_a_3d_vector_from_a_3d_point(self):
    '''Test case function for subtracting a 3D vector from a 3D point'''
    self.p = Point3D(3, 2, 1)
    self.v = Vector3D(5, 6, 7)
    result = self.p - self.v
    self.assertTrue(result == Point3D(-2, -4, -6))

  def test_subtracting_a_2d_vector_from_a_2d_point(self):
    '''Test case function for subtracting a 2D vector from a 2D point'''
    self.p = Point2D(3, 2)
    self.v = Vector2D(5, 6)
    result = self.p - self.v
    self.assertTrue(result == Point2D(-2, -4))

class TestVector(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    pass
  
  @classmethod
  def tearDownClass(cls):
    pass
  
  def setUp(self):
    pass
  
  def tearDown(self):
    pass

  def test_3d_vector_creates_correct_3d_tuple(self):
    '''Test case function for checking that Vector3D() creates 3D tuples with w=0.0'''
    self.v = Vector3D(4, -4, 3)
    self.assertTrue(self.v == Tuple3D(4, -4, 3, 0))

  def test_2d_vector_creates_correct_2d_tuple(self):
    '''Test case function for checking that Vector2D() creates 2D tuples with w=0.0'''
    self.v = Vector2D(4, -4)
    self.assertTrue(self.v == Tuple2D(4, -4, 0))

  def test_subtracting_two_3d_vectors(self):
    '''Test case function for subtracting two 3D vectors'''
    self.v1 = Vector3D(3, 2, 1)
    self.v2 = Vector3D(5, 6, 7)
    result = self.v1 - self.v2
    self.assertTrue(result == Vector3D(-2, -4, -6))

  def test_subtracting_two_2d_vectors(self):
    '''Test case function for subtracting two 2D vectors'''
    self.v1 = Vector2D(3, 2)
    self.v2 = Vector2D(5, 6)
    result = self.v1 - self.v2
    self.assertTrue(result == Vector2D(-2, -4))

  def test_subtract_3d_vector_from_3d_zero_vector(self):
    '''Test case function for subtracting a 3D vector from the 3D zero vector'''
    self.zero = Vector3D(0, 0, 0)
    self.v = Vector3D(1, -2, 3)
    result = self.zero - self.v
    self.assertTrue(result == Vector3D(-1, 2, -3))

  def test_subtract_2d_vector_from_2d_zero_vector(self):
    '''Test case function for subtracting a 2D vector from the 2D zero vector'''
    self.zero = Vector2D(0, 0)
    self.v = Vector2D(1, -2)
    result = self.zero - self.v
    self.assertTrue(result == Vector2D(-1, 2))

  def test_compute_3d_vector_magnitude_1(self):
    '''Test case function for computing the magnitude of Vector3D(1, 0, 0)'''
    self.v = Vector3D(1, 0, 0)
    self.assertTrue(ut.equal(Vector3D.magnitude(self.v), 1))

  def test_compute_2d_vector_magnitude_1(self):
    '''Test case function for computing the magnitude of Vector2D(1, 0)'''
    self.v = Vector2D(1, 0)
    self.assertTrue(ut.equal(Vector2D.magnitude(self.v), 1))

  def test_compute_3d_vector_magnitude_2(self):
    '''Test case function for computing the magnitude of Vector3D(0, 1, 0)'''
    self.v = Vector3D(0, 1, 0)
    self.assertTrue(ut.equal(Vector3D.magnitude(self.v), 1))

  def test_compute_2d_vector_magnitude_2(self):
    '''Test case function for computing the magnitude of Vector2D(0, 1)'''
    self.v = Vector2D(0, 1)
    self.assertTrue(ut.equal(Vector2D.magnitude(self.v), 1))

  def test_compute_3d_vector_magnitude_3(self):
    '''Test case function for computing the magnitude of Vector3D(0, 0, 1)'''
    self.v = Vector3D(0, 0, 1)
    self.assertTrue(ut.equal(Vector3D.magnitude(self.v), 1))

  def test_compute_3d_vector_magnitude_4(self):
    '''Test case function for computing the magnitude of Vector3D(1, 2, 3)'''
    self.v = Vector3D(1, 2, 3)
    self.assertTrue(ut.equal(Vector3D.magnitude(self.v), math.sqrt(14)))

  def test_compute_2d_vector_magnitude_3(self):
    '''Test case function for computing the magnitude of Vector2D(1, 2)'''
    self.v = Vector2D(1, 2)
    self.assertTrue(ut.equal(Vector2D.magnitude(self.v), math.sqrt(5)))

  def test_compute_3d_vector_magnitude_5(self):
    '''Test case function for computing the magnitude of Vector3D(-1, -2, -3)'''
    self.v = Vector3D(-1, -2, -3)
    self.assertTrue(ut.equal(Vector3D.magnitude(self.v), math.sqrt(14)))

  def test_compute_2d_vector_magnitude_4(self):
    '''Test case function for computing the magnitude of Vector2D(-1, -2)'''
    self.v = Vector2D(-1, -2)
    self.assertTrue(ut.equal(Vector2D.magnitude(self.v), math.sqrt(5)))

  def test_normalize_3d_vector_1(self):
    '''Test case function for normalizing Vector3D(4, 0, 0) gives (1, 0, 0)'''
    self.v = Vector3D(4, 0, 0)
    self.assertTrue(Vector3D.normalize(self.v) == Vector3D(1, 0, 0))

  def test_normalize_2d_vector_1(self):
    '''Test case function for normalizing Vector2D(4, 0) gives (1, 0)'''
    self.v = Vector2D(4, 0)
    self.assertTrue(Vector2D.normalize(self.v) == Vector2D(1, 0))

  def test_normalize_3d_vector_2(self):
    '''Test case function for normalizing Vector3D(1, 2, 3)'''
    self.v = Vector3D(1, 2, 3)
    self.assertTrue(Vector3D.normalize(self.v) == Vector3D(0.26726, 0.53452, 0.80178))

  def test_normalize_2d_vector_2(self):
    '''Test case function for normalizing Vector2D(1, 2)'''
    self.v = Vector2D(1, 2)
    self.assertTrue(Vector2D.normalize(self.v) == Vector2D(0.44721, 0.89442))

  def test_magnitude_of_normalized_3d_vector(self):
    '''Test case function for the magnitude of a normalized 3D vector'''
    self.v = Vector3D(1, 2, 3)
    norm = Vector3D.normalize(self.v)
    self.assertEqual(Vector3D.magnitude(norm), 1)

  def test_magnitude_of_normalized_2d_vector(self):
    '''Test case function for the magnitude of a normalized 2D vector'''
    self.v = Vector2D(1, 2)
    norm = Vector2D.normalize(self.v)
    self.assertTrue(ut.equal(Vector2D.magnitude(norm), 1))

  def test_cross_product_of_two_3d_vectors(self):
    '''Test case function for the cross product of two 3D vectors'''
    self.a = Vector3D(1, 2, 3)
    self.b = Vector3D(2, 3, 4)
    self.assertTrue(Vector3D.cross(self.a, self.b) == Vector3D(-1, 2, -1))
    self.assertTrue(Vector3D.cross(self.b, self.a) == Vector3D(1, -2, 1))

  class TestMatrix(unittest.TestCase):
  
    @classmethod
    def setUpClass(cls):
      pass
    
    @classmethod
    def tearDownClass(cls):
      pass
    
    def setUp(self):
      pass
    
    def tearDown(self):
      pass

  def test_construct_and_inspect_a_4x4_matrix(self):
    '''Test case function for the constructing and inspecting a 4x4 matrix'''
    self.M = Matrix4(1, 2, 3, 4,
                5.5, 6.5, 7.5, 8.5,
                9, 10, 11, 12,
                13.5, 14.5, 15.5, 16.5)
    
    self.assertEqual(self.M.at(0, 0), 1)
    self.assertEqual(self.M.at(0, 3), 4)
    self.assertEqual(self.M.at(1, 0), 5.5)
    self.assertEqual(self.M.at(1, 2), 7.5)
    self.assertEqual(self.M.at(2, 2), 11)
    self.assertEqual(self.M.at(3, 0), 13.5)
    self.assertEqual(self.M.at(3, 2), 15.5)

  def test_representing_a_2x2_matrix(self):
    '''Test case function for representing a 2x2 matrix'''
    self.M = Matrix2(-3, 5,
                     1, -2)
    
    self.assertEqual(self.M.at(0, 0), -3)
    self.assertEqual(self.M.at(0, 1), 5)
    self.assertEqual(self.M.at(1, 0), 1)
    self.assertEqual(self.M.at(1, 1), -2)

  def test_representing_a_3x3_matrix(self):
    '''Test case function for representing a 3x3 matrix'''
    self.M = Matrix3(-3, 5, 0,
                     1, -2, -7,
                     0, 1, 1)
    
    self.assertEqual(self.M.at(0, 0), -3)
    self.assertEqual(self.M.at(1, 1), -2)
    self.assertEqual(self.M.at(2, 2), 1)

  def test_identical_4x4_matrix_equality(self):
    '''Test case function for matrix equality with identical 4x4 matrices'''
    self.A = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.B = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.assertTrue(self.A == self.B)

  def test_identical_3x3_matrix_equality(self):
    '''Test case function for matrix equality with identical 3x3 matrices'''
    self.A = Matrix3(1, 2, 3,
                     4, 5, 6,
                     7, 8, 9)
    
    self.B = Matrix3(1, 2, 3,
                     4, 5, 6,
                     7, 8, 9)
    
    self.assertTrue(self.A == self.B)

  def test_different_4x4_matrix_equality(self):
    '''Test case function for matrix equality with different 4x4 matrices'''
    self.A = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.B = Matrix4(2, 3, 4, 5,
                     6, 7, 8, 9,
                     8, 7, 6, 5,
                     4, 3, 2, 1)
    
    self.assertTrue(self.A != self.B)

  def test_different_3x3_matrix_equality(self):
    '''Test case function for matrix equality with different 3x3 matrices'''
    self.A = Matrix3(1, 2, 3,
                     4, 5, 6,
                     7, 8, 9)
    
    self.B = Matrix3(2, 3, 4,
                     5, 6, 7,
                     8, 9, 8)
    
    self.assertTrue(self.A != self.B)

  def test_multiply_two_4x4_matrices(self):
    '''Test case function for multiplying two 4x4 matrices'''
    self.A = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.B = Matrix4(-2, 1, 2, 3,
                     3, 2, 1, -1,
                     4, 3, 6, 5,
                     1, 2, 7, 8)
    
  def test_multiply_two_3x3_matrices(self):
    '''Test case function for multiplying two 3x3 matrices'''
    self.A = Matrix3(1, 2, 3,
                     4, 5, 6,
                     7, 8, 9)
    
    self.B = Matrix3(-2, 1, 2,
                     3, 4, -5,
                     4, 3, 2)
    
    result = self.A.matrixMultiply(self.B)
    expected = Matrix3(16, 18, -2,
                       31, 42, -5,
                       46, 66, -8)
    
    self.assertTrue(result == expected)

  def test_multiply_4x4_matrix_by_3d_tuple(self):
    '''Test case function for multiplying a 4x4 matrix by a 3D tuple'''
    self.A = Matrix4(1, 2, 3, 4,
                     2, 4, 4, 2,
                     8, 6, 4, 1,
                     0, 0, 0, 1)
    
    self.b = Tuple3D(1, 2, 3, 1)
    
    result = self.A.tupleMultiply(self.b)
    expected = Tuple3D(18, 24, 33, 1)
    
    self.assertTrue(result == expected)

  def test_multiply_3x3_matrix_by_2d_tuple(self):
    '''Test case function for multiplying a 3x3 matrix by a 2D tuple'''
    self.A = Matrix3(1, 2, 3,
                     2, 4, 4,
                     0, 0, 1)
    
    self.b = Tuple2D(1, 2, 1)
    
    result = self.A.tupleMultiply(self.b)
    expected = Tuple2D(8, 14, 1)
    
    self.assertTrue(result == expected)

  def test_multiply_4x4_matrix_by_4x4_identity_matrix(self):
    '''Test case function for multiplying a 4x4 matrix by the 4x4 identity matrix'''
    self.A = Matrix4(0, 1, 2, 4,
                     1, 2, 4, 8,
                     2, 4, 8, 16,
                     4, 8, 16, 32)
    
    result = self.A.matrixMultiply(Matrix4().identity())
    self.assertTrue(result == self.A)

  def test_multiply_3x3_matrix_by_3x3_identity_matrix(self):
    '''Test case function for multiplying a 3x3 matrix by the 3x3 identity matrix'''
    self.A = Matrix3(0, 1, 2,
                     1, 2, 14,
                     2, 14, 18)
    
    result = self.A.matrixMultiply(Matrix3().identity())
    self.assertTrue(result == self.A)

  def test_multiply_4x4_identity_matrix_by_3d_tuple(self):
    '''Test case function for multiplying the 4x4 identity matrix by a 3D tuple'''
    self.a = Tuple3D(1, 2, 3, 4)
    
    result = Matrix4().identity().tupleMultiply(self.a)
    self.assertTrue(result == self.a)

  def test_multiply_3x3_identity_matrix_by_2d_tuple(self):
    '''Test case function for multiplying the 3x3 identity matrix by a 2D tuple'''
    self.a = Tuple2D(1, 2, 3)
    
    result = Matrix3().identity().tupleMultiply(self.a)
    self.assertTrue(result == self.a)

  def test_transposing_a_4x4_matrix(self):
    '''Test case function for transposing a 4x4 matrix'''
    self.A = Matrix4(0, 9, 3, 0,
                     9, 8, 0, 8,
                     1, 8, 5, 3,
                     0, 0, 5, 8)
    
    result = self.A.transpose()
    self.assertTrue(result == Matrix4(0, 9, 1, 0,
                                      9, 8, 8, 0,
                                      3, 0, 5, 5,
                                      0, 8, 3, 8))
    
  def test_transposing_a_3x3_matrix(self):
    '''Test case function for transposing a 3x3 matrix'''
    self.A = Matrix3(0, 9, 3,
                     9, 8, 0,
                     1, 8, 5)
    
    result = self.A.transpose()
    self.assertTrue(result == Matrix3(0, 9, 1,
                                      9, 8, 8,
                                      3, 0, 5))
    
  def test_transposing_the_4x4_identity_matrix(self):
    '''Test case function for transposing the 4x4 identity matrix'''
    self.A = Matrix4().identity().transpose()
    self.assertTrue(self.A == Matrix4().identity())

  def test_transposing_the_3x3_identity_matrix(self):
    '''Test case function for transposing the 3x3 identity matrix'''
    self.A = Matrix3().identity().transpose()
    self.assertTrue(self.A == Matrix3().identity())

  def test_calculating_the_determinant_of_a_2x2_matrix(self):
    '''Test case function for calculating the determinant of a 2x2 matrix'''
    self.A = Matrix2(1, 5,
                     -3, 2)
    self.assertEqual(self.A.determinant(), 17)

  def test_submatrix_of_3x3_matrix_is_2x2_matrix(self):
    '''Test case function for showing the submatrix of a 3x3 matrix is a 2x2 matrix'''
    self.A = Matrix3(1, 5, 0,
                     -3, 2, 7,
                     0, 6, -3)
    result = self.A.submatrix(0, 2)
    expected = Matrix2(-3, 2,
                       0, 6)
    self.assertTrue(result == expected)

  def test_submatrix_of_4x4_matrix_is_3x3_matrix(self):
    '''Test case function for showing the submatrix of a 4x4 matrix is a 3x3 matrix'''
    self.A = Matrix4(-6, 1, 1, 6,
                     -8, 5, 8, 6,
                     -1, 0, 8, 2,
                     -7, 1, -1, 1)
    result = self.A.submatrix(2, 1)
    expected = Matrix3(-6, 1, 6,
                       -8, 8, 6,
                       -7, -1, 1)
    self.assertTrue(result == expected)

  def test_calculate_minor_of_3x3_matrix(self):
    '''Test case function for calculating a minor of a 3x3 matrix'''
    self.A = Matrix3(3, 5, 0,
                     2, -1, -7,
                     6, -1, 5)
    self.B = self.A.submatrix(1, 0)
    self.assertEqual(self.B.determinant(), 25)
    self.assertEqual(self.A.minor(1, 0), 25)

  def test_calculate_cofactor_of_3x3_matrix(self):
    '''Test case function for calculating a cofactor of a 3x3 matrix'''
    self.A = Matrix3(3, 5, 0,
                     2, -1, -7,
                     6, -1, 5)
    self.assertEqual(self.A.minor(0, 0), -12)
    self.assertEqual(self.A.cofactor(0, 0), -12)
    self.assertEqual(self.A.minor(1, 0), 25)
    self.assertEqual(self.A.cofactor(1, 0), -25)

  def test_calculate_determinant_of_3x3_matrix(self):
    '''Test case function for calculating the determinant of a 3x3 matrix'''
    self.A = Matrix3(1, 2, 6,
                     -5, 8, -4,
                     2, 6, 4)
    self.assertEqual(self.A.cofactor(0, 0), 56)
    self.assertEqual(self.A.cofactor(0, 1), 12)
    self.assertEqual(self.A.cofactor(0, 2), -46)
    self.assertEqual(self.A.determinant(), -196)

  def test_calculate_determinant_of_4x4_matrix(self):
    '''Test case function for calculating the determinant of a 4x4 matrix'''
    self.A = Matrix4(-2, -8, 3, 5,
                     -3, 1, 7, 3,
                     1, 2, -9, 6,
                     -6, 7, 7, -9)
    self.assertEqual(self.A.cofactor(0, 0), 690)
    self.assertEqual(self.A.cofactor(0, 1), 447)
    self.assertEqual(self.A.cofactor(0, 2), 210)
    self.assertEqual(self.A.cofactor(0, 3), 51)
    self.assertEqual(self.A.determinant(), -4071)

  def test_calculate_determinant_of_4x4_matrix(self):
    '''Test case function for calculating the determinant of a 4x4 matrix'''
    self.A = Matrix4(-2, -8, 3, 5,
                     -3, 1, 7, 3,
                     1, 2, -9, 6,
                     -6, 7, 7, -9)
    self.assertEqual(self.A.cofactor(0, 0), 690)
    self.assertEqual(self.A.cofactor(0, 1), 447)
    self.assertEqual(self.A.cofactor(0, 2), 210)
    self.assertEqual(self.A.cofactor(0, 3), 51)
    self.assertEqual(self.A.determinant(), -4071)

  def test_invertible_4x4_matrix_for_invertibility(self):
    '''Test case function for testing a invertible 4x4 matrix for invertibility'''
    self.A = Matrix4(6, 4, 4, 4,
                     5, 5, 7, 6,
                     4, -9, 3, -7,
                     9, 1, 7, -6)
    
    self.assertEqual(self.A.determinant(), -2120)
    self.assertTrue(self.A.invertible())

  def test_invertible_3x3_matrix_for_invertibility(self):
    '''Test case function for testing a invertible 3x3 matrix for invertibility'''
    self.A = Matrix3(6, 4, 4,
                     5, 5, -7,
                     4, -9, 3)
    
    self.assertEqual(self.A.determinant(), -720)
    self.assertTrue(self.A.invertible())

  def test_noninvertible_4x4_matrix_for_invertibility(self):
    '''Test case function for testing a noninvertible 4x4 matrix for invertibility'''
    self.A = Matrix4(-4, 2, -2, -3,
                     9, 6, 2, 6,
                     0, -5, 1, -5,
                     0, 0, 0, 0)
    
    self.assertEqual(self.A.determinant(), 0)
    self.assertFalse(self.A.invertible())

  def test_noninvertible_3x3_matrix_for_invertibility(self):
    '''Test case function for testing a noninvertible 3x3 matrix for invertibility'''
    self.A = Matrix3(-4, 2, -2,
                     0, -5, 1,
                     0, 0, 0)
    
    self.assertEqual(self.A.determinant(), 0)
    self.assertFalse(self.A.invertible())

  def test_calculate_inverse_of_4x4_matrix(self):
    '''Test case function for calculating the inverse of a 4x4 matrix'''
    self.A = Matrix4(-5, 2, 6, -8,
                     1, -5, 1, 8,
                     7, 7, -6, -7,
                     1, -3, 7, 4)
    self.B = self.A.inverse()
    self.assertEqual(self.A.determinant(), 532)
    self.assertEqual(self.A.cofactor(2, 3), -160)
    self.assertEqual(self.B.at(3, 2), -160/532)
    self.assertEqual(self.A.cofactor(3, 2), 105)
    self.assertEqual(self.B.at(2, 3), 105/532)
    expected = Matrix4(0.21805, 0.45113, 0.24060, -0.04511,
                      -0.80827, -1.45677, -0.44361, 0.52068,
                      -0.07895, -0.22368, -0.05263, 0.19737,
                      -0.52256, -0.81391, -0.30075, 0.30639)
    self.assertTrue(self.B == expected)

  def test_calculate_inverse_of_3x3_matrix(self):
    '''Test case function for calculating the inverse of a 3x3 matrix'''
    self.A = Matrix3(-5, 2, 6,
                     1, -5, 1,
                     7, 7, -6)
    self.B = self.A.inverse()
    self.assertEqual(self.A.determinant(), 163)
    self.assertEqual(self.A.cofactor(2, 1), 11)
    self.assertEqual(self.B.at(1, 2), 11/163)
    self.assertEqual(self.A.cofactor(1, 2), 49)
    self.assertEqual(self.B.at(2, 1), 49/163)
    expected = Matrix3(0.14110, 0.33128, 0.19631,
                       0.07975, -0.07361, 0.06748,
                       0.25766, 0.30061, 0.14110)
    self.assertTrue(self.B == expected)

  def test_calculate_inverse_of_another_4x4_matrix(self):
    '''Test case function for calculating the inverse of another 4x4 matrix'''
    self.A = Matrix4(8, -5, 9, 2,
                     7, 5, 6, 1,
                     -6, 0, 9, 6,
                     -3, 0, -9, -4)
    self.B = self.A.inverse()
    expected = Matrix4(-0.15385, -0.15385, -0.28205, -0.53846,
                       -0.07692, 0.12308, 0.02564, 0.03077,
                        0.35897, 0.35897, 0.43590, 0.92308,
                       -0.69231, -0.69231, -0.76923, -1.92308)
    self.assertTrue(self.B == expected)

  def test_calculate_inverse_of_another_3x3_matrix(self):
    '''Test case function for calculating the inverse of another 3x3 matrix'''
    self.A = Matrix3(8, -5, 9,
                     -6, 3, 9,
                     -3, 2, -9)
    self.B = self.A.inverse()
    expected = Matrix3(-2.5, -1.5, -4,
                       -4.5, -2.5, -7,
                       -0.16666, -0.05555, -0.33333)
    self.assertTrue(self.B == expected)

  def test_calculate_inverse_of_a_third_4x4_matrix(self):
    '''Test case function for calculating the inverse of a third 4x4 matrix'''
    self.A = Matrix4(9, 3, 0, 9,
                     -5, -2, -6, -3,
                     -4, 9, 6, 4,
                     -7, 6, 6, 2)
    self.B = self.A.inverse()
    expected = Matrix4(-0.04074, -0.07778, 0.14444, -0.22222,
                       -0.07778, 0.03333, 0.36667, -0.33333,
                       -0.02901, -0.14630, -0.10926, 0.12963,
                        0.17778, 0.06667, -0.26667, 0.33333)
    self.assertTrue(self.B == expected)

  def test_multiply_product_of_4x4_matrix_by_its_inverse(self):
    '''Test case function for multiplying a 4x4 matrix's product by its inverse'''
    self.A = Matrix4(3, -9, 7, 3,
                     3, -8, 2, -9,
                     -4, 4, 4, 1,
                     -6, 5, -1, 1)
    self.B = Matrix4(8, 2, 2, 2,
                     3, -1, 7, 0,
                     7, 0, 5, 4,
                     6, -2, 0, 5)
    self.C = self.A.matrixMultiply(self.B)
    self.assertTrue(self.C.matrixMultiply(self.B.inverse()) == self.A)

  def test_multiply_product_of_3x3_matrix_by_its_inverse(self):
    '''Test case function for multiplying a 3x3 matrix's product by its inverse'''
    self.A = Matrix3(3, -9, 7,
                     3, -8, 2,
                     -4, 4, 4)
    self.B = Matrix3(8, 2, 2,
                     3, -1, 7,
                     7, 0, 5)
    self.C = self.A.matrixMultiply(self.B)
    self.assertTrue(self.C.matrixMultiply(self.B.inverse()) == self.A)

if __name__ == '__main__':
  unittest.main()