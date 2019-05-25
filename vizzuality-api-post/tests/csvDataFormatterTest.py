import unittest, sys
sys.path.append("..")
from dataFormatter import csvDataFormatter

class csvDataFormatterTest(unittest.TestCase):

    def test_setEncondingUtf8(self):
        fakeLine = b'Nina Simone,Aretha Franklin'
        result = csvDataFormatter.setEncodingUtf8(fakeLine)
        self.assertEqual(result, 'Nina Simone,Aretha Franklin')

    def test_removeNewLineCharactersRN(self):
        fakeLine = 'Vicente Amigo,Begun\r\n'
        result = csvDataFormatter.removeNewLineCharactersRN(fakeLine)
        self.assertEqual(result, 'Vicente Amigo,Begun')

    def test_splitLineCommaSeparated(self):
        fakeLine = 'Eduard Punset,Anthony Hopkins'
        result = csvDataFormatter.splitLineCommaSeparated(fakeLine)
        self.assertEqual(result, ['Eduard Punset', 'Anthony Hopkins'])

if __name__ == '__main__':
    unittest.main()