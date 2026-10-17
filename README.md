# 🌤️ API Service Stub

A lightweight weather forecast service that provides weather data for supported cities through a simple API interface with authentication.

## 📝 Project Requirements & Tools

- **Python**: >= 3.12
- **Poetry**: Dependency management
- **pytest**: Testing framework (>= 9.1.1)
- **coverage**: Code coverage reporting (>= 7.16.2)
- **pre-commit**: Git hooks for code quality (>= 4.7.0)

## 🚀 Installation

1. Clone the repository and navigate to the project directory
2. Install dependencies using Poetry:

```bash
poetry install
```

Or using the exported requirements.txt:

```bash
pip install -r requirements.txt
```

3. Install pre-commit hooks:

```bash
pre-commit install
```

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
coverage run -m pytest
coverage report
```

For a detailed HTML coverage report:

```bash
coverage html
```

## 🏙️ Supported Cities & Expected Behavior

The service supports the following cities (case-insensitive):

- **Kigali**: Returns temperature 24.5°C, Sunny, 65% humidity
- **London**: Returns temperature 14°C, Rainy, 88% humidity
- **New York**: Returns temperature 19.2°C, Cloudy, 70% humidity

**Expected Behavior:**

- Valid API key (`super_secret_key`) is required for all requests
- Empty or whitespace-only city names are rejected
- Unsupported cities return a `CityNotFoundException`
- Invalid API keys return an `InvalidAPIKeyException`

## 🏗️ Architecture & Components

### Core Components

**`WeatherService`** (`app/service.py`)

- Main service class that coordinates weather data retrieval
- Validates API keys and city names
- Handles business logic and error management
- Logs warnings for invalid requests

**`MockWeatherProvider`** (`app/provider.py`)

- Implements the `WeatherProvider` interface
- Stores hardcoded weather data for supported cities
- Returns data or `None` based on city lookup

**`WeatherProvider`** (`app/interfaces.py`)

- Abstract base class defining the provider interface
- Enforces implementation of the `fetch()` method

**Custom Exceptions** (`app/exceptions.py`)

- `InvalidAPIKeyException`: Raised for invalid authentication
- `CityNotFoundException`: Raised for unsupported cities
- `EmptyCityNameException`: Raised for empty city inputs

## 🔄 Red-Green-Refactor Workflow

1. **Red**: Write a failing test that describes the desired behavior
2. **Green**: Write the minimal code to make the test pass
3. **Refactor**: Improve the code structure while keeping tests green

This TDD approach ensures testable, maintainable code with high confidence in changes.

## ✅ Coverage & Quality Checks

Generate coverage report:

```bash
coverage run -m pytest
coverage report -m
```

Run pre-commit hooks manually:

```bash
pre-commit run --all-files
```

The configured pre-commit hooks check for:

- Trailing whitespace
- End-of-file consistency
- YAML syntax validity
- Large file additions

## 🔀 Git Workflow Summary

1. Create a new branch for your feature or fix
2. Write tests following the Red-Green-Refactor cycle
3. Commit changes with clear, descriptive messages
4. Pre-commit hooks automatically run on each commit
5. Push your branch and create a pull request
6. Ensure all tests pass and coverage is maintained

---

**Author**: furahayves (yvesderricks@gmail.com)
