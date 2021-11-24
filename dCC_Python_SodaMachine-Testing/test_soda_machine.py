import unittest
from soda_machine import SodaMachine
import coins
import cans

class TestFillRegister(unittest.TestCase):
    def setUp(self):
        self.register = SodaMachine()
        
        
    def test_fill_register(self):
        """Runs test to check register is being filled with coins"""
        register = self.register
        self.assertEqual(len(register.register), 88)
    
class TestFillInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = SodaMachine()
    
    def test_fill_inventory(self):
        """Runs test to check Soda Machines can list is being filled with cans"""
        inventory = self.inventory
        self.assertEqual(len(inventory.inventory), 30)    

class TestGetCoin(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_get_quarter(self):
        """Runs test to check that Quarter is being removed and returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertEqual(returned_coin.name, 'Quarter')
    
    def test_get_dime(self):
        """Runs test to check that Dime is being removed and returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertEqual(returned_coin.name, 'Dime')
        
    def test_get_nickel(self):
        """Runs test to check that Nickel is being removed and returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertEqual(returned_coin.name, 'Nickel')
    
    def test_get_penny(self):
        """Runs test to check that Penny is being removed and returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertEqual(returned_coin.name, 'Penny') 
        
    def test_not_valid_coin(self):
        """Runs test to check that invalid input returns None"""
        returned_coin = self.soda_machine.get_coin_from_register('Half Dollar')
        self.assertIsNone(returned_coin)
        
class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_register_has_quarter(self):
        """Runs test to check Quarter will return True"""
        coin = self.soda_machine.register_has_coin('Quarter')
        self.assertTrue(coin, 'Quarter')
    
    def test_register_has_dime(self):
        """Runs test to check Dime will return True"""
        coin = self.soda_machine.register_has_coin('Dime')
        self.assertTrue(coin, 'Dime')
    
    def test_register_has_nickel(self):
        """Runs test to check Nickel will return True"""
        coin = self.soda_machine.register_has_coin('Nickel')
        self.assertTrue(coin, 'Nickel')
    
    def test_register_has_penny(self):
        """Runs test to check Penny will return True"""
        coin = self.soda_machine.register_has_coin('Penny')
        self.assertTrue(coin, 'Penny')
    
    def test_not_valid_coin(self):
        """Runs test to check invalid input returns False"""
        coin = self.soda_machine.register_has_coin('Half Dollar')
        self.assertFalse(coin, 'Half Dollar')    

class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_change_value(self):
        """Runs test to check amount of change needed by subtracting payment amount from can price"""
        price = self.soda_machine.determine_change_value(10, 5)
        self.assertEqual(price, 5)
    
    def test_change_value_1(self):
        """Runs test to check amount of change needed by subtracting can price from payment amount"""
        price = self.soda_machine.determine_change_value(5, 10)
        self.assertEqual(price, -5)

    def test_change_value_2(self):
        """Runs test to check amount of changed needed when payment and can price are equal"""
        price = self.soda_machine.determine_change_value(10, 10)
        self.assertEqual(price, 0)
    
class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_coin_value(self):
        """Runs test to check when a coin list is passed in, returns the total value of the coins in the list"""
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
        """Runs test to check when Cola is selected, Cola is returned"""
        can = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(can.name, 'Cola')
    
    def test_get_inventory_orange_soda(self):
        """Runs test to check when Orange Soda is selected, Orange Soda is returned"""
        can = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(can.name, 'Orange Soda')
    
    def test_get_inventory_root_beer(self):
        """Runs test to check when Root Beer is selected, Root Beer is returned"""
        can = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(can.name, 'Root Beer')
        
    def test_invalid_soda_name(self):
        """Runs test to check when invalid input entered, None is returned"""
        can = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertIsNone(can)
        
class TestReturnInventory(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_return_inventory(self):
        """Runs test to add cans back into inventory"""
        can = 'Cola'
        self.soda_machine.return_inventory(can)
        self.assertEqual(len(self.soda_machine.inventory), 31)
        
class TestDepositCoinsIntoRegister(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_deposit_into_register(self):
        """Runs test to check when list of coins is passed in, coins are being added to the register"""
        coin_list = []
        coin_list.append(coins.Quarter())
        coin_list.append(coins.Dime())
        coin_list.append(coins.Nickel())
        coin_list.append(coins.Penny())
        self.soda_machine.deposit_coins_into_register(coin_list)
        self.assertEqual(len(self.soda_machine.register), 92)
        
if __name__ == '__main__':
    unittest.main()
        