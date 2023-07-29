import unittest
from library import TestJob
class TestMyCode(unittest.TestCase):
  async def test_square(self):
    result = await TestJob().square(2)
    self.assertEqual(result, 4)
  async def test_cube(self):
    result = await TestJob().cube(3)
    self.assertEqual(result, 27)
  async def test_sqrt(self):
    result = await TestJob().sqrt(9)
    self.assertEqual(result, 3.0)
if __name__ == '__main__':
unittest.main()
