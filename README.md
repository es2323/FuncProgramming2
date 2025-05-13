# Functional Programming Projects: JSON Parser & Solar Data Pipeline

📜 Project Overview
Two Python scripts demonstrating core functional programming principles:

Recursive JSON Parser - Processes nested JSON structures immutably

Solar Data Pipeline - Analyzes photovoltaic system metrics using pure transformations

Built with Python 3.8+ following strict FP paradigms.

🔍 JSON Parser Features
Core Functionality
Depth-first parsing of arbitrarily nested JSON

Immutable transformations preserving original data

Type-safe processing for objects/arrays/primitives

FP Concepts Applied
✔ Pure functions with zero side effects
✔ Recursive tree traversal
✔ Higher-order function composition
✔ Persistent immutable data structures

Use Cases
Configuration file processing

API response normalization

Complex data structure analysis

☀️ Solar Data Pipeline Features
Core Functionality
ETL pipeline for photovoltaic metrics

Statistical aggregation of voltage/current/power

Temporal filtering by substation and date

FP Concepts Applied
✔ Map-Reduce transformations
✔ Point-free function composition
✔ Monadic error handling
✔ Declarative data flow

Use Cases
Renewable energy monitoring

Smart grid analytics

Power generation reporting

🧠 Key FP Principles
Principle	JSON Parser	Data Pipeline
Immutability	✅	✅
Recursion	✅	❌
Pure Functions	✅	✅
Function Composition	✅	✅
🛠 Technical Foundation
Libraries Used:

json (standard library)

functools.reduce

werkzeug.security for hashing

Runtime:

No external dependencies (pure Python)

Compatible with PyPy for performance
