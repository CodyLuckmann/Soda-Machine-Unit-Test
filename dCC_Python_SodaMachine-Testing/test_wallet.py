import unittest
from wallet import Wallet



class TestFillWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()
        
    def see_money_list(self):
        self.assertEqual(len(self.wallet.money, 88))
        
        
if __name__ == '__main__':
    unittest.main()
                
