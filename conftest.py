import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config
from utils.logger import Logger


@pytest.fixture(scope="function")
def driver(request):
    logger = Logger.get_logger(__name__)
    logger.info("Setting up browser...")
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)        
    driver.get(Config.BASE_URL)
    
    yield driver
    
    # Take screenshot on test failure
    if request.node.rep_call.failed:
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
    
    logger.info("Tearing down browser...")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        item.rep_call = call
        yield


@pytest.fixture(scope="session")
def logger():
    return Logger.get_logger("TestFramework")
