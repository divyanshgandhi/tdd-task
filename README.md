# String Calculator TDD Kata - Python Implementation

A Test-Driven Development implementation of the String Calculator kata for Incubyte's TDD Assessment.

## 🎯 Assessment Objective

This project demonstrates mastery of:
- **Test-Driven Development (TDD)** with Red-Green-Refactor cycle
- **Clean Code** principles and Python best practices
- **pytest** testing framework
- **Git workflow** with frequent, meaningful commits

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- pip

### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd tdd-task

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run tests with coverage
pytest --cov=src

# Watch mode for continuous testing
ptw --runner "pytest --tb=short"
```

## 📋 Requirements Implementation

### ✅ Step 0: Repo Setup
- [x] Setting up repo for python 
- [x] Create empty implementation
- [x] Setup tests for `StringCalculator`

### ✅ Step 1: Basic String Calculator
- [x] Empty string returns 0
- [x] Single number returns that number
- [x] Two comma-separated numbers return their sum

### ✅ Step 2: Handle Any Amount of Numbers
- [x] Support unlimited comma-separated numbers

### Step 3: Handle New Lines
- [ ] Support new lines between numbers: `"1\n2,3"` → `6`

### Step 4: Support Different Delimiters
- [ ] Custom delimiter format: `"//[delimiter]\n[numbers...]"`
- [ ] Example: `"//;\n1;2"` → `3`

### Step 5: Negative Numbers
- [ ] Throw exception for negative numbers
- [ ] Show all negatives in exception message

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_string_calculator.py::TestStringCalculator::test_empty_string_returns_zero -v

# Run with detailed output
pytest -v

# Run with coverage report
pytest --cov=src --cov-report=html
```

## 🔄 TDD Process

Each feature follows the TDD cycle:

1. **🔴 RED**: Write a failing test
2. **🟢 GREEN**: Write minimal code to pass
3. **🔵 REFACTOR**: Improve code while keeping tests green
4. **📝 COMMIT**: Save progress with descriptive message

## 📁 Project Structure

```
tdd-task/
├── src/
│   └── string_calculator.py
├── tests/
│   └── test_string_calculator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎓 Key Learning Outcomes

- **TDD Discipline**: Red-Green-Refactor cycle
- **Clean Testing**: Readable, maintainable test cases
- **Python Idioms**: Leveraging Python's strengths
- **Git Best Practices**: Frequent, meaningful commits

## 📊 Test Coverage

Maintaining 100% test coverage throughout development.

---

*This project is part of the Incubyte TDD Assessment demonstrating software craftsmanship principles.*