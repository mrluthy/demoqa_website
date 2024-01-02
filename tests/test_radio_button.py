import pytest
from pylenium.driver import Pylenium

DEMOQA = "https://demoqa.com/elements"
RADIO_BUTTON_ID = "#item-2"
YES_RADIO_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[2]/label"
IMPRESSIVE_RADIO_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/label"
NO_RADIO_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[4]/label"
NO_RADIO_ID = "#noRadio"
SELECTED_TEXT_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/p/span"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(RADIO_BUTTON_ID).click()
    yield


def test_click_yes_radio(py: Pylenium, url_nav):
    py.getx(YES_RADIO_XPATH).click()
    assert py.getx(SELECTED_TEXT_XPATH).get_property("textContent") == "Yes"
    assert py.getx(SELECTED_TEXT_XPATH).css_value("color") == "rgba(40, 167, 69, 1)"


def test_click_impressive_radio(py: Pylenium, url_nav):
    py.getx(IMPRESSIVE_RADIO_XPATH).click()
    assert py.getx(SELECTED_TEXT_XPATH).get_property("textContent") == "Impressive"
    assert py.getx(SELECTED_TEXT_XPATH).css_value("color") == "rgba(40, 167, 69, 1)"


def test_no_cursor_no_radio(py: Pylenium, url_nav):
    assert py.getx(NO_RADIO_XPATH).css_value("cursor") == "not-allowed"
    assert py.getx(NO_RADIO_XPATH).css_value("color") == "rgba(108, 117, 125, 1)"
