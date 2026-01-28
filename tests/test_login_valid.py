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

    def test_negative_username(self, driver, logger):
        """Test login with invalid username"""
        logger.info("Starting negative username test")
        login_page = LoginPage(driver)
        
        login_page.login("incorrectUser", "Password123")
        
        assert login_page.is_visible(login_page.ERROR_MESSAGE), "Error message should be displayed"
        error_text = login_page.get_error_message()
        assert error_text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_text}'"
        logger.info("Negative username test passed")
