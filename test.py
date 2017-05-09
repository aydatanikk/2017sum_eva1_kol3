import unittest
from TestMatrix import addMatrix,subMatrix,mulMatrix

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_addMatrix(self):
        self.assertEqual( addMatrix([1][4],[6][2]),[7][6])

    def test_subMatrix(self):
        self.assertEqual( subMatrix([8][8],[1][6]),[7][2])
       
    def test_mulMatrix(self):
        self.assertEqual( multiply([0][0],[0]),[0][0])

if __name__ == '__main__':
    unittest.main()
