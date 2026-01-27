import os


class Config:
    # Base URL
    BASE_URL = "https://practicetestautomation.com/practice-test-login/"
    
    # Browser settings
    BROWSER = "chrome"
    HEADLESS = False
    IMPLICIT_WAIT = 10
    
    # Test data paths
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
    
    # Credentials
    VALID_USERNAME = "student"
    VALID_PASSWORD = "Password123"
