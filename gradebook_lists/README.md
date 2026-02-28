# Gradebook Lists Project

A Python learning project demonstrating list manipulation and operations using a student gradebook system.

## File

- `gradebook_lists.py` — Python script showcasing list operations and data management.

## Overview

This project demonstrates fundamental Python list operations through a practical gradebook management example. It shows how to create, modify, combine, and manipulate nested lists (lists of lists).

## Features

### Data Structures
- **Nested Lists**: Uses lists containing subject names and corresponding grades.
- **Multiple Gradebooks**: Combines previous semester data with current semester data.

### Operations Demonstrated

1. **Creating Lists**
   - Simple lists: `subjects`, `grades`
   - Nested lists: `gradebook` with [subject, grade] pairs

2. **Appending Data**
   ```python
   gradebook.append(["computer science", 100])
   gradebook.append(["visual arts", 93])
   ```
   - Adds new subject-grade entries to the gradebook.

3. **Modifying Data**
   ```python
   gradebook[-1][-1] = 93 + 5
   ```
   - Uses negative indexing to access and modify the last grade.

4. **Removing Data**
   ```python
   gradebook[2].remove(85)
   ```
   - Removes a grade value from a specific subject entry.

5. **Adding Results**
   ```python
   gradebook[2].append("Pass")
   ```
   - Appends a pass/fail status to a gradebook entry.

6. **Combining Lists**
   ```python
   full_gradebook = last_semester_gradebook + gradebook
   ```
   - Merges two gradebooks using the `+` operator.

## Running the Script

```bash
python gradebook_lists.py
```

### Expected Output

The script prints the combined gradebook containing both last semester's and current semester's grades with modifications.

## Code Breakdown

| Operation | Line | Purpose |
|-----------|------|---------|
| `append()` | 9-10 | Add new subject-grade entries |
| Indexing & assignment | 13 | Modify a grade value |
| `remove()` | 16 | Remove an item from a nested list |
| `append()` | 19 | Add metadata (pass/fail status) |
| List concatenation | 22 | Combine two separate lists |

## Learning Concepts

- **List Indexing**: Accessing elements using positive and negative indices
- **Nested Lists**: Working with lists containing other lists
- **List Methods**: `append()`, `remove()`
- **List Operators**: Concatenation with `+`
- **Mutability**: Modifying list contents in place

## Possible Enhancements

- Add a GPA calculation function
- Implement grade-to-letter conversion (A, B, C, etc.)
- Add error handling for invalid grades
- Create a class-based gradebook system
- Export gradebook to CSV or JSON
- Add functions to filter by subject or grade range
- Implement grade statistics (average, min, max)

## Requirements

- Python 3.6 or higher

## License

This is a learning project. No license specified.
