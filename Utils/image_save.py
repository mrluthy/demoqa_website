from pylenium.driver import Pylenium
import os
from pathlib import Path

from selenium.common import WebDriverException, NoSuchElementException, TimeoutException, StaleElementReferenceException


class ImageSaveHandler:
    VALID_IMAGE_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[1]"
    BROKEN_IMAGE_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/img[2]"

    @staticmethod
    def save_images(py: Pylenium):
        """
        Function attempts to save the two images on demoqa.com/broken page.
        The second image is invalid and therefore should not be saved.
        :param py: driver instance
        :return: None
        """
        try:
            py.getx(ImageSaveHandler.VALID_IMAGE_XPATH).screenshot(
                os.path.join(Path(__file__).parent.parent, "elements/valid.png"))
            py.getx(ImageSaveHandler.BROKEN_IMAGE_XPATH).screenshot(
                os.path.join(Path(__file__).parent.parent, "elements/broken.png"))
        except WebDriverException:
            pass
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            return None
