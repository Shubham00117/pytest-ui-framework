import pytest
import pytest_check as check
from pages.login_page import LoginPage
from utils.logger import Logger


class TestLoginValid:
    
    @pytest.mark.order(1)
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self, driver, logger):
        """Test successful login with valid credentials"""
        logger.info("Starting valid login test")
        login_page = LoginPage(driver)
        
        login_page.login("student", "Password123")
        
        # Industry Best Practice: Soft Assertions (Soft Checks)
        check.is_true(login_page.is_login_successful(), "Login success message not displayed")
        check.equal(login_page.get_title(), "Logged In Successfully | Practice Test Automation", "Page title mismatch")
        
        logger.info("Valid login test completed with soft assertions")

    @pytest.mark.order(2)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_negative_username(self, driver, logger):
        """Test login with invalid username"""
        logger.info("Starting negative username test")
        login_page = LoginPage(driver)
        
        login_page.login("incorrectUser", "Password123")
        
        assert login_page.is_visible(login_page.ERROR_MESSAGE), "Error message should be displayed"
        error_text = login_page.get_error_message()
        assert error_text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_text}'"
        logger.info("Negative username test passed")

    @pytest.mark.order(3)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_empty_credentials(self, driver, logger):
        """Test login with empty username and password"""
        logger.info("Starting empty credentials login test")
        login_page = LoginPage(driver)
        login_page.login("", "")
        assert login_page.is_visible(login_page.ERROR_MESSAGE), "Error message should be displayed for empty credentials"
        error_text = login_page.get_error_message()
        assert error_text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_text}'"
        logger.info("Empty credentials login test passed")

    @pytest.mark.order(4)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_empty_password(self, driver, logger):
        """Test login with empty password"""
        logger.info("Starting empty password login test")
        login_page = LoginPage(driver)
        login_page.login("student", "")
        assert login_page.is_visible(login_page.ERROR_MESSAGE), "Error message should be displayed for empty password"
        error_text = login_page.get_error_message()
        assert error_text == "Your password is invalid!", f"Expected 'Your password is invalid!', but got '{error_text}'"
        logger.info("Empty password login test passed")

    @pytest.mark.order(5)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_empty_username(self, driver, logger):
        """Test login with empty username"""
        logger.info("Starting empty username login test")
        login_page = LoginPage(driver)
        login_page.login("", "Password123")
        assert login_page.is_visible(login_page.ERROR_MESSAGE), "Error message should be displayed for empty username"
        error_text = login_page.get_error_message()
        assert error_text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_text}'"
        logger.info("Empty username login test passed")
