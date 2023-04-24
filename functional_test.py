from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_list_and_retrieve_it_later(self):
        # Erin has heard about a cool new online to-do app. 
        # She goes to check out its homepage 
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        # She types "Buy peacock feathers" into the text box 
        # assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title)
        
        # When she hits enter, the page updates, and now
        # the page has a list with this item "1: Buy peacock feathers" 

        # There is still a text box, and she enters
        # "Use peacock feathers to make a fly"
        
        # The page updates again, and now shows both items on her list
        # Erin wonders whether the site will remember her list.
        # Then she sees that the site has generated 
        # a unique URL with some explanatory text for her

        # She visits that URL and her to-do list is still there
        # Satisfied she goes for a cup of coffee

if __name__ == '__main__':
    unittest.main()