from pylenium.driver import Pylenium
import pytest

DEMOQA = "https://demoqa.com/elements"
LINKS_NAV_ID = "#item-5"
FIRST_LINK_ID = "#simpleLink"
FORBIDDEN_LINK_ID = "#forbidden"
HOME_PAGE_HEADER_XPATH = "//*[@id='app']/header/a"
LINK_RESPONSE_ID = "#linkResponse"
FIXED_BANNER_ID = "#fixedban"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(LINKS_NAV_ID).click()
    yield


def test_web_link(py: Pylenium, url_nav):
    first_link = py.get(FIRST_LINK_ID)
    assert first_link.get_attribute("href") == "https://demoqa.com/"
    assert first_link.get_attribute("text") == "Home"
    assert first_link.css_value("color") == "rgba(0, 123, 255, 1)"
    first_link.click()
    assert py.getx(HOME_PAGE_HEADER_XPATH).get_property("href") == "https://demoqa.com/"


def test_forbidden_link(py: Pylenium, url_nav):
    py.get(FORBIDDEN_LINK_ID).click()
    assert py.get(LINK_RESPONSE_ID).get_property("textContent") == ("Link has responded with staus 403 and status text "
                                                                    "Forbidden")
