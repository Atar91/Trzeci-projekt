import unittest
import grupowe

class test_grupowe(unittest.TestCase):

    def test_capitalize(self):
        txt = grupowe.podnies("ala ma kota")
        self.assertEqual(txt, "Ala Ma Kota")

if __name__ == '__main__':
    unittest.main()
