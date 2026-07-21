"""
Project 3: Enterprise Random Password Generator
DecodeLabs Python Programming — Industrial Training Kit

Architecture: Input -> Process -> Output
 - Input:   capture and validate a target password length
 - Process: build character pool, generate password with secrets + join()
 - Output:  display password and its calculated entropy
"""

import string
import secrets
import math

MIN_LENGTH = 15   # NIST SP 800-63-4: minimum length for high-security contexts
MAX_LENGTH = 64    # NIST SP 800-63-4: systems must support at least 64 chars


def get_password_length() -> int:
    """
    Phase 1: Input validation.
    Repeatedly prompts the user until a valid integer within the
    accepted NIST length range is provided. Prevents crashes from
    non-numeric input and prevents insecure (too-short) passwords.
    """
    while True:
        raw_value = input(
            f"Enter desired password length ({MIN_LENGTH}-{MAX_LENGTH} recommended): "
        ).strip()

        if not raw_value.isdigit():
            print("Invalid input. Please enter a whole number (e.g., 16).")
            continue

        length = int(raw_value)

        if length < MIN_LENGTH:
            print(f"Warning: {length} is below the NIST-recommended minimum "
                  f"of {MIN_LENGTH} characters for high-security contexts.")
            confirm = input("Use this length anyway? (y/n): ").strip().lower()
            if confirm != "y":
                continue

        if length > MAX_LENGTH:
            print(f"Length capped at maximum of {MAX_LENGTH} characters.")
            length = MAX_LENGTH

        return length


def get_character_pool(use_letters=True, use_digits=True, use_symbols=False) -> str:
    """
    Phase 2: Build the character pool using Python's string module
    instead of manually typed character arrays.
    """
    pool = ""
    if use_letters:
        pool += string.ascii_letters   # a-z, A-Z
    if use_digits:
        pool += string.digits          # 0-9
    if use_symbols:
        pool += string.punctuation     # !@#$%^&* etc.

    if not pool:
        raise ValueError("Character pool is empty. Enable at least one character type.")

    return pool


def generate_password(length: int, pool: str, require_digit=True, require_symbol=False) -> str:
    """
    Phase 2: Core generation logic.
    - Uses secrets.choice() instead of random.choice() for cryptographic
      security (hardware-level OS entropy, not the predictable Mersenne
      Twister used by the random module).
    - Uses a list + ''.join() accumulator instead of string += char,
      avoiding O(N^2) behavior caused by string immutability and
      achieving O(N) linear performance.
    """
    password_chars = [secrets.choice(pool) for _ in range(length)]

    # Optional: guarantee at least one digit / one symbol for extra strength
    if require_digit and not any(c in string.digits for c in password_chars):
        idx = secrets.randbelow(length)
        password_chars[idx] = secrets.choice(string.digits)

    if require_symbol and not any(c in string.punctuation for c in password_chars):
        idx = secrets.randbelow(length)
        password_chars[idx] = secrets.choice(string.punctuation)

    return "".join(password_chars)


def calculate_entropy(length: int, pool_size: int) -> float:
    """
    Phase 3: Mathematical verification.
    Entropy formula: E = L * log2(R)
      L = password length
      R = size of the character pool (range of possible characters)
    """
    return length * math.log2(pool_size)


def describe_strength(entropy_bits: float) -> str:
    """Give a human-readable strength rating based on entropy bits."""
    if entropy_bits < 40:
        return "Weak"
    elif entropy_bits < 60:
        return "Moderate"
    elif entropy_bits < 80:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=" * 55)
    print(" DecodeLabs — Enterprise Random Password Generator")
    print("=" * 55)

    # --- Phase 1: Input ---
    length = get_password_length()

    include_symbols = input("Include special characters (@, #, $, etc.)? (y/n): ")\
        .strip().lower() == "y"

    # --- Phase 2: Process ---
    pool = get_character_pool(use_letters=True, use_digits=True, use_symbols=include_symbols)
    password = generate_password(
        length=length,
        pool=pool,
        require_digit=True,
        require_symbol=include_symbols
    )

    # --- Phase 3: Output & Verification ---
    entropy = calculate_entropy(length, len(pool))
    strength = describe_strength(entropy)

    print("\n" + "-" * 55)
    print(f"Generated Password : {password}")
    print(f"Length              : {length} characters")
    print(f"Character Pool Size : {len(pool)} possible characters")
    print(f"Entropy             : {entropy:.2f} bits")
    print(f"Strength Rating     : {strength}")
    print("-" * 55)


if __name__ == "__main__":
    main()