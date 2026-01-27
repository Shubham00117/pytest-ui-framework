# Pytest UI Framework

A robust UI automation framework built with Pytest and Selenium.

## Project Structure

```
pytest-ui-framework/
│
├── pages/              # Page Objects
│   └── login_page.py
│
├── tests/              # Test cases
│   └── test_login.py
│
├── utils/              # Helpers (wait, logger, config)
│   └── wait_utils.py
│
├── reports/            # Generated reports
│
├── conftest.py         # Fixtures (browser, setup)
├── pytest.ini          # PyTest config
├── requirements.txt
└── README.md
```

## Setup

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Basic Test Run
```bash
pytest
```

### Run with specific markers
```bash
pytest -m smoke
pytest -m login
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Generate Allure Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Run in Headless Mode
```bash
pytest -v --browser=headless
```

## Page Object Model

The framework uses the Page Object Model pattern for better maintainability:

- **pages/**: Contains page object classes
- **tests/**: Contains test cases using page objects
- **utils/**: Contains utility classes and helpers

## Configuration

### pytest.ini
Main configuration file containing:
- Test discovery patterns
- Default command line options
- Custom markers
- Logging configuration

### conftest.py
Contains shared fixtures:
- `browser`: Regular Chrome browser fixture
- `browser_headless`: Headless Chrome fixture
- Automatic screenshot capture on failure

## Features

- ✅ Page Object Model architecture
- ✅ Automatic screenshot capture on test failure
- ✅ HTML test reports
- ✅ Allure reporting integration
- ✅ Custom wait utilities
- ✅ Headless browser support
- ✅ Test markers for categorization
- ✅ Detailed logging

## Writing New Tests

1. Create page objects in `pages/` directory
2. Write test cases in `tests/` directory
3. Use the `browser` fixture in your test functions
4. Follow naming conventions: `test_*.py`

Example:
```python
def test_example(browser):
    page = LoginPage(browser)
    page.load()
    # Your test logic here
    assert True
```

## Reports

- **HTML Reports**: Generated in `reports/report.html`
- **Allure Reports**: Generated in `reports/allure-results/`
- **Screenshots**: Saved automatically on test failure

## Troubleshooting

1. **WebDriver Issues**: Ensure Chrome browser is installed
2. **Permission Issues**: Check if reports directory has write permissions
3. **Timeout Issues**: Adjust wait timeouts in `conftest.py` or page objects
