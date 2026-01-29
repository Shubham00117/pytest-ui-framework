# Professional Pytest UI Automation Framework

A state-of-the-art UI automation framework built with Pytest and Selenium, following industry-standard design patterns and best practices.

## 🚀 Key Features

- **Page Object Model (POM)**: Enhanced maintainability and modularity.
- **Parallel Execution**: Powered by `pytest-xdist` for high-speed test runs.
- **Flaky Test Resilience**: Automatic reruns using `pytest-rerunfailures`.
- **Soft Assertions**: Integrated `pytest-check` for comprehensive validation.
- **Dynamic Configuration**: Support for multiple browsers and environments via command line.
- **Rich Reporting**: Allure Results, Self-contained HTML reports, and automated screenshots on failure.
- **Headless Support**: Seamless CI/CD integration with headless browser options.
- **Structured Suites**: Industry-standard categorization (Smoke, Sanity, Regression).

---

## 🏗️ Project Structure

```text
pytest-ui-framework/
├── base/               # Base classes for reusable logic
│   └── base_page.py    # Common Selenium wrappers
├── pages/              # Page Object classes
│   └── login_page.py
├── tests/              # Test suites
│   ├── test_login_valid.py
│   └── test_login_ddt.py (Data Driven)
├── data/               # Test data (CSV, JSON, etc.)
│   └── login_data.csv
├── utils/              # Logs, Helpers, Readers
│   ├── logger.py
│   └── csv_reader.py
├── reports/            # Test execution artifacts
│   ├── allure-results/
│   └── screenshots/    # Failure captures
├── config/             # Framework level settings
├── conftest.py         # Global hooks and fixtures
└── pytest.ini          # Pytest configuration & markers
```

---

## 🛠️ Setup & Installation

1. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate  # macOS/Linux
   # or
   .\venv\Scripts\activate   # Windows
   ```

2. **Install Industry-standard Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Execution Commands

### 🎯 Running Test Suites (Markers)
| Suite | Command |
| :--- | :--- |
| **Smoke** | `pytest -m smoke` |
| **Sanity** | `pytest -m sanity` |
| **Regression** | `pytest -m regression` |

### 🌐 Cross-Browser Testing
```bash
pytest --browser firefox
pytest --browser edge
pytest --browser chrome  # Default
```

### ⚡ Parallel & Headless Execution
```bash
# Run in parallel across all CPU cores in headless mode
pytest --headless -n auto
```

### 🌍 Environment Switching
```bash
pytest --env prod
pytest --env qa    # Default
```

### 📊 Reporting
- **HTML Report**: Automatically generated at `reports/report.html` after every run.
- **Allure Report**:
  ```bash
  # Step 1: Run tests with Allure
  pytest --alluredir=reports/allure-results
  
  # Step 2: Serve the report
  allure serve reports/allure-results
  ```

---

## 🧠 Best Practices Implemented

### 1. Soft Assertions (checks)
Instead of hard `asserts` which stop execution immediately, we use `check`:
```python
import pytest_check as check

def test_example(driver):
    check.is_true(page.is_success(), "Success message missing")
    check.equal(driver.title, "Expected", "Title mismatch")
    # Test continues even if checks fail!
```

### 2. Test Ordering
Tests are ordered to follow logical workflows using `@pytest.mark.order(n)`.

### 3. Automated Error Recovery
Failed UI tests are automatically rerun once to eliminate false negatives caused by network latency or transients.

### 4. Failure Screenshots
The framework automatically captures and attaches screenshots to Allure reports when a test fails, helping in instant debugging.
