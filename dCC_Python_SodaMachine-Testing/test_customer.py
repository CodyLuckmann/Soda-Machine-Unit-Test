import unittest
from customer import Customer
import cans
import coins
from coins import Nickel, Dime, Quarter

class TestGetWalletCoin(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer()
        
    def test_get_quarter(self):
        """Runs test to remove and return Quarter"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.name, 'Quarter')
        
    def test_get_dime(self):
        """Runs test to remove and return Dime"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.name, 'Dime')
        
    def test_get_nickel(self):
        """Runs test to remove and return Nickel"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.name, 'Nickel')
        
    def test_get_penny(self):
        """Runs test to remove and return Penny"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.name, 'Penny')
        
    def test_not_valid_coin(self):
        """Runs test to return None when coin name is invalid"""
        returned_coin = self.customer.get_wallet_coin('Half Dollar')
        self.assertIsNone(returned_coin)
        
class TestAddCoinsToWallet(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
        
    def test_add_coins(self):
        """Runs test to add coins from a list into the wallets money list"""
        coin_list = [coins.Quarter(), coins.Penny(), coins.Dime()]
        coin = self.customer.add_coins_to_wallet(coin_list)
        self.assertEqual(len(self.customer.wallet.money), 91)
        
    def test_empty_list(self):
        """Runs test to add empty coin list to wallets money list, money list should stay the same"""
        coin_list = []
        self.customer.add_coins_to_wallet(coin_list)
        self.assertEqual(len(self.customer.wallet.money), 88)
        
class TestAddCanToBackpack(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()
        
    def test_add_can(self):
        """Runs test to add can into backpacks purchased_cans list"""
        self.customer.add_can_to_backpack(cans.Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
        
    def test_add_another_can(self):
        """Runs test to add can into backpacks purchased_cans list"""
        self.customer.add_can_to_backpack(cans.OrangeSoda())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
        
    def test_third_can(self):
        """Runs test to add can into backpacks purchased_cans list"""
        self.customer.add_can_to_backpack(cans.RootBeer())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
                
        
if __name__ == '__main__':
    unittest.main()
        