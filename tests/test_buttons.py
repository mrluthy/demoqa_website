from Utils.interactions import Interactions

from pylenium.driver import Pylenium
import pytest

DEMOQA = "https://demoqa.com/elements"
BUTTON_NAV_ID = "#item-4"
PY_DOUBLE_CLICK_BUTTON_ID = "#doubleClickBtn"
DOUBLE_CLICK_BUTTON_ID = "doubleClickBtn"
DOUBLE_CLICK_MESSAGE = "#doubleClickMessage"
RIGHT_CLICK_BUTTON_ID = "#rightClickBtn"
RIGHT_CLICK_MESSAGE = "#rightClickMessage"
DYNAMIC_CLICK_XPATH = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button"
DYNAMIC_CLICK_MESSAGE = "#dynamicClickMessage"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(BUTTON_NAV_ID).click()
    yield


def test_button_clicks(py: Pylenium, url_nav):
    Interactions.wait_and_get(py, DOUBLE_CLICK_BUTTON_ID).double_click()
    assert py.get(DOUBLE_CLICK_MESSAGE).get_attribute("textContent") == "You have done a double click"
    py.getx(DYNAMIC_CLICK_XPATH).click()
    assert py.get(DYNAMIC_CLICK_MESSAGE).get_attribute("textContent") == "You have done a dynamic click"
    py.get(RIGHT_CLICK_BUTTON_ID).right_click()
    assert py.get(RIGHT_CLICK_MESSAGE).get_attribute("textContent") == "You have done a right click"
