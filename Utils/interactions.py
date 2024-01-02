from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.by import By
from pylenium.driver import Pylenium


class Interactions:

    @staticmethod
    def wait_and_get(py: Pylenium, element, timeout=5):
        """"
        waits and gets the desired element
        :param py: Pylenium driver object
        :param element: web element
        :param timeout: defaulted to wait 5 seconds. Can change default value when calling function
        """
        try:
            py.wait(timeout, use_py=True).until(lambda x: x.find_element(By.ID, element))
            return py.get(f"#{element}")
        except (WebDriverException, TimeoutException, NoSuchElementException, StaleElementReferenceException):
            return None
