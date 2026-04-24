# 🗂️ KingshukDatta — Projects

A curated collection of beginner-to-intermediate programming projects written in **Python** and **JavaScript**. The repository covers CLI games, GUI apps, utility scripts, and a database-integrated management system — built to practice and demonstrate core programming concepts.

---

## 📁 Repository Structure

```
Projects/
├── Python Projects/
│   ├── Mini Projects/
│   │   ├── rock_paper_scissor.py
│   │   ├── tic_tac_toe.py
│   │   ├── rent_calculator.py
│   │   └── rent_calculator_improved.py
│   └── Main Projects/
│       └── Student Result Manager/
│           ├── student_result_manager.py
│           ├── student_result_management_Database.py
│           └── Student Result Management Database Script.sql
└── JavaScript Projects/
    └── Mini Projects/
        └── slotMachine.js
```

---

## 🐍 Python Projects

### Mini Projects

#### ✂️ Rock Paper Scissors (`rock_paper_scissor.py`)
A classic command-line Rock, Paper, Scissors game against the computer.

**Features:**
- Random computer choice using Python's `random` module
- Continuous play loop — play as many rounds as you want
- Clean input handling with exit options (`exit`, `quit`, `e`, `q`)

**How to run:**
```bash
python rock_paper_scissor.py
```

---

#### ❌⭕ Tic-Tac-Toe (`tic_tac_toe.py`)
A two-player Tic-Tac-Toe game with a graphical user interface built using Python's `tkinter` library.

**Features:**
- Interactive 3×3 GUI grid
- Alternating turns between Player X and Player O
- Automatic winner detection with a visual highlight (winning cells turn green)
- On-screen label showing whose turn it is

**Requirements:**
- Python 3.x (tkinter is included in the standard library)

**How to run:**
```bash
python tic_tac_toe.py
```

---

#### 🏠 Rent Calculator (`rent_calculator.py` & `rent_calculator_improved.py`)
A utility script to split shared living expenses equally among flatmates.

**Inputs:**
- Monthly rent
- Total food ordered
- Electricity units consumed & charge per unit
- Number of persons sharing the flat

**Output:** The equal share each person must pay.

The **improved version** wraps the logic in a reusable function for better code organisation.

**How to run:**
```bash
python rent_calculator.py
# or
python rent_calculator_improved.py
```

---

### Main Projects

#### 🎓 Student Result Manager

A menu-driven student management system available in two versions:

**Version 1 — Dictionary-based (`student_result_manager.py`)**

Stores student data in-memory using a Python dictionary.

| Menu Option | Action |
|---|---|
| 1 | Add a student (name, roll number, marks) |
| 2 | View all students |
| 3 | Check result & grade for a student |
| 4 | Exit |

**How to run:**
```bash
python student_result_manager.py
```

---

**Version 2 — MySQL Database (`student_result_management_Database.py`)**

Persists student data in a MySQL database with full CRUD operations.

| Menu Option | Action |
|---|---|
| 1 | Add a student |
| 2 | View all students |
| 3 | Check result & grade |
| 4 | Delete a student |
| 5 | Exit |

**Requirements:**
- MySQL server running locally
- A database named `school` with a `students` table (see `Student Result Management Database Script.sql`)
- `mysql-connector-python` package

```bash
pip install mysql-connector-python
```

**Database setup:**
```bash
mysql -u root -p < "Student Result Management Database Script.sql"
```

**How to run:**
```bash
python student_result_management_Database.py
```

**Grading Scale:**

| Marks | Grade |
|---|---|
| 80 – 100 | A+ |
| 70 – 79 | A |
| 60 – 69 | A- |
| 50 – 59 | B |
| 40 – 49 | C |
| 33 – 39 | D |
| Below 33 | F |

---

## 🟨 JavaScript Projects

### Mini Projects

#### 🎰 Slot Machine (`slotMachine.js`)
A terminal-based slot machine game with a betting system, built with Node.js.

**Features:**
- Deposit real money (virtual balance) to start
- Choose how many lines (1–3) to bet on
- Set a bet amount per line
- Spin a 3×3 reel with symbols A, B, C, D (each with different rarity and payout)
- Win if all symbols on a bet line match
- Game ends automatically when balance hits zero

**Symbol Payouts:**

| Symbol | Rarity | Multiplier |
|---|---|---|
| A | Rarest (×2) | 5× |
| B | Rare (×4) | 4× |
| C | Common (×6) | 3× |
| D | Most common (×8) | 2× |

**Requirements:**
- Node.js installed
- `prompt-sync` package (already listed in `package.json`)

**How to run:**
```bash
cd "JavaScript Projects/Mini Projects"
npm install
node slotMachine.js
```

---

## 🛠️ Tech Stack

| Language | Libraries / Tools |
|---|---|
| Python | `tkinter`, `random`, `mysql-connector-python` |
| JavaScript | Node.js, `prompt-sync` |
| Database | MySQL |

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KingshukDatta/Projects.git
   cd Projects
   ```

2. **Run a Python project:**
   ```bash
   cd "Python Projects/Mini Projects"
   python rock_paper_scissor.py
   ```

3. **Run the JavaScript Slot Machine:**
   ```bash
   cd "JavaScript Projects/Mini Projects"
   npm install
   node slotMachine.js
   ```

---

## 📌 Notes

- Python 3.x is required for all Python projects.
- The `tkinter` library is bundled with standard Python installations on Windows and macOS. Linux users may need to install it separately:
  ```bash
  sudo apt install python3-tk
  ```
- The database version of the Student Result Manager requires a locally running MySQL instance with credentials configured in the script (`host`, `user`, `password`, `database`).

---

## 👤 Author

**Kingshuk Datta**  
GitHub: [@KingshukDatta](https://github.com/KingshukDatta)
