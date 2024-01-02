from pylenium.driver import Pylenium
import pytest

DEMOQA = "https://demoqa.com/elements"
UPLOAD_AND_DOWNLOAD_NAV_ID = "#item-7"
UPLOAD_ID = "#uploadFile"
INTERACTIONS_BUTTON_XPATH = "//*[@id='app']/div/div/div[2]/div[1]/div/div/div[5]/span/div/div[1]/text()"
UPLOADED_FILE_PATH_ID = "#uploadedFilePath"
DOWNLOAD_BUTTON_ID = "#downloadButton"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(UPLOAD_AND_DOWNLOAD_NAV_ID).scroll_into_view().click()
    yield


def test_up_and_download(py: Pylenium, url_nav):
    py.get(UPLOAD_ID).upload("/Users/michael.luthy/PycharmProjects/pythonProject/elements/valid.png")
    assert py.get(UPLOADED_FILE_PATH_ID).get_property("outerText") == "C:\\fakepath\\valid.png"
    py.get(DOWNLOAD_BUTTON_ID).click()
