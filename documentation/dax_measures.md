# DAX Measures Reference — Accounts Receivable & Working Capital Analytics

This document records the intended business definitions and measure patterns for the Accounts Receivable and Working Capital Analytics dashboard.

> **Validation status:** The Power BI report file has not been opened and inspected in Power BI Desktop during this repository update. The definitions below are therefore a reference specification, not confirmation that the PBIX measures and visuals implement them. Final model-level verification remains outstanding.

---

## 1. Collections & Receivables Metrics

### Total Invoiced

**Business definition:** Total monetary value of invoices issued within the current filter context.

```dax
Total Invoiced =
SUM ( Fact_AR_Invoices[Invoice_Amount_USD] )
```

### Total Collected

**Business definition:** Total cash payments recorded against AR invoices.

```dax
Total Collected =
SUM ( Fact_AR_Payments[Amount_Paid_USD] )
```

### AR Outstanding

**Business definition:** Uncollected invoice value remaining after payments received by the selected as-of date.

**Reference logic:** For each invoice in scope, subtract payments recorded on or before the as-of date from the invoice amount. Sum the remaining invoice balances. Payments after the as-of date must not reduce the snapshot balance.

### Collection Efficiency %

**Business definition:** Collected cash as a proportion of total invoiced value.

```dax
Collection Efficiency % =
DIVIDE ( [Total Collected], [Total Invoiced], 0 )
```

---

## 2. Aging & Delinquency Metrics

### Overdue AR

**Business definition:** Outstanding receivables whose invoice due date is earlier than the selected as-of date.

**Reference logic:** Calculate the unpaid balance at the same as-of date used for AR Outstanding, then include only invoices whose due date has passed.

### Current AR

**Business definition:** Outstanding receivables that remain within payment terms at the selected as-of date.

**Reference logic:** Calculate the unpaid balance at the same as-of date used for AR Outstanding, then include invoices whose due date has not passed.

### Overdue AR %

**Business definition:** Overdue outstanding receivables as a proportion of total outstanding AR.

```dax
Overdue AR % =
DIVIDE ( [Overdue AR], [AR Outstanding], 0 )
```

### Days Sales Outstanding (DSO)

**Business definition:** Period-end AR outstanding expressed as a number of days of invoiced sales for the full FY2024–FY2025 reporting period.

```dax
DSO =
DIVIDE ( [AR Outstanding], [Total Invoiced], 0 ) * 731
```

**Date basis:** 1 January 2024 through 31 December 2025 inclusive (731 days). The README reports DSO as 104.7 days using the 31 December 2025 AR snapshot and total invoiced value for this two-year period.

**Interpretation:** This is a period-end snapshot DSO calculation. It uses period-end AR rather than average AR; it should not be described as an average-balance DSO calculation.

---

## 3. Aging Bucket Measures

The dashboard uses the following conceptual aging buckets:

- Current
- 1–30 Days
- 31–60 Days
- 61–90 Days
- 90+ Days

Example measure pattern:

```dax
AR 90+ Days =
CALCULATE (
    [AR Outstanding],
    Fact_AR_Invoices[Aging_Bucket] = "90+ Days"
)
```

The aging bucket must be calculated from the same as-of date used for the corresponding AR balance.

---

## 4. Customer Risk Metrics

### Overdue Customers Count

**Business definition:** Distinct customers with overdue outstanding receivables.

```dax
Overdue Customers Count =
CALCULATE (
    DISTINCTCOUNT ( Fact_AR_Invoices[Customer_Key] ),
    Fact_AR_Invoices[Aging_Bucket] IN {
        "1-30 Days",
        "31-60 Days",
        "61-90 Days",
        "90+ Days"
    }
)
```

Customer-level analysis is supported through the relationship between `Fact_AR_Invoices` and `Dim_Customer`.

---

## 5. Dispute Operations Metrics

### Disputed AR Amount

**Business definition:** Outstanding receivables associated with active/open disputes.

```dax
Disputed AR Amount =
CALCULATE (
    [AR Outstanding],
    Fact_AR_Invoices[Dispute_Status] = "Open"
)
```

### Disputed AR %

**Business definition:** Active disputed AR as a proportion of total outstanding AR.

```dax
Disputed AR % =
DIVIDE ( [Disputed AR Amount], [AR Outstanding], 0 )
```

### Open Disputes Count

**Business definition:** Count of invoice-level records currently marked as open disputes.

```dax
Open Disputes Count =
CALCULATE (
    COUNTROWS ( Fact_AR_Invoices ),
    Fact_AR_Invoices[Dispute_Status] = "Open"
)
```

---

## 6. Measure Design Principles

The measure layer is designed around four finance questions:

1. How much was billed?
2. How much cash was collected?
3. How much receivable exposure remains, and how severe is the aging?
4. How much working capital is tied up in disputes?

Measures should remain filter-aware so users can analyze the same KPIs by customer, segment, risk category, aging bucket, dispute category and operational owner.

All snapshot balances, aging measures and overdue calculations must use a consistent as-of date.

---

## 7. Final Validation Checklist

Before treating the Power BI model as verified, confirm in Power BI Desktop:

- Invoice totals reconcile with the source invoice table.
- Payment totals reconcile with the payment fact table.
- AR outstanding reconciles to invoice value less applicable payments as of 31 December 2025.
- Payments dated after the cutoff do not reduce the 31 December 2025 outstanding balance.
- Aging and AR balances use the same as-of date.
- DSO uses the documented 731-day reporting period and period-end AR basis.
- Dispute visuals are restricted to the intended `Open` dispute status.
- Customer concentration claims use the same overdue-AR definition as the dashboard.
