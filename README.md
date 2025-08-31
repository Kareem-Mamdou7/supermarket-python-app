# 🛒 Supermarket Management System

A **menu-driven Python application** that simulates the day-to-day operations of a supermarket.  
This project was developed as part of my training at the **National Telecommunication Institute (NTI)** under the guidance of **Ahmed Madeh**.

---

## 🚀 Features

### 📦 Product & Inventory Management

- Add, update, and remove products.
- Track product stock levels in real time.
- Store product data persistently using **JSON files**.

### 🛍️ Cart & Checkout System

- Add or remove items from the cart with quantity validation.
- Automatic bill calculation with payment and change generation.
- Save every transaction to a text file for record-keeping.

### 👤 Customer Interaction

- User-friendly **command-line menu interface**.
- Prevents invalid operations (like removing unavailable products).
- Provides clear summaries of purchases and stock updates.

### 📊 End-to-End Workflow

- From stock management → cart operations → checkout → transaction history.

---

## 🧑‍💻 Tech Stack

- **Language:** Python
- **Concepts:** Object-Oriented Programming (OOP), File Handling, JSON Persistence
- **Files:**
  - `supermarket.py` → main application logic
  - `products.json` → persistent storage of inventory
  - `transactions.txt` → record of completed purchases

---

## 📂 Project Structure

```
Supermarket-System-OOP/
│
├── supermarket.py        # Main application
├── products.json         # Product database
├── transactions.txt      # Checkout transaction logs
└── README.md             # Project documentation
```

---

## 📸 Demo (Sample Run)

```
Welcome To Kareem's Market!

What Do You Want To Do?
(1) Display Store Products. (Stock)
(2) Add Product To Store.
(3) Remove Product from Store
(4) Display Cart.
(5) Add Product To Cart.
(6) Remove Product From Cart.
(7) Checkout.
(8) Read Transactions' File.
(9) Exit.
```

---

## 🎯 Learning Outcomes

- Applied **OOP principles** for structured, modular design.
- Built a **persistent storage system** using JSON.
- Designed an **interactive CLI application** with real-world logic.
- Practiced clean, maintainable, and scalable coding practices.

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Run the program:
   ```bash
   python supermarket.py
   ```

---

## 🙏 Acknowledgments

Special thanks to my NTI instructor **Ahmed Madeh** for his guidance and support during this project.

---

## 📎 License

This project is for educational purposes. You are free to use and modify it.
