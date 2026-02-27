# Manythings - Multi-Purpose Python Calculator & String Tool

A beginner-friendly Python program that performs basic math operations, prime number checking, and string manipulations through an interactive menu-driven interface.

## File

- `Manythings.py` — Main Python script with interactive menu system.

## Overview

This is a learning project demonstrating fundamental Python concepts including:
- Arithmetic operations
- Number theory (prime number checking)
- String manipulation
- Conditional logic (if/elif/else)
- Loops (while, for)
- User input handling

## Features

### 1. **Arithmetic Operations**
   - **Addition** - Add two numbers
   - **Subtraction** - Subtract two numbers
   - **Multiplication** - Multiply two numbers
   - **Division** - Divide two numbers
   - **Modulus** - Find remainder after division

### 2. **Prime Number Checker**
   - Determines if a given number is prime or not
   - Uses efficient algorithm: checks divisibility up to √n
   - Handles edge cases (numbers ≤ 1 are not prime)

### 3. **String Operations**
   - **Concatenation** - Join two strings together
   - **Reverse** - Reverse the characters in a string
   - **Length** - Count the number of characters in a string

## Running the Program

```bash
python Manythings.py
```

## How to Use

1. **Run the script** - The menu will appear in your terminal
2. **Select an option** - Enter a number (1-10) based on what you want to do
3. **Provide input** - Enter the required numbers or strings
4. **View results** - The program displays the result
5. **Repeat or exit** - Select another option or choose 10 to exit

### Example Walkthrough

```
Menu:
1. Addition
2. Subtraction
3. Multiplication
4. Divide
5. Modulus
6. Check prime number or not!
7. String Concatenation
8. String Reverse
9. String Length
10. Exit

Enter your choice: 1
Enter first number: 5
Enter second number: 3
1. Sum = 8
```

## Menu Options

| Option | Operation | Example |
|--------|-----------|---------|
| 1 | Addition | 5 + 3 = 8 |
| 2 | Subtraction | 10 - 4 = 6 |
| 3 | Multiplication | 6 * 7 = 42 |
| 4 | Division | 15 / 3 = 5.0 |
| 5 | Modulus | 17 % 5 = 2 |
| 6 | Prime Check | Is 7 prime? Yes |
| 7 | String Concatenation | "Hello" + "World" = "HelloWorld" |
| 8 | String Reverse | "Python" → "nohtyP" |
| 9 | String Length | "Code" has 4 characters |
| 10 | Exit | Terminates the program |

## Code Highlights

### Prime Number Algorithm
```python
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")
```
- Checks divisibility only up to the square root of the number
- Uses while-for-else loop structure

### String Reverse
```python
reversed_string = string[::-1]
```
- Uses Python's slice notation with step -1 to reverse

### Menu Loop
```python
while True:
    # Menu display
    # User input and processing
```
- Infinite loop that continues until user selects exit (option 10)

## Learning Concepts

- **Conditional Statements** - if/elif/else for decision making
- **Loops** - while and for loops for repetition
- **Functions** - Mathematical and string operations
- **Input/Output** - Taking user input and displaying results
- **String Slicing** - Using [::-1] for reversal
- **Integer Operations** - Arithmetic and modulus operations
- **Number Theory** - Prime number checking algorithm

## Requirements

- Python 3.6 or higher

## Possible Enhancements

- Add power/exponent operation
- Add square root calculation
- Add factorial calculation
- Input validation and error handling
- Add more string operations (uppercase, lowercase, reverse words)
- Create functions to reduce code repetition
- Add a simple calculator history feature
- Implement a graphical user interface (GUI) using tkinter
- Add temperature conversion
- Add percentage calculation

## Notes

- The program uses an infinite `while True` loop that runs until option 10 is selected
- Currently commented out input prompts can be uncommented for testing
- Input validation could be improved for robustness

## License

This is a learning project. No license specified.
