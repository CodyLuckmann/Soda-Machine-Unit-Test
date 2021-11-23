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
        # coin_list = len(self.customer.wallet.money)
        # self.customer.add_coins_to_wallet(Nickel(), Dime(), Quarter())
        coin_list = [coins.Quarter, coins.Penny, coins.Dime]
        coin = self.customer.add_coins_to_wallet(coin_list)
        self.assertEqual(len(self.customer.wallet.money), 91)
        
    def test_empty_list(self):
        coin_list = []
        coin = self.customer.add_coins_to_wallet(coin_list)
        self.assertEqual(len(self.customer.wallet.money), 88)
        
        


        
if __name__ == '__main__':
    unittest.main()
        