import unittest
import user_interface
import cans
import coins

class TestValidateMainMenu(unittest.TestCase):
    
    def test_validate_main_menu_1(self):
        """ Runs test to check when user input is 1 the correct tuple is returned"""
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(1)
        self.assertEqual(person, (True, 1))
    
    def test_validate_main_menu_2(self):
        """ Runs test to check when user input is 2 the correct tuple is returned"""
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(2)
        self.assertEqual(person, (True, 2))
    
    def test_validate_main_menu_3(self):
        """ Runs test to check when user input is 3 the correct tuple is returned"""
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(3)
        self.assertEqual(person, (True,  3))
    
    def test_validate_main_menu_4(self):
        """ Runs test to check when user input is 4 the correct tuple is returned"""
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(4)
        self.assertEqual(person, (True, 4))    
    
    def test_not_valid_option(self):
        """ Runs test to check when user input is not 1-4 returns False, None"""
        self.user_interface = user_interface
        person = self.user_interface.validate_main_menu(5)
        self.assertEqual(person, (False, None))

class TestTryParseInt(unittest.TestCase):
    
    def test_try_parse_int(self):
        """Runs test to check if string can be parsed into an integer"""
        self.user_interface = user_interface
        number = self.user_interface.try_parse_int(10)
        self.assertEqual(number, 10)

    def test_try_parse_int_1(self):
        """Runs test when string can't be parsed to integer, returns 0"""
        self.user_interface = user_interface
        string = self.user_interface.try_parse_int('hello')
        self.assertEqual(string, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    
    def test_get_unique_names(self):
        """Runs test to check when list of cans is passed in of multiple same can names, removes duplicates"""
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
        """Runs test when empty list is passed in length of list remains at 0"""
        self.user_interface = user_interface
        can_list = []
        can = self.user_interface.get_unique_can_names(can_list)
        self.assertEqual(len(can), 0)

class TestDisplayPaymentValue(unittest.TestCase):
    
    def test_display_payment_value(self):
        """Runs test to determine when list of coins is added, returns total payment"""
        self.user_interface = user_interface
        coins_list = []
        coins_list.append(coins.Quarter())
        coins_list.append(coins.Dime())
        coins_list.append(coins.Nickel())
        coins_list.append(coins.Penny())
        money = self.user_interface.display_payment_value(coins_list)
        self.assertEqual(money, .41)

    def test_display_payment_value_2(self):
        """Run test when empty list of coins added, total value equals 0"""
        self.user_interface = user_interface
        coins_list = []
        money = self.user_interface.display_payment_value(coins_list)
        self.assertEqual(money, 0)
        
class TestValidateCoinSelection(unittest.TestCase):
    
    def test_validated_coin_selection(self):
        self.user_interface = user_interface
    
    def test_validate_coin_1(self):
        """Runs test to check when user input is 1, returns correct tuple"""
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(1)
        self.assertEqual(coin, (True, 'Quarter'))
    
    def test_validate_coin_2(self):
        """Runs test to check when user input is 2, returns correct tuple"""
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(2)
        self.assertEqual(coin, (True, 'Dime'))
    
    def test_validate_coin_3(self):
        """Runs test to check when user input is 3, returns correct tuple"""
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(3)
        self.assertEqual(coin, (True, 'Nickel'))
    
    def test_validate_coin_4(self):
        """Runs test to check when user input is 4, returns correct tuple"""
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(4)
        self.assertEqual(coin, (True, 'Penny'))
    
    def test_validate_coin_5(self):
        """Runs test to check when user input is 5, returns correct tuple"""
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(5)
        self.assertEqual(coin, (True, 'Done'))
    
    def test_not_valid_coin(self):
        """Runs test to check when user input is not betwenn 1-5, returns False, None"""
        self.user_interface = user_interface
        coin = self.user_interface.validate_coin_selection(6)
        self.assertEqual(coin, (False, None))
        
if __name__ == '__main__':
    unittest.main()
