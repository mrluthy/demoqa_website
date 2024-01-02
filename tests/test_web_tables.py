from pylenium.driver import Pylenium
import pytest
import tests.test_text_box

DEMOQA = "https://demoqa.com/elements"
WEB_TABLE_NAV_ID = "#item-3"
FIRST_ROW_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div"
EDIT_RECORD_1_ID = "#edit-record-1"
AGE_ID = "#age"
UPDATED_AGE_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[3]"
ADD_RECORD_ID = "#addNewRecordButton"
FIRST_NAME_ID = "#firstName"
LAST_NAME_ID = "#lastName"
EMAIL_ID = "#userEmail"
SALARY_ID = "#salary"
DEPARTMENT_ID = "#department"
NEW_TABLE_ENTRY_XPATH = "//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div"


@pytest.fixture
def url_nav(py, request):
    py.visit(DEMOQA)
    py.get(WEB_TABLE_NAV_ID).click()
    yield


def test_first_row(py: Pylenium, url_nav):
    assert py.getx(FIRST_ROW_XPATH).get_attribute("textContent") == "CierraVega39cierra@example.com10000Insurance "


def test_edit_record_1(py: Pylenium, url_nav):
    py.get(EDIT_RECORD_1_ID).click()
    py.get(AGE_ID).clear()
    py.get(AGE_ID).type("1")
    py.get(tests.test_text_box.SUBMIT_BUTTON_ID).click()
    py.getx(UPDATED_AGE_XPATH).should().have_text("1")


def test_new_record(py: Pylenium, url_nav):
    py.get(ADD_RECORD_ID).click()
    py.get(FIRST_NAME_ID).type("Bul")
    py.get(LAST_NAME_ID).type("Kathos")
    py.get(EMAIL_ID).type("theimmortalking@barbarian.com")
    py.get(AGE_ID).type("25")
    py.get(SALARY_ID).type("1000000000")
    py.get(DEPARTMENT_ID).type("SDET")
    py.get(tests.test_text_box.SUBMIT_BUTTON_ID).click()
    assert py.getx(NEW_TABLE_ENTRY_XPATH).get_attribute("textContent") == ("BulKathos25theimmortalking@barbarian"
                                                                           ".com1000000000SDET ")
