# Data Dictionary — Accounts Receivable \& Working Capital Analytics

The project uses four simulated source tables: two dimensions and two facts.

## Dim\_Customer

|Field|Description|
|-|-|
|`Customer\_Key`|Unique customer identifier used for relationships|
|`Customer\_Name`|Simulated customer name|
|`Customer\_Segment`|Enterprise, Mid-Market, or SMB segment|
|`Credit\_Limit\_USD`|Simulated customer credit limit|
|`Standard\_Payment\_Terms`|Standard contractual payment terms in days|
|`Risk\_Category`|Simulated Low, Medium, or High credit-risk category|

## Dim\_Dispute\_Reason

|Field|Description|
|-|-|
|`Dispute\_Reason\_Key`|Unique dispute-reason identifier|
|`Dispute\_Category`|Operational/root-cause category for a dispute|
|`Department\_Owner`|Functional team responsible for the dispute category|

## Fact\_AR\_Invoices

|Field|Description|
|-|-|
|`Invoice\_Key`|Unique invoice identifier|
|`Customer\_Key`|Customer relationship key|
|`Invoice\_Date`|Date the invoice was issued|
|`Due\_Date`|Contractual invoice due date|
|`Payment\_Terms\_Days`|Payment terms applied to the invoice|
|`Invoice\_Amount\_USD`|Gross invoice value in USD|
|`Dispute\_Flag`|Indicates whether the invoice is associated with a dispute|
|`Dispute\_Reason\_Key`|Relationship to the dispute-reason dimension|
|`Dispute\_Status`|Simulated dispute status|

## Fact\_AR\_Payments

|Field|Description|
|-|-|
|`Payment\_Key`|Unique payment identifier|
|`Invoice\_Key`|Invoice relationship key|
|`Payment\_Date`|Date payment was received|
|`Amount\_Paid\_USD`|Payment amount in USD|
|`Payment\_Method`|Simulated payment method|

## Modeling Notes

* `Dim\_Customer` provides customer-level attributes for invoice analysis.
* `Dim\_Dispute\_Reason` provides business context for dispute analysis.
* `Fact\_AR\_Invoices` is the primary transaction fact for receivables.
* `Fact\_AR\_Payments` records cash collections against invoices.
* Calculated aging, open balance, and KPI measures belong to the analytical/model layer rather than the raw CSV source layer.

