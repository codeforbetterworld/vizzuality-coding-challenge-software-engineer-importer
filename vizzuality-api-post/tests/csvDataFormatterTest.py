import unittest, sys
sys.path.append("..")
from dataFormatter import csvDataFormatter

class csvDataFormatterTest(unittest.TestCase):

    def test_splitLine(self):
        fakeLine = 'Eduard Punset,Anthony Hopkins'
        result = csvDataFormatter.splitLine(fakeLine)
        self.assertEqual(result, ['Eduard Punset', 'Anthony Hopkins'])

if __name__ == '__main__':
    unittest.main()