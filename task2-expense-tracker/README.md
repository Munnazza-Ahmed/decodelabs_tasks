# DecodeLabs Expense Tracker

**Industrial Training Kit — Project 2 | Batch 2026**

A command-line Python script that continuously accepts expense amounts from a user, categorizes them, accumulates a running total, and saves a full session log to a text file.

---

## Overview

This project simulates a real-world backend engineering task: safely accepting continuous data input, validating it, processing it into a running state, and producing a reliable output. It follows the **Input → Process → Output (IPO)** model taught in Project 2 of the training kit.

## Features

- **Continuous input loop** — enter as many expenses as you like in one session
- **Category tagging** — every expense is tagged (Food, Travel, Shopping, Bills, Entertainment, Other)
- **Running total (Accumulator Pattern)** — `total += expense`, with state preserved outside the loop
- **Defensive coding** — invalid (non-numeric) input is caught and rejected without crashing the program
- **Sentinel-based exit** — type `quit` at any amount prompt to stop and see your results
- **Category breakdown** — final summary shows how much was spent per category
- **File logging** — every session automatically saves a timestamped `.txt` log with all transactions and totals

## Requirements

- Python 3.6 or later
- No external libraries required (uses only the built-in `datetime` module)

## How to Run

```bash
python expense_tracker.py
```

or, depending on your system:

```bash
python3 expense_tracker.py
```

## Usage

1. Run the script.
2. At the prompt, enter a numeric expense amount (e.g. `100`, `49.99`).
3. Choose a category from the numbered menu that appears.
4. Repeat steps 2–3 for as many expenses as you want to log.
5. Type `quit` at the amount prompt to stop.
6. The script displays:
   - Total number of transactions
   - Final total spent
   - A breakdown of spending by category
7. A log file is automatically saved in the same folder.

### Example Session

```
Enter expense amount (or 'quit' to stop): 100
  Categories:
    1. Food
    2. Travel
    3. Shopping
    4. Bills
    5. Entertainment
    6. Other
  Select category number: 1
  Added: 100.00 to Food  |  Running Total: 100.00

Enter expense amount (or 'quit' to stop): 50
  Select category number: 2
  Added: 50.00 to Travel  |  Running Total: 150.00

Enter expense amount (or 'quit' to stop): ten
  Invalid Data. Please enter a numeric value.

Enter expense amount (or 'quit' to stop): quit
==================================================
Transactions recorded : 2
FINAL TOTAL SPENT      : 150.00

Breakdown by category:
  Food           : 100.00
  Travel         : 50.00
==================================================

Log saved to: expense_log_20260721_073618.txt
```

## Output Log File

Each run creates a file named:

```
expense_log_YYYYMMDD_HHMMSS.txt
```

It contains:
- A timestamped list of every transaction (category, amount, time)
- A category-wise spending breakdown
- The final transaction count and total spent

## Project Structure

```
.
├── expense_tracker.py     # Main script
├── README.md               # This file
└── expense_log_*.txt       # Auto-generated session logs (created after each run)
```

## Concepts Demonstrated

| Concept | Where it appears |
|---|---|
| IPO Model (Input → Process → Output) | Overall script structure |
| Accumulator Pattern | `total += expense` |
| State preservation | `total`, `count`, `category_totals` initialized outside the loop |
| Defensive coding / Poka-Yoke | `try/except ValueError` on user input |
| Continuous loop control | `while True:` |
| Sentinel value / kill switch | `sentinel = "quit"` with `break` |
| Dictionaries for aggregation | `category_totals` |
| File I/O | `save_to_file()` |

## Quality Checklist

- [x] `total` initialized **outside** the loop
- [x] Catches `ValueError` on invalid input
- [x] Kill switch (`quit`) breaks the loop and prints the final total
- [x] Handles 5+ continuous transactions without errors
- [x] Logic (calculation) decoupled from output (display/file)

## Author

DecodeLabs Internship Program — Python Programming Track, Project 2
