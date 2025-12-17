import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
  def test_area_zero_side(self):
    res = area(0)
    self.assertEqual(res, 0)

  def test_area_large_side(self):
    res = area(100)
    self.assertEqual(res, 1000)
    
  def test_area_float_side(self):
    res = area(2.5)
    self.assertEqual(res, 6.25)
  
  def test_perimeter_zero_side(self):
    res = perimeter(0)
    self.assertEqual(res, 0)
  
  def test_perimeter_large_side(self):
    res = perimeter(100)
    self.assertEqual(res, 400)
  
  def test_perimeter_float_side(self):
    res = perimeter(2.5)
    self.assertEqual(res, 10)


if __name__ == '__main__':
    unittest.main()
