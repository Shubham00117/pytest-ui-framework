import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config
from utils.logger import Logger
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, edge")
    parser.addoption("--env", action="store", default="qa", help="Environment to run tests on: dev, qa, prod")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    logger = Logger.get_logger(__name__)
    browser_name = request.config.getoption("--browser").lower()
    env_name = request.config.getoption("--env").lower()
    is_headless = request.config.getoption("--headless")
    
    logger.info(f"Setting up {browser_name} browser (Headless={is_headless}) for {env_name} environment...")
    
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        if is_headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise pytest.UsageError(f"--browser {browser_name} is not supported!")

    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)        
    
    # In a real industry project, you would map env_name to specific URLs
    # For now, we use the base URL from config
    driver.get(Config.BASE_URL)
    
    yield driver
    
    # Take screenshot on test failure
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
    
    logger.info("Tearing down browser...")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        setattr(item, "rep_call", report)


@pytest.fixture(scope="session")
def logger():
    return Logger.get_logger("TestFramework")
