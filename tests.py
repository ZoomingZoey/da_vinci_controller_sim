import unittest
import math

import tuple as tp
import utils as ut
from point import Point
from vector import Vector
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
  def test_tuple_is_point(self):
    '''Test case function for checking if a tuple with w=1.0 is a point'''
    self.a = tp.Tuple(4.3, -4.2, 3.1, 1.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.z, 3.1)
    self.assertEqual(self.a.w, 1.0)
    self.assertEqual(self.a.isPoint(), True)
    self.assertEqual(self.a.isVector(), False)

  def test_tuple_is_vector(self):
    '''Test case function for checking if a tuple with w=0.0 is a vector'''
    self.a = tp.Tuple(4.3, -4.2, 3.1, 0.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.z, 3.1)
    self.assertEqual(self.a.w, 0.0)
    self.assertEqual(self.a.isPoint(), False)
    self.assertEqual(self.a.isVector(), True)

  def test_tuple_is_vector(self):
    '''Test case function for checking if a tuple with w=0.0 is a vector'''
    self.a = tp.Tuple(4.3, -4.2, 3.1, 0.0)
    self.assertEqual(self.a.x, 4.3)
    self.assertEqual(self.a.y, -4.2)
    self.assertEqual(self.a.z, 3.1)
    self.assertEqual(self.a.w, 0.0)
    self.assertEqual(self.a.isPoint(), False)
    self.assertEqual(self.a.isVector(), True)

  def test_adding_two_tuples(self):
    '''Test case function for adding two tuples'''
    self.a1 = tp.Tuple(3, -2, 5, 1)
    self.a2 = tp.Tuple(-2, 3, 1, 0)
    result = self.a1 + self.a2
    self.assertTrue(result == tp.Tuple(1, 1, 6, 1))

  def test_negating_a_tuple(self):
    '''Test case function for negating a tuple'''
    self.a = tp.Tuple(1, -2, 3, -4)
    self.assertTrue(-self.a == tp.Tuple(-1, 2, -3, 4))

  def test_multiplying_a_tuple_by_a_scalar(self):
    '''Test case function for multiplying a tuple by a scalar'''
    self.a = tp.Tuple(1, -2, 3, -4)
    result = self.a * 3.5
    self.assertTrue(result == tp.Tuple(3.5, -7, 10.5, -14))

  def test_multiplying_a_tuple_by_a_fraction(self):
    '''Test case function for multiplying a tuple by a fraction'''
    self.a = tp.Tuple(1, -2, 3, -4)
    result = self.a * 0.5
    self.assertTrue(result == tp.Tuple(0.5, -1, 1.5, -2))

  def test_dividing_a_tuple_by_a_scalar(self):
    '''Test case function for dividing a tuple by a scalar'''
    self.a = tp.Tuple(1, -2, 3, -4)
    result = self.a / 2
    self.assertTrue(result == tp.Tuple(0.5, -1, 1.5, -2))

  def test_dot_product_of_two_tuples(self):
    '''Test case function for the dot product of two tuples'''
    self.a = Vector(1, 2, 3)
    self.b = Vector(2, 3, 4)
    result = Vector.dot(self.a, self.b)
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

  def test_tuple_is_point(self):
    '''Test case function for checking that Point() creates tuples with w=1.0'''
    self.p = Point(4, -4, 3)
    self.assertTrue(self.p == tp.Tuple(4, -4, 3, 1))

  def test_subtracting_two_points(self):
    '''Test case function for subtracting two points'''
    self.p1 = Point(3, 2, 1)
    self.p2 = Point(5, 6, 7)
    result = self.p1 - self.p2
    self.assertTrue(result == Vector(-2, -4, -6))

  def test_subtracting_a_vector_from_a_point(self):
    '''Test case function for subtracting a vector from a point'''
    self.p = Point(3, 2, 1)
    self.v = Vector(5, 6, 7)
    result = self.p - self.v
    self.assertTrue(result == Point(-2, -4, -6))

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

  def test_tuple_is_vector(self):
    '''Test case function for checking that Vector() creates tuples with w=0.0'''
    self.v = Vector(4, -4, 3)
    self.assertTrue(self.v == tp.Tuple(4, -4, 3, 0))

  def test_subtracting_two_vectors(self):
    '''Test case function for subtracting two vectors'''
    self.v1 = Vector(3, 2, 1)
    self.v2 = Vector(5, 6, 7)
    result = self.v1 - self.v2
    self.assertTrue(result == Vector(-2, -4, -6))

  def test_subtract_vector_from_zero_vector(self):
    '''Test case function for subtracting a vector from the zero vector'''
    self.zero = Vector(0, 0, 0)
    self.v = Vector(1, -2, 3)
    result = self.zero - self.v
    self.assertTrue(result == Vector(-1, 2, -3))

  def test_compute_vector_magnitude_1(self):
    '''Test case function for computing the magnitude of vector(1, 0, 0)'''
    self.v = Vector(1, 0, 0)
    self.assertTrue(ut.equal(Vector.magnitude(self.v), 1))

  def test_compute_vector_magnitude_2(self):
    '''Test case function for computing the magnitude of vector(0, 1, 0)'''
    self.v = Vector(0, 1, 0)
    self.assertTrue(ut.equal(Vector.magnitude(self.v), 1))

  def test_compute_vector_magnitude_3(self):
    '''Test case function for computing the magnitude of vector(0, 0, 1)'''
    self.v = Vector(0, 0, 1)
    self.assertTrue(ut.equal(Vector.magnitude(self.v), 1))

  def test_compute_vector_magnitude_4(self):
    '''Test case function for computing the magnitude of vector(1, 2, 3)'''
    self.v = Vector(1, 2, 3)
    self.assertTrue(ut.equal(Vector.magnitude(self.v), math.sqrt(14)))

  def test_compute_vector_magnitude_5(self):
    '''Test case function for computing the magnitude of vector(-1, -2, -3)'''
    self.v = Vector(-1, -2, -3)
    self.assertTrue(ut.equal(Vector.magnitude(self.v), math.sqrt(14)))

  def test_normalize_vector_1(self):
    '''Test case function for normalizing vector(4, 0, 0) gives (1, 0, 0)'''
    self.v = Vector(4, 0, 0)
    self.assertTrue(Vector.normalize(self.v) == Vector(1, 0, 0))

  def test_normalize_vector_2(self):
    '''Test case function for normalizing vector(1, 2, 3)'''
    self.v = Vector(1, 2, 3)
    self.assertTrue(Vector.normalize(self.v) == Vector(0.26726, 0.53452, 0.80178))

  def test_magnitude_of_normalized_vector(self):
    '''Test case function for the magnitude of a normalized vector'''
    self.v = Vector(1, 2, 3)
    norm = Vector.normalize(self.v)
    self.assertEqual(Vector.magnitude(norm), 1)

  def test_cross_product_of_two_vectors(self):
    '''Test case function for the cross product of two vectors'''
    self.a = Vector(1, 2, 3)
    self.b = Vector(2, 3, 4)
    self.assertTrue(Vector.cross(self.a, self.b) == Vector(-1, 2, -1))
    self.assertTrue(Vector.cross(self.b, self.a) == Vector(1, -2, 1))

  class TestMatrix4(unittest.TestCase):
  
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

  def test_identical_matrix_equality(self):
    '''Test case function for matrix equality with identical matrices'''
    self.A = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.B = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.assertTrue(self.A == self.B)

  def test_different_matrix_equality(self):
    '''Test case function for matrix equality with different matrices'''
    self.A = Matrix4(1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 8, 7, 6,
                     5, 4, 3, 2)
    
    self.B = Matrix4(2, 3, 4, 5,
                     6, 7, 8, 9,
                     8, 7, 6, 5,
                     4, 3, 2, 1)
    
    self.assertTrue(self.A != self.B)

if __name__ == '__main__':
  unittest.main()