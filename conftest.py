import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', 
                 help="Choose language: fr, es, etc.")

@pytest.fixture(scope="function")
def language(request):
    language=str(request.config.getoption("language")  )
    return language


@pytest.fixture(scope="function")
def browser(request):   
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":                      
        print("\nstart chrome browser with for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()


