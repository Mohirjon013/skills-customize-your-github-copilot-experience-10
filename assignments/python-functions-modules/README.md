# 📘 Assignment: Python Functions and Modules

## 🎯 Objective

Learn how to organize Python programs with reusable functions and modules. Build a small utility program that separates calculations from the user-facing code.

## 📝 Tasks

### 🛠️ Create Reusable Functions

#### Description

Create functions that perform common temperature conversions. Each function should accept a value as an argument and return the converted result.

#### Requirements

Completed program should:

- Define `celsius_to_fahrenheit(celsius)` and `fahrenheit_to_celsius(fahrenheit)` functions
- Return numeric results instead of printing from the conversion functions
- Call both functions with sample values and display the results clearly

### 🛠️ Build a Utility Module

#### Description

Move the temperature conversion functions into a module named `temperature_utils.py`. Create a separate `main.py` file that imports the module and uses its functions.

#### Requirements

Completed program should:

- Store both conversion functions in `temperature_utils.py`
- Import and call the functions from `main.py`
- Keep user interaction and output in `main.py`
- Demonstrate at least two conversions with readable output

### 🛠️ Add a Function-Based Menu

#### Description

Extend `main.py` with a function-based menu that lets the user choose a conversion and enter a temperature.

#### Requirements

Completed program should:

- Use a function to display the menu
- Use a function to handle the selected conversion
- Handle an invalid menu choice with a helpful message
- Continue allowing conversions until the user chooses to quit
