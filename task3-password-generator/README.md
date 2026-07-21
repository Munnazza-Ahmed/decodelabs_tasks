# 🔐 Enterprise Random Password Generator

A Python command-line tool that generates cryptographically secure, random passwords — built as **Project 3** of the DecodeLabs Python Programming Industrial Training Kit (Batch 2026).

This isn't just a "random characters" script. It's an exercise in **library integration, string manipulation, and applied security engineering**, following modern password-security standards.

---

## 📋 Features

- ✅ Interactive CLI prompts for password length
- ✅ Input validation (rejects non-numeric input, warns on insecure lengths)
- ✅ Enforces [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/) 2024 guidelines (15–64 character range)
- ✅ Uses `secrets.choice()` instead of `random.choice()` for cryptographic-grade randomness
- ✅ Character pool built from Python's `string` module (`ascii_letters`, `digits`, `punctuation`)
- ✅ Optional special-character inclusion
- ✅ Guarantees at least one digit (and one symbol, if enabled) in the output
- ✅ Efficient `O(N)` password construction using `''.join()` instead of `+=` in a loop
- ✅ Calculates and displays password **entropy** (bits of unpredictability)
- ✅ Strength rating (Weak → Very Strong)

---

## 🛠️ Tech Concepts Covered

| Concept | Why it matters |
|---|---|
| `secrets` module | Cryptographically secure randomness (vs. the predictable `random`/Mersenne Twister) |
| `string` module | Standardized, locale-independent character classification |
| String immutability | Understanding why `+=` in a loop is inefficient (`O(N²)`) |
| `.join()` pattern | Linear-time (`O(N)`) string construction |
| Information entropy | `E = L × log₂(R)` — measuring password strength mathematically |
| Input validation | Preventing crashes and insecure defaults |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher (for the `secrets` module)

### Installation

```bash
git clone https://github.com/<your-username>/enterprise-password-generator.git
cd enterprise-password-generator
```

No external dependencies — uses only the Python standard library.

### Usage

```bash
python3 password_generator.py
```

You'll be prompted for:
1. **Password length** (15–64 recommended; shorter lengths trigger a security warning)
2. **Whether to include special characters** (`@`, `#`, `$`, etc.)

### Example Output

```
=======================================================
 DecodeLabs — Enterprise Random Password Generator
=======================================================
Enter desired password length (15-64 recommended): 16
Include special characters (@, #, $, etc.)? (y/n): y

-------------------------------------------------------
Generated Password : NNbh{kiX<gAAg.=0
Length              : 16 characters
Character Pool Size : 94 possible characters
Entropy             : 104.87 bits
Strength Rating     : Very Strong
-------------------------------------------------------
```

---

## 📂 Project Structure

```
enterprise-password-generator/
├── password_generator.py   # Main script
└── README.md                # This file
```

---

## 🧠 How It Works

The script follows an **Input → Process → Output** architecture:

1. **Input** — Captures and validates the desired password length against NIST guidelines.
2. **Process** — Builds a character pool from the `string` module, then uses `secrets.choice()` in a list comprehension, joined with `.join()`, to generate the password securely and efficiently.
3. **Output** — Calculates the password's information entropy and reports a strength rating before displaying it.

---

## 🔮 Possible Extensions

- Add a `--no-repeat` flag to disallow repeated characters
- Support generating and copying multiple passwords at once (bulk mode)
- Add a `--exclude-ambiguous` option to skip characters like `l`, `1`, `O`, `0`
- Package as a CLI tool with `argparse` for non-interactive use
- Add unit tests for validation and entropy calculations

---

## 📄 License

This project is part of the DecodeLabs Industrial Training Kit and is intended for educational purposes.

---

