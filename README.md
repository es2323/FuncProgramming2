# Functional Programming Projects: JSON Parser & Solar Data Pipeline

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Functional](https://img.shields.io/badge/Paradigm-Functional_Programming-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📂 Project Structure


## 1. 🧩 JSON Parser (`json_parser.py`)

### FP Concepts Demonstrated
```python
# Pure function example
def parse_json(data):
    return (
        {k: parse_json(v) for k, v in data.items()}  # Recursion + dict comprehension
        if isinstance(data, dict)
        else [parse_json(item) for item in data]      # Recursion + list comprehension
        if isinstance(data, list)
        else data                                     # Base case
    )

