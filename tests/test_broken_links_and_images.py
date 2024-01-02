import pytest
from pylenium.driver import Pylenium
from Utils.image_save import ImageSaveHandler

DEMOQA = "https://demoqa.com/elements"
BROKEN_NAV_ID = "#item-6"
BROKEN_LINK_URL = "https://the-internet.herokuapp.com/status_codes/500"
VALID_LINK_URL = "https://demoqa.com/"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(BROKEN_NAV_ID).click()
    yield


def test_save_images(py: Pylenium, url_nav):
    ImageSaveHandler.save_images(py)


def test_broken_link(py: Pylenium, url_nav):
    py.contains("Click Here for Broken Link").click()
    assert py.url() == BROKEN_LINK_URL


def test_valid_link(py: Pylenium, url_nav):
    py.contains("Click Here for Valid Link").click()
    assert py.url() == VALID_LINK_URL
