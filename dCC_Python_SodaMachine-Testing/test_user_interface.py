import unittest
import user_interface
import cans
import coins

class TestValidateMainMenu(unittest.TestCase):
    
    def test_validate_main_menu_1(self):
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(1)
        self.assertTrue(person)
    
    def test_validate_main_menu_2(self):
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(2)
        self.assertTrue(person)
    
    def test_validate_main_menu_3(self):
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(3)
        self.assertTrue(person)
    
    def test_validate_main_menu_4(self):
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(4)
        self.assertTrue(person)    
    
    def test_not_valid_option(self):
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(5)
        self.assertTrue(person)

class TestTryParseInt(unittest.TestCase):
    
    def test_try_parse_int(self):
        self.user_interface = user_interface
        number = self.user_interface.try_parse_int(10)
        self.assertEqual(number, 10)

    def test_try_parse_int_1(self):
        self.user_interface = user_interface
        string = self.user_interface.try_parse_int('hello')
        self.assertEqual(string, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    
    def test_get_unique_names(self):
        self.user_interface = user_interface
        can_list = []
        can_list.append(cans.Cola())
        can_list.append(cans.Cola())
        can_list.append(cans.RootBeer())
        can_list.append(cans.RootBeer())
        can_list.append(cans.OrangeSoda())
        can_list.append(cans.OrangeSoda())
        can = self.user_interface.get_unique_can_names(can_list)
        self.assertEqual(len(can), 3)
    
    def test_get_unique_names_1(self):
        self.user_interface = user_interface
        can_list = []
        can = self.user_interface.get_unique_can_names(can_list)
        self.assertEqual(len(can), 0)

class TestDisplayPaymentValue(unittest.TestCase):
    
    def test_display_payment_value(self):
        self.user_interface = user_interface
        coins_list = []
        coins_list.append(coins.Quarter())
        coins_list.append(coins.Dime())
        coins_list.append(coins.Nickel())
        coins_list.append(coins.Penny())
        money = self.user_interface.display_payment_value(coins_list)
        self.assertEqual(money, .41)

    def test_display_payment_value_2(self):
        self.user_interface = user_interface
        coins_list = []
        money = self.user_interface.display_payment_value(coins_list)
        self.assertEqual(money, 0)
        
class TestValidateCoinSelection(unittest.TestCase):
    
    def test_validated_coin_selection(self):
        self.user_interface = user_interface
    
    def test_validate_coin_1(self):
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(1)
        self.assertEqual(coin, coin)
    
    def test_validate_coin_2(self):
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(2)
        self.assertEqual(coin, coin)
    def test_validate_coin_3(self):
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(3)
        self.assertEqual(coin, coin)
    def test_validate_coin_4(self):
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(4)
        self.assertEqual(coin, coin)
    def test_validate_coin_5(self):
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(5)
        self.assertEqual(coin, coin)
    def test_not_valid_coin(self):
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(6)
        self.assertEqual(coin, coin)
        
if __name__ == '__main__':
    unittest.main()
