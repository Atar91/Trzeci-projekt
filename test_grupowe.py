import unittest
import grupowe

class test_grupowe(unittest.TestCase):

    def test_capitalize(self):
        txt = grupowe.podnies("ala ma kota")
        self.assertEqual(txt, "Ala ma kota")

    def test_lower(self):
        txt = grupowe.poloz("ALA MA KOTA")
        self.assertEqual(txt, "ala ma kota")

    def test_replace(self):
        txt = grupowe.zamien("Ala ma kota")
        self.assertEqual(txt, "Ala ma psa")

    def test_count(self):
        txt = grupowe.policz("Lubie jablka, jablka sa pyszne")
        self.assertEqual(txt, 2)

if __name__ == '__main__':
    unittest.main()
