import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from utilities.readProperties import ReadConfig


# Setting default browser as Chrome in case user does not specify the browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on (chrome or firefox)")

# Fetching the browser and launching the application, maximize the window as setup mechanism.
@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    print("\n--- Setup: Launching browser ---")
    driver.get(ReadConfig.getApplicationURL())
    driver.maximize_window()
    yield driver
    print("--- Teardown: Closing browser ---")
    driver.quit()

########## For pytest html reports #########
#hook for adding new environment info in the html report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'Project 1 - EdTech Platform Web Application'
    config.stash[metadata_key]['Module'] = 'GUVI Website'
    config.stash[metadata_key]['Tester Name'] = 'Ramya V'

#hook for delete/modify environment info in the html report
pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)