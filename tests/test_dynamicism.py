import pytest
from pylenium.driver import Pylenium

from Utils.interactions import Interactions

DEMOQA = "https://demoqa.com/elements"
DYNAMIC_PROPERTIES_NAV_ID = "#item-8"
ENABLE_AFTER_ID = "#enableAfter"
VISIBLE_AFTER_ID = "#visibleAfter"
UPDATED_VISIBLE_AFTER_ID = "visibleAfter"
COLOR_CHANGE_ID = "#colorChange"
COLOR_CHANGE_NO_HASH = "colorChange"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(DYNAMIC_PROPERTIES_NAV_ID).scroll_into_view().click()
    yield


def test_get_dynamic_text_element(py: Pylenium, url_nav):
    assert py.contains("This text has random Id").get_property("textContent") == "This text has random Id"


def test_button_dynamic_enabled(py: Pylenium, url_nav):
    assert py.get(ENABLE_AFTER_ID).click()


def test_button_dynamic_disabled(py: Pylenium, url_nav):
    Interactions.wait_and_get(py, UPDATED_VISIBLE_AFTER_ID)
