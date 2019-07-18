import time
import pytest
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_button_add_to_basket(browser):
    browser.get(link)
    browser.find_element_by_css_selector("[id=language_selector]>.btn").click()

#Удалите знак комментария в следующей строке для запуска с --language=fr
#    time.sleep(30)

    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        pytest.fail("There is no such element")
