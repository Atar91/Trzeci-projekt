import unittest
import grupowe

class test_grupowe(unittest.TestCase):

    def test_capitalize(self):
        txt = grupowe.podnies("ala ma kota")
        self.assertEqual(txt, "Ala ma kota")

    def test_lower(self):
        txt = grupowe.poloz("ALA MA KOTA")
        self.assertEqual(txt, "ala ma kota")

if __name__ == '__main__':
    unittest.main()
