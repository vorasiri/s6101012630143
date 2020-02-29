from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
def test_user_can_checkout_homepage(self):
    browser.get('http://localhost:8000')
    assert 'HOME' in browser.title
    time.sleep(30)
    self.assertIn('Calculator POST method', [link.text for link in main.find_elements_by_tag_name('a')])
    self.assertIn('Calculator GET method', [link.text for link in main.find_elements_by_tag_name('a')])
    self.assertIn('About', [link.text for link in main.find_elements_by_tag_name('a')])

def test_user_can_calculate_numbers(self):
    
    browser.get('http://localhost:8000')
    time.sleep(30)
    self.assertIn('Calculator POST method', [link.text for link in main.find_elements_by_tag_name('a')])
    
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
    variableX.send_keys('150.2')
    time.sleep(10)
    variableY.send_keys('90')
    time.sleep(10)
    button_minus.send_keys(Keys.ENTER)
    time.sleep(30)
    # Check the result
    self.assertIn('Result:', [link.text for link in main.find_elements_by_tag_name('span')])
    self.assertIn('60.2', [link.text for link in main.find_elements_by_tag_name('span')])
    time.sleep(30)