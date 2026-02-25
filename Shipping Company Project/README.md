# Sal's Shipping Company - Shipping Cost Calculator

A Python program that calculates shipping costs for different delivery methods and recommends the cheapest option based on package weight.

## File

- `Shipping Company Project-2.py` — Main Python script for shipping cost calculation.

## Overview

This project demonstrates practical Python concepts including:
- Functions and return statements
- Conditional logic (if/elif/else)
- Comparison operators
- The `min()` built-in function
- Real-world problem solving (cost optimization)

## Features

- **Ground Shipping** - Standard shipping with weight-based pricing tiers
- **Ground Shipping Premium** - Flat-rate premium option ($125.00)
- **Drone Shipping** - Express drone delivery with weight-based pricing
- **Cost Comparison** - Automatically determines the cheapest shipping method
- **Weight-based Pricing** - Different rates based on package weight

## Running the Program

```bash
python "Shipping Company Project-2.py"
```

### Example Output

For a 41.5 lb package:
```
Ground Shipping $ 217.625
Ground Shipping Premium $ 125.0
Drone Shipping $ 591.375
Cheapest method is Ground Shipping Premium: $ 125.0
```

## Shipping Methods & Pricing

### Ground Shipping

Weight-based pricing with $20 flat fee:

| Weight Range | Rate per lb | Formula |
|--------------|-------------|---------|
| ≤ 2 lbs | $1.50 | weight × $1.50 + $20 |
| 2 < weight ≤ 6 lbs | $3.00 | weight × $3.00 + $20 |
| 6 < weight ≤ 10 lbs | $4.00 | weight × $4.00 + $20 |
| > 10 lbs | $4.75 | weight × $4.75 + $20 |

**Example**: 5 lb package = (5 × $3.00) + $20 = $35.00

### Ground Shipping Premium

Flat-rate option:
- **Cost**: $125.00 (regardless of weight)
- **Best for**: Heavier packages

### Drone Shipping

Weight-based pricing (no flat fee):

| Weight Range | Rate per lb |
|--------------|-------------|
| ≤ 2 lbs | $4.50/lb |
| 2 < weight ≤ 6 lbs | $9.00/lb |
| 6 < weight ≤ 10 lbs | $12.00/lb |
| > 10 lbs | $14.25/lb |

**Example**: 5 lb package = 5 × $9.00 = $45.00

## Code Structure

### Ground Shipping Function
```python
def calculate_ground_shipping(weight):
    if weight <= 2:
        return weight * 1.5 + 20
    elif weight <= 6:
        return weight * 3.0 + 20
    elif weight <= 10:
        return weight * 4.0 + 20
    else:
        return weight * 4.75 + 20
```
- Uses conditional logic to apply correct rate
- Returns calculated cost
- Includes $20 flat handling fee

### Drone Shipping Calculation
```python
if weight <= 2:
    cost_drone = weight * 4.50
elif weight <= 6:
    cost_drone = weight * 9.00
elif weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25
```
- Implements pricing tiers directly in conditional statements
- No function wrapper (could be refactored)

### Cost Comparison
```python
cheapest_method = min(cost_ground, cost_ground_premium, cost_drone)

if cheapest_method == cost_ground:
    # Show Ground Shipping as cheapest
elif cheapest_method == cost_ground_premium:
    # Show Premium as cheapest
else:
    # Show Drone as cheapest
```
- Uses `min()` to find the lowest cost
- Uses conditional logic to identify and display the cheapest option

## Learning Concepts

- **Functions** - Define `calculate_ground_shipping()` function with parameters and return values
- **Conditionals** - if/elif/else for different weight tiers
- **Comparison Operators** - Using `<=` for weight ranges
- **Built-in Functions** - `min()` for finding minimum value
- **Logic Flow** - Nested conditionals for complex decision making
- **Variables** - Storing calculated costs
- **Comments** - Documenting code sections

## Usage

To use this program with different weights:

1. Modify the `weight` variable at the top:
   ```python
   weight = 41.5  # Change this value
   ```

2. Run the program to see all three shipping costs and the cheapest option

### Weight Examples

- **Light package** (1 lb): Ground Shipping Premium likely cheapest
- **Medium package** (5 lb): Compare all options needed
- **Heavy package** (50 lb): Ground Shipping Premium usually best

## Interactive Version

To make this accept user input:

```python
weight = float(input("Enter package weight (lbs): "))

# Rest of program continues...
```

## Possible Enhancements

- **User Input** - Accept weight from user input
- **Refactoring** - Create a `calculate_drone_shipping()` function too
- **Loop Support** - Process multiple packages in a loop
- **Delivery Estimation** - Add estimated delivery times
- **Tax Calculation** - Add state/local taxes to final cost
- **Discount Options** - Implement bulk discounts
- **Package Validation** - Add weight limits and error handling
- **File I/O** - Save shipping quotes to a file
- **GUI Interface** - Create a graphical interface using tkinter
- **Multi-weight Packages** - Handle partial weights or rounded-up weights
- **Surcharge Fees** - Add fuel surcharges or weather fees
- **Rate Updates** - Read rates from a configuration file

## Refactoring Example

The code could be made more maintainable by creating a function for drone shipping:

```python
def calculate_drone_shipping(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight <= 6:
        return weight * 9.00
    elif weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25

cost_drone = calculate_drone_shipping(weight)
```

Or using a more elegant approach with weight tier dictionaries:

```python
def calculate_shipping(weight, rates):
    for max_weight, rate in sorted(rates.items()):
        if weight <= max_weight:
            return weight * rate + 20
    return weight * rates[max(rates.keys())] + 20
```

## Real-World Application

This type of calculation is used by:
- E-commerce platforms (Amazon, eBay, etc.)
- Shipping companies (FedEx, UPS, DHL, etc.)
- Logistics providers
- Warehouse management systems

## Requirements

- Python 3.6 or higher
- No external dependencies

## Notes

- Current implementation uses a fixed weight (41.5 lbs) - ideal for learning
- No input validation (could add error handling)
- Prices are simplified for educational purposes
- Real shipping includes additional factors (distance, service level, etc.)

## License

This is a learning project. No license specified.
