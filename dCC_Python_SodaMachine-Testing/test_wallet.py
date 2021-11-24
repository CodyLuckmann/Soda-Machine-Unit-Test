import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    def setUp(self): 
        self.wallet = Wallet()
        
    def test_fill_wallet(self):
        """Runs test to check the wallet is being filled with coins """
        wallet = self.wallet.money
        self.assertEqual(len(wallet), 88)
        
if __name__ == '__main__':
    unittest.main()
    
    
