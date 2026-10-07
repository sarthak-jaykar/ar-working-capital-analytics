# Accounts Receivable \& Working Capital Analytics

[!\[Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[!\[Python](https://img.shields.io/badge/Python-Data%20Generation-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[!\[Pandas](https://img.shields.io/badge/Pandas-Data%20Preparation-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[!\[Finance](https://img.shields.io/badge/Domain-Finance%20%7C%20Accounts%20Receivable-2E7D32)](#)

An end-to-end simulated Accounts Receivable (AR) and working-capital analytics solution built to help finance teams monitor collections, identify delinquency risk, analyze receivables aging, and investigate operational disputes.

The project combines **Python-based synthetic data generation and validation** with a **Power BI reporting layer** covering executive performance, customer risk, collections prioritization, and dispute operations.

> \\\*\\\*Portfolio project:\\\*\\\* The company, customers, invoices, payments, and business scenarios are fictional/simulated and are intended for learning and portfolio demonstration.

\---

## Business Problem

Accounts receivable teams need more than a total outstanding balance. Finance leadership and collections teams need to understand:

* How much has been invoiced versus collected?
* How much AR remains outstanding and how much is overdue?
* Which customers represent the greatest delinquency exposure?
* Which aging buckets require immediate attention?
* Where are disputes tying up receivables?
* Which operational owners or dispute categories should be investigated?

This project translates those questions into an interactive finance dashboard for collection and working-capital decision support.

## Business Objectives

1. Monitor invoicing, collections, and outstanding receivables.
2. Analyze AR aging and delinquency exposure.
3. Identify high-risk customers and concentrated overdue balances.
4. Support invoice-level collection prioritization.
5. Analyze disputed receivables by category and operational owner.
6. Provide management-oriented views for collection and dispute follow-up.

## Key Business Questions

* What is the current receivables exposure?
* How much of the portfolio is overdue?
* Which aging buckets contain the largest balances?
* Which customers contribute most to overdue AR?
* How does customer risk relate to delinquency exposure?
* Which dispute categories and operational owners are associated with trapped receivables?
* Where should collections and dispute teams focus their next actions?

\---

## Dashboard Pages

### 1\. Executive Overview

!\[Executive Overview](Screenshots/01\_Executive\_Overview.png)

The executive page provides a management-level view of receivables and cash-collection performance.

**Focus areas:**

* Total invoiced and collected amounts
* Outstanding AR exposure
* Collection and delinquency KPIs
* Monthly billings versus cash collections
* Current versus overdue AR
* Aging-bucket distribution
* Disputed receivables by category

### 2\. Customer Risk \& Delinquency Deep Dive

!\[Customer Risk \& Delinquency Deep Dive](Screenshots/02\_Customer\_Deep\_Dive.png)

The customer-level page moves from portfolio-level exposure into collection prioritization.

**Focus areas:**

* Customer risk segmentation
* Overdue exposure by risk category
* Top delinquent customer accounts
* Invoice-level collection worklist
* Due dates, open balances, aging, and dispute information

### 3\. Dispute \& Collections Operations

!\[Dispute \& Collections Operations](Screenshots/03\_Dispute\_Operations.png)

The operations page focuses on disputed receivables and the operational causes behind collection delays.

**Focus areas:**

* Disputed AR exposure
* Dispute categories and root causes
* Operational ownership
* Aging severity across dispute categories
* Dispute-resolution worklist

\---

## Analytical Methodology

```text
Business Problem
      ↓
Synthetic Data Generation
      ↓
Data Validation
      ↓
Python / Pandas Data Generation \\\& Validation
      ↓
Power BI Data Model
      ↓
DAX Measures
      ↓
Interactive Dashboard
      ↓
Business Insights
      ↓
Collection \\\& Operations Actions
```

The analytical workflow separates **reproducible data generation and validation** from the **business reporting layer**. Python supports the source-data workflow, while Power BI provides interactive decision support for finance users.

## Data Model

The solution follows a finance-oriented star-schema approach with two fact tables and supporting dimensions:

```text
Dim\\\_Customer ───────────┐
                        │
                        ▼
                 Fact\\\_AR\\\_Invoices ◄──── Dim\\\_Dispute\\\_Reason
                        │
                        ▼
                 Fact\\\_AR\\\_Payments
```

### Source tables

|Table|Purpose|
|-|-|
|`Dim\\\_Customer`|Customer segment, credit limit, payment terms, and risk category|
|`Dim\\\_Dispute\\\_Reason`|Dispute category and operational ownership|
|`Fact\\\_AR\\\_Invoices`|Invoice dates, due dates, amounts, dispute attributes, and customer relationships|
|`Fact\\\_AR\\\_Payments`|Payment dates, payment amounts, methods, and invoice relationships|

## Tools \& Technologies

* **Power BI Desktop** — data modeling, DAX, interactive reporting
* **Python** — reproducible synthetic data generation and analysis
* **Pandas** — tabular data preparation and validation
* **NumPy** — deterministic data generation
* **CSV** — source data layer

## Repository Structure

```text
ar-working-capital-analytics/
├── README.md
├── data/
│   └── raw/
│       ├── Dim\\\_Customer.csv
│       ├── Dim\\\_Dispute\\\_Reason.csv
│       ├── Fact\\\_AR\\\_Invoices.csv
│       └── Fact\\\_AR\\\_Payments.csv
├── python/
│   └── 01\\\_generate\\\_data.py
├── powerbi/
│   └── AR\\\_Working\\\_Capital\\\_Analytics.pbix
├── documentation/
│   ├── dax\\\_measures.md
│   └── data\\\_dictionary.md
└── Screenshots/
    ├── 01\\\_Executive\\\_Overview.png
    ├── 02\\\_Customer\\\_Deep\\\_Dive.png
    └── 03\\\_Dispute\\\_Operations.png
```

## Reproduction

From the repository root:

```bash
cd python
python 01\\\_generate\\\_data.py
```

The script is intended to support reproducible generation of the simulated AR dataset. The Power BI file can then be opened from `powerbi/AR\\\_Working\\\_Capital\\\_Analytics.pbix`.

> \\\*\\\*Note:\\\*\\\* The current portfolio version is being refined further for metric/date consistency and operational filtering. The documentation intentionally describes the analytical design without hard-coding figures that are under validation.

## Business Value

The dashboard is designed to support four practical finance decisions:

1. **Monitor receivables exposure** — understand outstanding and overdue balances.
2. **Prioritize collections** — identify customers and invoices requiring attention.
3. **Reduce working-capital leakage** — investigate aging and delayed collections.
4. **Resolve operational disputes** — connect disputed receivables with root causes and owners.

## Documentation

* [DAX Measures Reference](documentation/dax_measures.md)
* [Data Dictionary](documentation/data_dictionary.md)

## Portfolio Context

This project represents the **Finance / Accounts Receivable** domain within a broader Business Analyst + Data Analyst portfolio. It demonstrates the combination of finance-domain understanding, analytical reasoning, data preparation, Power BI reporting, and business-oriented decision support.

## Author

**Sarthak Jaykar**  
B.Tech Computer Science + MBA Business Analytics

[GitHub](https://github.com/sarthak-jaykar) · [LinkedIn](https://www.linkedin.com/in/sarthak-jaykar/)

\---

*Simulated portfolio project. All company names, customers, transactions, and scenarios are fictional.*

