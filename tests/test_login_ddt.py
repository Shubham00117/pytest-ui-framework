import pytest
from pages.login_page import LoginPage
from utils.csv_reader import get_login_data
from utils.logger import Logger


class TestLoginDDT:
    
    @pytest.mark.regression
    @pytest.mark.parametrize("login_data", get_login_data())
    def test_login_ddt(self, driver, login_data, logger):
        """Test login functionality with data from CSV"""
        logger.info(f"Testing login with username: {login_data['username']}")
        login_page = LoginPage(driver)
        
        login_page.login(login_data['username'], login_data['password'])
        login_success = login_page.is_login_successful()
        
        expected_success = (login_data['username'] == 'student' and 
                           login_data['password'] == 'Password123')
        
        assert login_success == expected_success, f"Login result mismatch for {login_data['username']}"
        logger.info(f"Login test for {login_data['username']} completed")
