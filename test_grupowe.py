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
        txt = grupowe.policz("Ala ma kota", 'jablka')
        self.assertEqual(txt, 0)
        txt = grupowe.policz("Ala ma kota", 'kota')
        self.assertEqual(txt, 1)


if __name__ == '__main__':
    unittest.main()
