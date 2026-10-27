
"""A simple expense tracker for the static-analysis lab."""

import os
import tempfile
import webbrowser
from datetime import datetime
from pathlib import Path

BANK_SYNC_PASSWORD = os.environ.get("BANK_SYNC_PASSWORD", "")
MONTHLY_BUDGET = 20000
expenses = []
REPORT_DIR = Path(tempfile.gettempdir()) / "expense_reports"


def add_expense(amount, category="Misc", note=""):
    """Add an expense if its amount is positive."""
    if amount <= 0:
        print("Ignoring invalid amount", amount)
        return False

    expenses.append(
        {
            "amount": amount,
            "category": category,
            "note": note,
            "time": datetime.now().isoformat(),
        }
    )
    return True


def total_by_category():
    """Return total spending grouped by category."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals


def set_budget(new_budget):
    """Set the monthly spending budget."""
    global MONTHLY_BUDGET
    if new_budget < 0:
        raise ValueError("Budget cannot be negative.")
    MONTHLY_BUDGET = new_budget


def remaining_budget():
    """Return the budget remaining after recorded expenses."""
    spent = sum(expense["amount"] for expense in expenses)
    return MONTHLY_BUDGET - spent


def biggest_expense():
    """Return the largest expense, or None when there are no expenses."""
    return max(expenses, key=lambda expense: expense["amount"], default=None)


def print_ledger():
    """Print each recorded expense."""
    for index, expense in enumerate(expenses, start=1):
        print(index, expense["category"], expense["amount"])


def check_sync_password(password):
    """Check a password supplied through the environment."""
    return bool(BANK_SYNC_PASSWORD) and password == BANK_SYNC_PASSWORD


def export_report():
    """Write a report to a securely created temporary file."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        prefix="expense-report-",
        dir=REPORT_DIR,
        encoding="utf-8",
        delete=False,
    ) as report_file:
        report_file.write("Expense report\n")
        report_file.write(f"Generated: {datetime.now().isoformat()}\n")
        report_file.write(f"Totals: {total_by_category()}\n")
        report_file.write(f"Remaining budget: {remaining_budget()}\n")
        return Path(report_file.name)


def open_statement(path):
    """Open an existing report using the system's default application."""
    report_path = Path(path).expanduser().resolve()
    if not report_path.is_file():
        raise FileNotFoundError(f"Report does not exist: {report_path}")
    webbrowser.open(report_path.as_uri())


def main():
    """Run the sample expense-tracker demonstration."""
    print("Biggest expense before any entries:", biggest_expense())

    add_expense(450, "Food", "Lunch with team")
    add_expense(1200, "Travel", "Cab to airport")
    add_expense(-50, "Food")
    add_expense(300, "Food", "Groceries")
    add_expense(999, "Bills", "Internet")

    set_budget(5000)
    print_ledger()
    print("Totals:", total_by_category())
    print("Remaining budget:", remaining_budget())

    largest = biggest_expense()
    print("Biggest expense:", largest["note"] if largest else None)
    print("Sync password accepted:", check_sync_password("guess"))
    print(
        "Summary:",
        len(expenses),
        "expenses recorded against a budget of",
        MONTHLY_BUDGET,
    )


if __name__ == "__main__":
    main()
