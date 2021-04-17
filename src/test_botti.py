import unittest
from arvaus import arvauksen_tarkastaja

class test_arvaus(unittest.TestCase):
    def setUp(self):
        self.tarkastaja = arvauksen_tarkastaja()
    
    def test_aseta_arvattava(self):
        self.tarkastaja.aseta_arvattava("Selen lever")
        self.assertEqual(self.tarkastaja.arvattava, "Selen lever")
        self.tarkastaja.aseta_arvattava("Hyvät ystävät")
        self.assertEqual(self.tarkastaja.arvattava, "Hyvät ystävät")

if __name__ == '__main__':
    unittest.main()