# TOPSIS Utility: A Decision-Making Tool

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)

A Python package to calculate **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** scores for multi-criteria decision-making problems.

---

## Installation

Install via pip:

```bash
pip install topsis-utility-102203540
```

---

## Usage

Run the tool using the command-line interface:

```bash
topsis_tool <input_file> <weights> <impacts> <output_file>
```

### Parameters:
- `<input_file>`: Path to the CSV file containing data.
- `<weights>`: Comma-separated weights of criteria (e.g., `1,2,3`).
- `<impacts>`: Comma-separated impacts of criteria (`+` for benefit, `-` for cost).
- `<output_file>`: Path to save the output CSV file.

---

## Dependencies

- `pandas` >= 1.1.5  
- `numpy` >= 1.19.0  

These dependencies are automatically installed with the package.

## How It Works

1. **Normalize the Dataset**: Each value is divided by the column's square root of sum of squares.  
2. **Apply Weights**: Multiply the normalized data by user-provided weights.  
3. **Determine Ideal Solutions**:
   - Positive Ideal Solution: Maximum value for benefit criteria, minimum for cost.
   - Negative Ideal Solution: Minimum value for benefit criteria, maximum for cost.
4. **Compute Distances**:
   - Distance to Positive Ideal Solution (D+).
   - Distance to Negative Ideal Solution (D-).
5. **Calculate TOPSIS Score**:
   - Relative Closeness to Ideal Solution = D- / (D+ + D-).  
6. **Rank Alternatives**: Higher scores are ranked higher.

---

