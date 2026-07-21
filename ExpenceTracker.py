"""
DecodeLabs - Python Programming (Industrial Training Kit)
Project 2: Expense Tracker (Enhanced Version)
-----------------------------------------------------------
Goal: Continuously accept expense amounts + categories from
the user, accumulate them into a running total, break the
total down by category, and save a full log to a text file.

Key concepts demonstrated:
  - Accumulator pattern (total = total + new_expense)
  - Input validation / defensive coding (try/except)
  - Sentinel value to gracefully exit the loop
  - Dictionaries for category-wise accumulation
  - File I/O to persist the session log
  - Separation of processing (logic) from output (display)
"""

from datetime import datetime

CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]


def choose_category():
    """Let the user pick a category from a numbered menu."""
    print("  Categories:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"    {i}. {cat}")

    while True:
        choice = input("  Select category number: ").strip()
        try:
            index = int(choice)
            if 1 <= index <= len(CATEGORIES):
                return CATEGORIES[index - 1]
            else:
                print(f"  Please enter a number between 1 and {len(CATEGORIES)}.")
        except ValueError:
            print("  Invalid input. Please enter a number.")


def main():
    # PHASE: Initialization (State lives OUTSIDE the loop)
    total = 0.0
    count = 0
    sentinel = "quit"
    category_totals = {cat: 0.0 for cat in CATEGORIES}
    transactions = []  # list of (category, amount, timestamp) tuples

    print("=" * 50)
    print("   DECODELABS EXPENSE TRACKER (with Categories)")
    print("=" * 50)
    print(f"Enter an expense amount, or type '{sentinel}' to stop.")
    print(f"(Tip: type '{sentinel}' at any amount prompt to finish and see your total.)\n")

    # PHASE: The Logic Skeleton (Continuous Audit Loop)
    while True:
        user_input = input(f"Enter expense amount (or '{sentinel}' to stop): ").strip()

        # Sentinel path -> graceful shutdown / kill switch
        if user_input.lower() == sentinel:
            break

        # PHASE 1: The Gatekeeper (Defensive Coding / Poka-Yoke)
        try:
            expense = float(user_input)
        except ValueError:
            print("  Invalid Data. Please enter a numeric value.\n")
            continue

        if expense < 0:
            print("  Expense cannot be negative. Try again.\n")
            continue

        # Ask for category
        category = choose_category()

        # PHASE: The Accumulator Pattern (Heartbeat of the Ledger)
        total += expense
        count += 1
        category_totals[category] += expense
        transactions.append((category, expense, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        print(f"  Added: {expense:.2f} to {category}  |  Running Total: {total:.2f}\n")

    # PHASE 3: Output (Decoupling Logic from Display)
    print("=" * 50)
    if count == 0:
        print("No expenses were recorded.")
    else:
        print(f"Transactions recorded : {count}")
        print(f"FINAL TOTAL SPENT      : {total:.2f}\n")
        print("Breakdown by category:")
        for cat, amt in category_totals.items():
            if amt > 0:
                print(f"  {cat:<15}: {amt:.2f}")
    print("=" * 50)

    # Save log to file
    if count > 0:
        save_to_file(transactions, category_totals, total, count)


def save_to_file(transactions, category_totals, total, count):
    """Persist the session's transactions and summary to a text file."""
    filename = f"expense_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        with open(filename, "w") as f:
            f.write("DECODELABS EXPENSE TRACKER - SESSION LOG\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("TRANSACTIONS:\n")
            f.write("-" * 50 + "\n")
            for category, amount, timestamp in transactions:
                f.write(f"[{timestamp}]  {category:<15}  {amount:>10.2f}\n")

            f.write("-" * 50 + "\n\n")
            f.write("CATEGORY BREAKDOWN:\n")
            for cat, amt in category_totals.items():
                if amt > 0:
                    f.write(f"  {cat:<15}: {amt:.2f}\n")

            f.write("\n" + "=" * 50 + "\n")
            f.write(f"Total Transactions : {count}\n")
            f.write(f"FINAL TOTAL SPENT   : {total:.2f}\n")
            f.write("=" * 50 + "\n")

        print(f"\nLog saved to: {filename}")

    except IOError as e:
        print(f"\nCould not save log file: {e}")


if __name__ == "__main__":
    main()