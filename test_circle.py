import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
  def test_area_zero_radius(self):
    res = area(0)
    self.assertEqual(res, 0)
  
  def test_area_large_radius(self):
    res = area(100)
    expected = math.pi * 100 * 100
    self.assertAlmostEqual(res, expected, places=10)
  
  def test_perimeter_zero_radius(self):
    res = perimeter(0)
    self.assertEqual(res, 0)
  
  def test_perimeter_large_radius(self):
    res = perimeter(100)
    expected = 2 * math.pi * 100
    self.assertAlmostEqual(res, expected, places=10)


if __name__ == '__main__':
    unittest.main()
