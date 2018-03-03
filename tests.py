import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver


class SimpleBrowserTest(unittest.TestCase):
    """Class to illustrate a basic webdriver test case."""

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)
        self.browser.get("https://google.com")

    def test_google_search_result_headers(self):
        """Ensure first page google results have query text in their headers."""
        SEARCH_BAR_XPATH = "//input[@name='q']"
        RESULT_HEADERS_XPATH = "//h3[@class='r']"

        query = "selenium webdriver"

        search_bar = self.browser.find_element(By.XPATH, SEARCH_BAR_XPATH)
        search_bar.send_keys(query)
        search_bar.submit()

        for result in self.browser.find_elements(By.XPATH, RESULT_HEADERS_XPATH):
            # Ensure result headers contain what was searched for.
            if result.text.strip():
                self.assertTrue(
                    (query.lower() in result.text.lower()), 
                    "Header '{}' doesn't contain search text.".format(result.text)
                )
                print("PASSED: {}".format(result.text))

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()