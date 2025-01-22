# Project Title

A simple calculator that can sum numbers from a string with support for custom delimiters, and handles negative numbers with proper error handling.

## Description

This project implements a basic calculator that can take a string of numbers separated by commas, newlines, or custom delimiters. The calculator computes the sum of the numbers. It includes input validation to reject negative numbers, and it raises an error with a descriptive message listing the negative numbers encountered.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Dependencies

Before you begin, ensure you have the following prerequisites installed on your system:

- **Python 3.x**: Ensure Python is installed on your machine.
  - Download from [python.org](https://www.python.org/downloads/).
- **pip**: The Python package installer (usually comes with Python).
- **virtualenv**: Used to create isolated Python environments.
  - Install via pip: `pip install virtualenv`

**Operating System Requirements**:
- Windows, macOS, or Linux are supported.

### Installing

Follow these steps to get the project running on your machine.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Singh-Sg/incubyte-test/
    ```

2. **Create a Virtual Environment**:
    On macOS/Linux:
    ```bash
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment**:
    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```

4. **Install required dependencies** (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

### Executing the Program

To run the calculator program, follow these steps:

1. **Run the Python script**:
    ```bash
    python task_calculator.py
    ```

2. **Example Usage**:

    1. **For an empty input**:
        ```python
        print(add_num.calculate_sum(""))  # returns 0
        ```

    2. **For a basic input**:
        ```python
        print(add_num.calculate_sum("1,5"))  # returns 6
        ```

    3. **For newline-separated numbers**:
        ```python
        print(add_num.calculate_sum("1\n2,3"))  # returns 6
        ```

    4. **For a custom delimiter**:
        ```python
        print(add_num.calculate_sum("//;\n1;2"))  # returns 3
        ```

    5. **For invalid input (negative numbers)**:
        ```python
        try:
            print(add_num.calculate_sum("1,2,-3,4"))
        except ValueError as ex:
            print(ex)  # prints: negative numbers not allowed: -3
        ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
