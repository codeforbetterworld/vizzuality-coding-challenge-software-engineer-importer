import unittest
import sys
sys.path.append("..")
from dataRetriever import getCsvData

class getCsvDataTest(unittest.TestCase):

    def test_getColumns(self):
        fakecsvData = [['Country', 'City'], ['Switzerland', 'Eduard Punset']]
        result = getCsvData.getCsvColumns(fakecsvData)
        self.assertEqual(result, ['Country', 'City'])

if __name__ == '__main__':
    unittest.main()