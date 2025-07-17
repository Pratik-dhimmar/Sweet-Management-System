# 🍬 Sweet Shop Management System

A fully test-driven inventory management system for a sweet shop. This Python-based CLI backend allows adding, deleting, searching, sorting, purchasing, and restocking sweets using clean code and SOLID principles.

---

## 📌 Features

- ✅ **Add Sweet** – Add new sweets with ID, name, category, price, and quantity
- ❌ **Delete Sweet** – Remove a sweet from the system by ID
- 👀 **View All Sweets** – See a full list of available sweets
- 🔍 **Search Sweets** – Search by name, category, or price range
- 🧮 **Sort Sweets** – Sort sweets by name, category, or price (asc/desc)
- 🛒 **Purchase Sweet** – Reduce stock on valid purchase
- 📦 **Restock Sweet** – Increase available quantity

All operations are unit-tested using **TDD-first** workflow.

---

## ⚙️ Technologies Used

- **Python 3.11+**
- `unittest` (standard library)
- Git for version control
- [Optional: AI assistance where indicated]

> ✅ No third-party dependencies required.

---

## 🧪 Test-Driven Development (TDD)

This project strictly followed TDD:
1. Wrote failing tests first
2. Wrote the minimal implementation to pass tests
3. Refactored cleanly
4. Repeated the cycle for each feature

You can explore test cases in `tests/test_inventory.py`.

---

## 📁 Project Structure

```text
sweet-shop-management/
│
├── sweetshop/
│   ├── models.py          # Sweet class
│   └── inventory.py       # Business logic for inventory operations
│
├── tests/
│   └── test_inventory.py  # All unit tests using unittest
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧪 Running the Tests

```bash
# Clone the repository
git clone https://github.com/Pratik-dhimmar/Sweet-Management-System.git
cd Sweet-Management-System 

# Run all unit tests
python -m unittest discover
```

---

## 📊 Sample Sweet Data

| ID   | Name        | Category     | Price | Quantity |
|------|-------------|--------------|-------|----------|
| 1001 | Kaju Katli  | Nut-Based    | 50    | 20       |
| 1002 | Gajar Halwa | Vegetable    | 30    | 15       |
| 1003 | Gulab Jamun | Milk-Based   | 10    | 50       |

---

## 🧪 Run Manually (Interactive Mode)

To try the system interactively:

```bash
python main.py

## 🧼 Clean Code Practices

- Follows **SOLID principles**
- Follows **Single Responsibility** per method/module
- Defensive programming: input validation and graceful error handling
- Strong modular separation between models and logic

---

## 🧠 AI Commit Note

> Some commits used AI assistance for generating test cases or refactoring during implementation. All logic was reviewed and validated manually.

---


## 🙋 Contact

Feel free to connect:

- 📧 dpm8901@example.com
- 💼 [LinkedIn](https://www.linkedin.com/in/pratik-dhimmar-3168002b4/)
- 🌐 [GitHub](https://github.com/Pratik-dhimmar/)

---

