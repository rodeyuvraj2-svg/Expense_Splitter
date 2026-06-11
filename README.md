# Expense Splitter

A simple command-line Expense Splitter application built with Python. It helps users manage shared expenses, track balances, and settle debts between group members.

## Features

* Add members
* Add expenses
* Split expenses equally among selected members
* View balances
* Track who owes whom
* Settle debts
* Store data using JSON files
* View expense history

## Project Structure

```text
Expense_Splitter/
│
├── cli/
│   ├── balance.py
│   ├── expense.py
│   ├── member.py
│   └── settlement.py
│
├── models/
│   └── expense.py
│
├── services/
│   ├── balance.py
│   ├── expense.py
│   ├── member.py
│   └── settlement.py
│
├── storage/
│   ├── members.json
│   └── expense.json
│
├── main.py
└── README.md
```
## Usage

### Main Menu

```text
1. Add Member
2. Add Expense
3. Balance
4. Settlement
5. Exit
```

### Add Expense

* Enter expense name
* Enter total amount
* Select payer
* Select members involved
* Expense is automatically split equally

### Show Balance

Displays:

```text
payer should receive 3500

member 1 owes 1750
member 2 owes 1750
```

### Settlement

Allows members to pay their pending debt and updates balances automatically.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON File Handling

## Concepts Implemented

* Classes and Objects
* Inheritance
* File Handling
* JSON Storage
* Data Persistence
* Modular Programming

## Author

Yuvraj Rode
