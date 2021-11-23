import unittest
from soda_machine import SodaMachine
import coins
import cans

class TestFillRegister(unittest.TestCase):
    def setUp(self):
        self.register = SodaMachine()
        
        
    def test_fill_register(self):
        register = self.register
        self.assertEqual(len(register.register), 88)
    
class TestFillInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = SodaMachine()
    
    def test_fill_inventory(self):
        inventory = self.inventory
        self.assertEqual(len(inventory.inventory), 30)    

class TestGetCoin(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_get_quarter(self):
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertEqual(returned_coin.name, 'Quarter')
    
    def test_get_dime(self):
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertEqual(returned_coin.name, 'Dime')
        
    def test_get_nickel(self):
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertEqual(returned_coin.name, 'Nickel')
    
    def test_get_penny(self):
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertEqual(returned_coin.name, 'Penny') 
        
    def test_not_valid_coin(self):
        returned_coin = self.soda_machine.get_coin_from_register('Half Dollar')
        self.assertNotIsInstance(returned_coin, coins.Coin)
        
class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_register_has_quarter(self):
        coin = self.soda_machine.register_has_coin('Quarter')
        self.assertTrue(coin, 'Quarter')
    
    def test_register_has_dime(self):
        coin = self.soda_machine.register_has_coin('Dime')
        self.assertTrue(coin, 'Dime')
    
    def test_register_has_nickel(self):
        coin = self.soda_machine.register_has_coin('Nickel')
        self.assertTrue(coin, 'Nickel')
    
    def test_register_has_penny(self):
        coin = self.soda_machine.register_has_coin('Penny')
        self.assertTrue(coin, 'Penny')
    
    def test_not_valid_coin(self):
        coin = self.soda_machine.register_has_coin('Half Dollar')
        self.assertFalse(coin, 'Half Dollar')    

class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_change_value(self):
        price = self.soda_machine.determine_change_value(10, 5)
        self.assertEqual(price, 5)
    
    def test_change_value_1(self):
        price = self.soda_machine.determine_change_value(5, 10)
        self.assertEqual(price, -5)

    def test_change_value_2(self):
        price = self.soda_machine.determine_change_value(10, 10)
        self.assertEqual(price, 0)
    
class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_coin_value(self):
        coin_list = []
        coin_list.append(coins.Quarter())
        coin_list.append(coins.Dime())
        coin_list.append(coins.Nickel())
        coin_list.append(coins.Penny())
        value = self.soda_machine.calculate_coin_value(coin_list)
        self.assertEqual(value, .41)
    
class TestGetInventorySoda(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_get_inventory_cola(self):
        can = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(can.name, 'Cola')
    
    def test_get_inventory_orange_soda(self):
        can = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(can.name, 'Orange Soda')
    
    def test_get_inventory_root_beer(self):
        can = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(can.name, 'Root Beer')
        
    def test_invalid_soda_name(self):
        can = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertIsNone(can)
        
class TestReturnInventory(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_return_inventory(self):
        can = 'Cola'
        self.soda_machine.return_inventory(can)
        self.assertEqual(len(self.soda_machine.inventory), 31)
        
class TestDepositCoinsIntoRegister(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_deposit_into_register(self):
        coin_list = []
        coin_list.append(coins.Quarter())
        coin_list.append(coins.Dime())
        coin_list.append(coins.Nickel())
        coin_list.append(coins.Penny())
        self.soda_machine.deposit_coins_into_register(coin_list)
        self.assertEqual(len(self.soda_machine.register), 92)
        
if __name__ == '__main__':
    unittest.main()
        