# Accounts Receivable & Working Capital Analytics

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Python](https://img.shields.io/badge/Python-EDA-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue)
![Finance](https://img.shields.io/badge/Domain-Finance-green)

## Overview

This project presents a simulated **Accounts Receivable (AR) and Working Capital Analytics solution** designed to help finance teams monitor receivables, identify collection risks, analyze customer payment behavior, and support working-capital decisions.

The project combines **Python-based data preparation and exploratory analysis with Power BI reporting**, transforming transactional AR data into an interactive management dashboard.

The solution focuses on three key areas:

* Executive AR and working-capital performance
* Customer-level receivables and collection analysis
* Dispute and collection operations

> **Portfolio project:** Built using synthetic data and simulated business scenarios for analytical and learning purposes.

---

## Business Objectives

The dashboard is designed to help finance and collections teams:

* Monitor total invoiced, collected, and outstanding receivables
* Track overdue and aging receivables
* Analyze customer payment behavior
* Identify high-risk and high-exposure customers
* Monitor collection performance
* Analyze invoice disputes and their operational impact
* Identify receivables requiring collection attention
* Support working-capital and cash-flow improvement decisions

---

## Key Business Questions

The analysis addresses questions such as:

* How much receivables exposure is currently outstanding?
* What proportion of receivables is overdue?
* Which customers contribute the highest outstanding balances?
* Which customers require collection attention?
* What does the receivables aging profile look like?
* Which payment behaviors indicate collection risk?
* How significant are invoice disputes?
* Which dispute categories require operational attention?
* Where should collection teams prioritize their efforts?

---

# Dashboard

The Power BI solution contains three analytical pages.

## 1. Executive Overview

Provides a high-level view of Accounts Receivable performance, including:

* Total invoiced amount
* Amount collected
* Outstanding receivables
* Overdue receivables
* Receivables aging
* Collection performance
* Key AR trends and management indicators

![Executive Overview](Screenshots/Page1_Executive_Overview.png)

---

## 2. Customer Deep Dive

Provides customer-level analysis to identify receivables concentration and collection priorities.

Key analysis includes:

* Customer outstanding balances
* Overdue exposure
* Aging distribution
* Top delinquent accounts
* Customer payment behavior
* Collection performance by customer

![Customer Deep Dive](Screenshots/Page2_Customer_Deep_Dive.png)

---

## 3. Dispute Operations

Focuses on the operational side of receivables management.

Key analysis includes:

* Invoice dispute activity
* Dispute categories
* Dispute status
* Customer-level dispute exposure
* Collection and resolution activity
* Operational areas requiring attention

![Dispute Operations](Screenshots/Page3_Dispute_Operations.png)

---

# Analytical Methodology

The project follows an end-to-end analytics workflow:

**Business Problem → Data Generation → Data Validation → Python Analysis → Power BI Data Model → DAX Measures → Dashboard → Insights → Recommendations**

### 1. Business Problem

Defined the Accounts Receivable and working-capital problem from a finance and collections perspective.

### 2. Data Generation

Created a synthetic transactional dataset representing invoices, payments, customers, and dispute information.

### 3. Data Validation

Validated relationships, amounts, dates, payment records, customer mappings, and transactional consistency.

### 4. Python Analysis

Used Python, Pandas, and NumPy for exploratory analysis and data validation before dashboard development.

### 5. Power BI Data Model

Structured the data into dimension and fact tables to support customer, invoice, payment, and dispute analysis.

### 6. DAX

Created calculated measures and analytical KPIs for receivables and collection performance.

### 7. Dashboard

Built an interactive Power BI report covering executive performance, customer analysis, and dispute operations.

### 8. Insights & Recommendations

Used the analytical results to identify collection risks, customer concentration, aging patterns, and operational priorities.

---

# Data Model

The project uses a simple finance-oriented analytical model consisting of:

* **Dim_Customer** — customer master information
* **Dim_Dispute_Reason** — dispute classification
* **Fact_AR_Invoices** — invoice-level receivables transactions
* **Fact_AR_Payments** — payment transactions

This structure separates transactional facts from descriptive dimensions and supports customer-level and operational AR analysis.

---

# Tools & Technologies

| Tool                 | Purpose                                            |
| -------------------- | -------------------------------------------------- |
| **Power BI Desktop** | Dashboard development, data modeling and reporting |
| **DAX**              | Financial and analytical measures                  |
| **Python**           | Data preparation and exploratory analysis          |
| **Pandas**           | Data manipulation and validation                   |
| **NumPy**            | Numerical analysis                                 |
| **CSV**              | Source data format                                 |

---

# Dataset

The project uses **synthetic FY2025 Accounts Receivable data** created specifically for this portfolio project.

The dataset represents realistic finance scenarios involving:

* Customers
* Invoices
* Payments
* Outstanding balances
* Overdue receivables
* Aging categories
* Payment behavior
* Invoice disputes

No real company or customer information is used.

---

# Repository Structure

```text
ar-working-capital-analytics/
├── README.md
├── data/
│   └── raw/
│       ├── Dim_Customer.csv
│       ├── Dim_Dispute_Reason.csv
│       ├── Fact_AR_Invoices.csv
│       └── Fact_AR_Payments.csv
├── python/
│   └── 01_generate_data.py
├── powerbi/
│   └── AR_Working_Capital_Analytics.pbix
├── documentation/
│   ├── dax_measures.md
│   └── data_dictionary.md
└── Screenshots/
    ├── Page1_Executive_Overview.png
    ├── Page2_Customer_Deep_Dive.png
    └── Page3_Dispute_Operations.png
```

---

# Reproduction

To regenerate the synthetic dataset:

```bash
cd python
python 01_generate_data.py
```

The generated CSV files are stored under:

```text
data/raw/
```

For the analytical workflow:

1. Run the Python data-generation script.
2. Review the generated datasets.
3. Open the Power BI file.
4. Refresh the data if required.
5. Explore the three dashboard pages.

---

# Documentation

Additional project documentation is available in the repository:

* [DAX Measures](documentation/dax_measures.md)
* [Data Dictionary](documentation/data_dictionary.md)

---

# Business Value

An Accounts Receivable analytics solution can help finance and collections teams move from basic receivables reporting toward more structured collection management.

The analysis supports:

* Better visibility into outstanding receivables
* Identification of overdue exposure
* Customer-level collection prioritization
* Monitoring of payment behavior
* Dispute management
* Working-capital visibility
* Data-driven collection decisions

---

# Project Scope

This is a **simulated portfolio project** created for demonstrating finance-domain analytics, Power BI reporting, Python-based analysis, and business problem-solving skills.

The company, customers, transactions, and business scenarios are fictional.

---

## Author

**Sarthak Jaykar**
B.Tech Computer Science + MBA Business Analytics

[GitHub](https://github.com/sarthak-jaykar) · [LinkedIn](https://www.linkedin.com/in/sarthak-jaykar/)
