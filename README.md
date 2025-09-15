# Matrix Calculator in Python

## Overview
This Python script is an interactive matrix calculator that allows users to create, store, and perform various matrix operations. It supports basic matrix arithmetic and algebra functions with an easy-to-use command-line menu interface.

## Features
- Add and store matrices with user-defined names and dimensions.
- Display all saved matrices.
- Compute matrix operations including:
  - Addition, subtraction, multiplication
  - Transpose
  - Trace (for square matrices)
  - Determinant (for square matrices)
  - Cofactor matrix
  - Adjoint matrix
  - Inverse matrix
- Validates matrix dimension compatibility for operations.
- Uses NumPy for determinant calculation to ensure accuracy.
- Handles user input interactively and continues until exit.

## Tutorial Video

For a detailed walkthrough of the matrix operations implemented in this project, including addition, subtraction, multiplication, trace, determinant, cofactor, adjoint, and inverse, watch the tutorial video below:

[🔢 Mastering Matrix Operations in Python: Flowcharts & Code Explained 🐍](https://youtu.be/JZhI3ohtJgg?si=1KqW7_tal70TjmS6)

This video provides step-by-step explanations of the code along with practical examples.

## Requirements
- Python 3.x
- NumPy library (`pip install numpy`)

## How to Use
1. Run the script in a Python environment.
2. Use the menu commands to:
   - Add new matrices (`am`)
   - Display saved matrices (`d`)
   - Calculate trace (`tr`)
   - Calculate determinant (`dt`)
   - Add matrices (`a`)
   - Subtract matrices (`sb`)
   - Multiply matrices (`m`)
   - Transpose (`t`)
   - Find cofactor matrix (`c`)
   - Find adjoint matrix (`ad`)
   - Find inverse matrix (`i`)
3. Follow prompts to enter matrix names and data.
4. Continue working with matrices until choosing to exit by entering 'N' at the continue prompt.

## Menu Commands Summary
| Command | Description                |
|---------|----------------------------|
| am      | Add a new matrix           |
| d       | Display all matrices       |
| tr      | Trace of a square matrix   |
| dt      | Determinant of a matrix    |
| a       | Add two matrices           |
| sb      | Subtract two matrices      |
| m       | Multiply two matrices      |
| t       | Transpose a matrix         |
| c       | Cofactor matrix of a matrix|
| ad      | Adjoint of a matrix        |
| i       | Inverse of a matrix        |

## Notes
- Trace, determinant, inverse, cofactor, and adjoint operations only work for square matrices.
- For matrix multiplication, the number of columns in the first matrix must equal the number of rows in the second.
- Data entries must be integers by default (can be adjusted for floats if needed).
- The script includes basic error handling with prompts for invalid inputs.

## License
This project is provided as-is for educational purposes.

---
