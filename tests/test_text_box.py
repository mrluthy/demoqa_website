from pylenium.driver import Pylenium
import pytest

DEMOQA = "https://demoqa.com/elements"
TEXTBOX_NAV_ID = "#item-0"
FULL_NAME_ID = "#userName"
EMAIL_ID = "#userEmail"
CURRENT_ADDRESS_ID = "#currentAddress"
PERMANENT_ADDRESS_ID = "#permanentAddress"
SUBMIT_BUTTON_ID = "#submit"
RESULT_NAME_ID = "#name"
RESULT_EMAIL_ID = "#email"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(TEXTBOX_NAV_ID).click()
    yield


def test_text_box(py: Pylenium, url_nav):
    py.get(FULL_NAME_ID).type("Bul Kathos")
    py.get(EMAIL_ID).type("theimmortalking@barbarian.com")
    py.get(SUBMIT_BUTTON_ID).click()
    assert py.get(RESULT_NAME_ID).should().have_text("Name:Bul Kathos")
    assert py.get(RESULT_EMAIL_ID).should().have_text("Email:theimmortalking@barbarian.com")


def test_text_box_error(py: Pylenium, url_nav):
    py.get(FULL_NAME_ID).type("Bul Kathos")
    py.get(EMAIL_ID).type("theimmortalking")
    py.get(SUBMIT_BUTTON_ID).click()
    assert py.get(EMAIL_ID).css_value("border") == "1px solid rgb(206,212,218)" or "1px solid rgb(246,211,219)"


def test_submit_btn_color(py: Pylenium, url_nav):
    assert py.get(SUBMIT_BUTTON_ID).css_value("background-color") == "rgba(0, 123, 255, 1)"
