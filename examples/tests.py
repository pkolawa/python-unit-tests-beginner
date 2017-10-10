import unittest

#Import class Move
import moves

class MoveTests(unittest.TestCase):
  def test_two_plus_two(self):
    assert 5 + 5 == 10

  def test_one_plus_one(self):
    assert not 1 + 1 == 3

#If we run this script directly, run the tests:
if __name__ == '__main__':
  unittest.main()
