# DAX Measures Reference — Accounts Receivable \& Working Capital Analytics

This document records the principal business measures used by the Accounts Receivable and Working Capital Analytics dashboard.

> \*\*Validation note:\*\* The current Power BI model is scheduled for a metric/date-consistency review. This reference documents the intended business definitions and measure architecture; numerical outputs will be revalidated before the final portfolio release.

\---

## 1\. Collections \& Receivables Metrics

### Total Invoiced

**Business definition:** Total monetary value of invoices issued within the current filter context.

```DAX
Total Invoiced =
SUM(Fact\_AR\_Invoices\[Invoice\_Amount\_USD])
```

### Total Collected

**Business definition:** Total cash payments recorded against AR invoices.

```DAX
Total Collected =
SUM(Fact\_AR\_Payments\[Amount\_Paid\_USD])
```

### AR Outstanding

**Business definition:** Uncollected invoice value remaining after recorded payments.

The final implementation should reconcile invoice balances against the payment fact table rather than relying on an undocumented source column.

### Collection Efficiency %

**Business definition:** Collected cash as a proportion of invoiced value.

```DAX
Collection Efficiency % =
DIVIDE(\[Total Collected], \[Total Invoiced], 0)
```

\---

## 2\. Aging \& Delinquency Metrics

### Overdue AR

**Business definition:** Outstanding receivables whose invoices are past their contractual due date within the selected as-of context.

The final implementation should use a consistent aging/as-of date across AR balance and aging measures.

### Current AR

**Business definition:** Outstanding receivables that remain within payment terms at the selected as-of date.

### Overdue AR %

**Business definition:** Overdue outstanding receivables as a proportion of total outstanding AR.

```DAX
Overdue AR % =
DIVIDE(\[Overdue AR], \[AR Outstanding], 0)
```

### Days Sales Outstanding (DSO)

**Business definition:** A working-capital efficiency metric estimating the average number of days required to collect receivables.

The final DSO implementation must be validated against the chosen business definition and date basis before release.

\---

## 3\. Aging Bucket Measures

The dashboard uses the following conceptual aging buckets:

* Current
* 1–30 Days
* 31–60 Days
* 61–90 Days
* 90+ Days

Example measure pattern:

```DAX
AR 90+ Days =
CALCULATE(
    \[AR Outstanding],
    Fact\_AR\_Invoices\[Aging\_Bucket] = "90+ Days"
)
```

The final model should ensure that the aging bucket is calculated from the same as-of date used for the corresponding AR balance.

\---

## 4\. Customer Risk Metrics

### Overdue Customers Count

**Business definition:** Distinct customers with overdue outstanding receivables.

```DAX
Overdue Customers Count =
CALCULATE(
    DISTINCTCOUNT(Fact\_AR\_Invoices\[Customer\_Key]),
    Fact\_AR\_Invoices\[Aging\_Bucket] IN {
        "1-30 Days",
        "31-60 Days",
        "61-90 Days",
        "90+ Days"
    }
)
```

Customer-level analysis is supported through the relationship between `Fact\_AR\_Invoices` and `Dim\_Customer`.

\---

## 5\. Dispute Operations Metrics

### Disputed AR Amount

**Business definition:** Outstanding receivables associated with active/open disputes.

```DAX
Disputed AR Amount =
CALCULATE(
    \[AR Outstanding],
    Fact\_AR\_Invoices\[Dispute\_Status] = "Open"
)
```

### Disputed AR %

**Business definition:** Active disputed AR as a proportion of total outstanding AR.

```DAX
Disputed AR % =
DIVIDE(\[Disputed AR Amount], \[AR Outstanding], 0)
```

### Open Disputes Count

**Business definition:** Count of invoice-level records currently marked as open disputes.

```DAX
Open Disputes Count =
CALCULATE(
    COUNTROWS(Fact\_AR\_Invoices),
    Fact\_AR\_Invoices\[Dispute\_Status] = "Open"
)
```

\---

## 6\. Measure Design Principles

The measure layer is designed around four finance questions:

1. **How much was billed?**
2. **How much cash was collected?**
3. **How much receivable exposure remains and how severe is the aging?**
4. **How much working capital is tied up in disputes?**

Measures should remain filter-aware so users can analyze the same KPIs by customer, segment, risk category, aging bucket, dispute category, and operational owner.

\---

## 7\. Final Validation Checklist

Before the final portfolio release, validate:

* Invoice totals reconcile with the source invoice table.
* Payment totals reconcile with the payment fact table.
* AR outstanding reconciles to invoice value less applicable payments.
* Aging and AR balances use the same as-of date.
* DSO uses the intended business definition and date basis.
* Dispute visuals are restricted to the intended dispute status.
* Customer concentration claims are calculated from the same overdue-AR definition used by the dashboard.

