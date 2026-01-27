import pytest
from pages.login_page import LoginPage
from utils.logger import Logger


class TestLoginValid:
    
    def test_valid_login(self, driver, logger):
        """Test successful login with valid credentials"""
        logger.info("Starting valid login test")
        login_page = LoginPage(driver)
        
        login_page.login("student", "Password123")
        assert login_page.is_login_successful(), "Login should succeed with valid credentials"
        logger.info("Valid login test passed")
