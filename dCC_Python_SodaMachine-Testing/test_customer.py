import unittest
from customer import Customer
import coins



class TestGetWalletCoin(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer()
        
    def test_get_quarter(self):
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.name, 'Quarter')
        
    def test_get_dime(self):
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.name, 'Dime')
        
    def test_get_nickel(self):
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.name, 'Nickel')
        
    def test_get_penny(self):
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.name, 'Penny')
        
    def test_not_valid_coin(self):
        returned_coin = self.customer.get_wallet_coin('Half Dollar')
        self.assertNotIsInstance(returned_coin, coins.Coin)
        
class TestAddCoinsToWallet(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
        
    def test_add_coins(self):
        coin_1 = 'Quarter'
        coin_2 = 'Dime'
        coin_3 = 'Nickel'
        coin_list = [coin_1, coin_2, coin_3]
        result =self.customer.wallet.money(coin_list)
        self.assertEqual(result, len(self
        
        
        
        
if __name__ == '__main__':
    unittest.main()
        