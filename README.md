
# 💰 Track My Finances 

A lightweight, Python-based terminal application designed to help you manage multiple financial accounts, track income and expenses, and visualize your transaction history via CSV files.

## 🚀 Features

* **Account Management**: Create and switch between multiple financial accounts.
* **Persistent Storage**: All data is saved in structured `.csv` files within an `Accounts/` directory.
* **Transaction Tracking**: Easily log **Income** and **Expenses** with categories and timestamps.
* **Smart Filtering**: Search your history by:
    * Transaction Type (Income/Expense)
    * Category
    * Specific Date, Month, or Year.


* **Real-time Balance**: Automatically calculates and updates your balance after every transaction.

## 🛠️ Technical Architecture

The project follows Object-Oriented Programming (OOP) principles to ensure code maintainability:

* **`Account`**: Handles file I/O, balance loading, and account validation.
* **`Transaction`**: Manages the logic for adding, listing, and filtering financial records.
* **`Menu`**: Orchestrates the CLI flow and user interactions.
* **`Utils`**: Contains helper methods for input validation and terminal formatting.

## 📥 Installation & Usage

### Prerequisites

* Python 3.x installed on your machine.

### Running the App

1. **Clone the repository**:
```bash
git clone https://github.com/JMaxtos/trackmyfinances.git
cd trackmyfinances

```

2. **Run the application**:
```bash
python menu.py

```

## 📊 Data Format

Transactions are stored in a standard CSV format, making it easy to export your data to Excel or Google Sheets:
| Date | Type | Category | Value | Balance |
| :--- | :--- | :--- | :--- | :--- |
| 2026-02-02 17:00 | Income | Initial Amount | 1000.0 | 1000.0 |
| 2026-02-02 17:05 | Expense | Groceries | 50.0 | 950.0 |

---

## 📝 Future Improvements

* [ ] Add Visual UI.
* [ ] Add Data Visualization 
