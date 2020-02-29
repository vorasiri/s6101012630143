from selenium import webdriver

def test_user_can_checkout_homepage(self):
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')


def test_user_can_calculate_numbers(self):
    # Found x and y field
    variableX = self.browser.find_element_by_id('x')
    variableY = self.browser.find_element_by_id('y')
    # Found operator buttons
    button_plus = self.browser.find_element_by_id('op_plus')
    self.assertTrue(button_plus)
    button_minus = self.browser.find_element_by_id('op_minus')
    self.assertTrue(button_minus)
    button_mul = self.browser.find_element_by_id('op_mul')
    self.assertTrue(button_mul)
    button_divide = self.browser.find_element_by_id('op_divide')
    self.assertTrue(button_divide)
    # Type value x=150.23, y=90 and click minus button
    variableX.send_keys('150.23')
    variableX.send_keys('90')
    button_minus.send_keys(Keys.ENTER)