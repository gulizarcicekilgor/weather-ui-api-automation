# 🌤️ Weather Automation Test Project

Automated testing project for [OpenWeatherMap](https://openweathermap.org/) using Python, Playwright, and pytest.

---

## 🎯 Project Goals

- Learn Playwright from scratch
- Apply Page Object Model (POM) design pattern
- Combine UI and API testing
- Generate test reports with Allure
- Run tests automatically with GitHub Actions (CI/CD)

---

## ✅ Tasks

- [ ] Project setup (Playwright, pytest, Allure)
- [ ] Folder structure (tests, pages, utils)
- [ ] conftest.py — browser & page fixtures
- [ ] Homepage load test
- [ ] Search city test
- [ ] Verify weather data on UI (temperature, humidity, wind)
- [ ] Page Object Model — WeatherPage class
- [ ] OpenWeatherMap API tests
- [ ] Compare UI data vs API data
- [ ] Allure reporting
- [ ] GitHub Actions CI/CD pipeline

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Programming language |
| Playwright | Browser automation |
| pytest | Test framework |
| Allure | Test reporting |
| GitHub Actions | CI/CD |


## 📁 Project Structure

```
weather-automation/
├── tests/        # Test files
├── pages/        # Page Object Model classes
├── utils/        # Helper functions
├── conftest.py   # Fixtures
└── README.md
```

## 🚀 How to Run

```bash
# Install dependencies
pip install pytest playwright pytest-playwright allure-pytest
playwright install

# Run tests
pytest tests/ -v
```