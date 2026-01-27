# Allure Reports

## Quick Commands

### Run Tests & Generate Report
```bash
# Clean previous results and run tests
pytest --alluredir=reports/allure-results --clean-alluredir

# Generate static report
allure generate reports/allure-results -o reports/allure-report --clean

# Open report in browser
open reports/allure-report/index.html
```

### One Command (Recommended)
```bash
pytest --alluredir=reports/allure-results --clean-alluredir && allure generate reports/allure-results -o reports/allure-report --clean && open reports/allure-report/index.html
```

### Live Server (Alternative)
```bash
# Run tests
pytest --alluredir=reports/allure-results

# Start live server
allure serve reports/allure-results
```

## What You Get
- Test results overview
- Individual test details
- Screenshots on failure
- Execution timeline
- Test parameters

## File Locations
- Test data: `reports/allure-results/`
- HTML report: `reports/allure-report/index.html`
