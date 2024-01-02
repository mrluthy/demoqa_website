import pytest
from pylenium.driver import Pylenium

DEMOQA = "https://demoqa.com/elements"
CHECKBOX_NAV_ID = "#item-1"
EXPAND_ALL_XPATH = "//*[@id='tree-node']/div/button[1]"
RESULT_ID = "#result"
TEXT_SUCCESS_XPATH = "//*[@id='result']/span[2]"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(CHECKBOX_NAV_ID).click()
    yield


def test_click_checkbox(py: Pylenium, url_nav):
    py.getx(EXPAND_ALL_XPATH).click()
    py.contains("Public").click()
    assert py.get(RESULT_ID).get_property("textContent") == "You have selected :public"
    assert py.getx(TEXT_SUCCESS_XPATH).css_value("color") == "rgba(40, 167, 69, 1)"


def test_click_all_checkboxes(py: Pylenium, url_nav):
    py.contains("Home").click()
    assert py.get(RESULT_ID).children().length() == 18

