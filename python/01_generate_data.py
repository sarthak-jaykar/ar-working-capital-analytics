import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set deterministic seed for reproducibility
np.random.seed(42)

# ==========================================
# 1. PARAMETERS & TIMELINES
# ==========================================
NUM_CUSTOMERS = 150
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2025, 12, 31)
TOTAL_DAYS = (END_DATE - START_DATE).days

# ==========================================
# 2. DIM_CUSTOMER
# ==========================================
segments = ["Enterprise", "Mid-Market", "SMB"]
segment_weights = [0.20, 0.50, 0.30]

customer_data = []
for cid in range(1, NUM_CUSTOMERS + 1):
    seg = np.random.choice(segments, p=segment_weights)

    if seg == "Enterprise":
        credit_limit = np.random.choice([300000, 500000, 1000000])
        terms = np.random.choice([60, 90], p=[0.7, 0.3])
        risk = np.random.choice(["Low", "Medium"], p=[0.85, 0.15])
    elif seg == "Mid-Market":
        credit_limit = np.random.choice([50000, 100000, 200000])
        terms = np.random.choice([30, 45, 60], p=[0.4, 0.4, 0.2])
        risk = np.random.choice(["Low", "Medium", "High"], p=[0.5, 0.35, 0.15])
    else:  # SMB
        credit_limit = np.random.choice([15000, 25000, 50000])
        terms = np.random.choice([30, 45], p=[0.8, 0.2])
        risk = np.random.choice(["Low", "Medium", "High"], p=[0.3, 0.45, 0.25])

    customer_data.append(
        {
            "Customer_Key": f"CUST-{cid:04d}",
            "Customer_Name": f"Client Corp {cid:04d}",
            "Customer_Segment": seg,
            "Credit_Limit_USD": credit_limit,
            "Standard_Payment_Terms": terms,
            "Risk_Category": risk,
        }
    )

df_customer = pd.DataFrame(customer_data)

# ==========================================
# 3. DIM_DISPUTE_REASON
# ==========================================
dispute_reasons = [
    {
        "Dispute_Reason_Key": 1,
        "Dispute_Category": "Pricing / Billing Error",
        "Department_Owner": "Billing & Finance",
    },
    {
        "Dispute_Reason_Key": 2,
        "Dispute_Category": "Damaged / Defective Goods",
        "Department_Owner": "Quality Assurance",
    },
    {
        "Dispute_Reason_Key": 3,
        "Dispute_Category": "Missing / Mismatched PO",
        "Department_Owner": "Sales Operations",
    },
    {
        "Dispute_Reason_Key": 4,
        "Dispute_Category": "Late / Incomplete Delivery",
        "Department_Owner": "Supply Chain & Logistics",
    },
    {
        "Dispute_Reason_Key": 5,
        "Dispute_Category": "Contractual Terms Dispute",
        "Department_Owner": "Legal & Commercial",
    },
]
df_dispute_reason = pd.DataFrame(dispute_reasons)

# ==========================================
# 4. FACT_AR_INVOICES & FACT_AR_PAYMENTS
# ==========================================
invoices = []
payments = []

invoice_counter = 1
payment_counter = 1

for _, cust in df_customer.iterrows():
    if cust["Customer_Segment"] == "Enterprise":
        n_invoices = np.random.randint(110, 160)
        amt_range = (5000, 32000)
    elif cust["Customer_Segment"] == "Mid-Market":
        n_invoices = np.random.randint(60, 110)
        amt_range = (1500, 12000)
    else:
        n_invoices = np.random.randint(20, 50)
        amt_range = (500, 4000)

    for _ in range(n_invoices):
        inv_key = f"INV-{invoice_counter:06d}"
        invoice_counter += 1

        day_offset = np.random.randint(0, TOTAL_DAYS)
        inv_date = START_DATE + timedelta(days=int(day_offset))
        terms_days = int(cust["Standard_Payment_Terms"])
        due_date = inv_date + timedelta(days=terms_days)

        inv_amount = round(float(np.random.uniform(*amt_range)), 2)

        # Dispute probability tied to risk category
        dispute_prob = 0.14 if cust["Risk_Category"] == "High" else 0.05
        has_dispute = np.random.rand() < dispute_prob
        dispute_key = None
        dispute_status = "No Dispute"

        if has_dispute:
            dispute_key = int(np.random.choice(df_dispute_reason["Dispute_Reason_Key"]))
            dispute_status = np.random.choice(["Resolved", "Open"], p=[0.72, 0.28])

        invoices.append(
            {
                "Invoice_Key": inv_key,
                "Customer_Key": cust["Customer_Key"],
                "Invoice_Date": inv_date.strftime("%Y-%m-%d"),
                "Due_Date": due_date.strftime("%Y-%m-%d"),
                "Payment_Terms_Days": terms_days,
                "Invoice_Amount_USD": inv_amount,
                "Dispute_Flag": 1 if has_dispute else 0,
                "Dispute_Reason_Key": dispute_key,
                "Dispute_Status": dispute_status,
            }
        )

        # Payment behavior: on-time (67%), minor late (19%), major late (9%), unpaid (5%)
        behavior = np.random.choice(
            ["on_time", "minor_late", "major_late", "unpaid"],
            p=[0.67, 0.19, 0.09, 0.05],
        )

        if dispute_status == "Open":
            behavior = "unpaid"

        if behavior != "unpaid":
            if behavior == "on_time":
                delay = np.random.randint(-5, 1)
            elif behavior == "minor_late":
                delay = np.random.randint(1, 31)
            else:
                delay = np.random.randint(31, 95)

            pay_date = due_date + timedelta(days=int(delay))

            # Allow payments through early 2026 to reflect normal lag
            if pay_date <= END_DATE + timedelta(days=60):
                # 10% probability of partial settlement across two tranches
                if np.random.rand() < 0.10:
                    part1 = round(inv_amount * np.random.uniform(0.4, 0.6), 2)
                    part2 = round(inv_amount - part1, 2)

                    payments.append(
                        {
                            "Payment_Key": f"PAY-{payment_counter:07d}",
                            "Invoice_Key": inv_key,
                            "Payment_Date": pay_date.strftime("%Y-%m-%d"),
                            "Amount_Paid_USD": part1,
                            "Payment_Method": np.random.choice(
                                ["ACH", "Wire", "Check"], p=[0.65, 0.25, 0.10]
                            ),
                        }
                    )
                    payment_counter += 1

                    pay2_date = pay_date + timedelta(
                        days=int(np.random.randint(10, 25))
                    )
                    payments.append(
                        {
                            "Payment_Key": f"PAY-{payment_counter:07d}",
                            "Invoice_Key": inv_key,
                            "Payment_Date": pay2_date.strftime("%Y-%m-%d"),
                            "Amount_Paid_USD": part2,
                            "Payment_Method": np.random.choice(
                                ["ACH", "Wire", "Check"], p=[0.65, 0.25, 0.10]
                            ),
                        }
                    )
                    payment_counter += 1
                else:
                    payments.append(
                        {
                            "Payment_Key": f"PAY-{payment_counter:07d}",
                            "Invoice_Key": inv_key,
                            "Payment_Date": pay_date.strftime("%Y-%m-%d"),
                            "Amount_Paid_USD": inv_amount,
                            "Payment_Method": np.random.choice(
                                ["ACH", "Wire", "Check"], p=[0.65, 0.25, 0.10]
                            ),
                        }
                    )
                    payment_counter += 1

df_invoices = pd.DataFrame(invoices)
df_payments = pd.DataFrame(payments)

# Export clean CSV files
from pathlib import Path
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df_customer.to_csv(OUTPUT_DIR / "Dim_Customer.csv", index=False)
df_dispute_reason.to_csv(OUTPUT_DIR / "Dim_Dispute_Reason.csv", index=False)
df_invoices.to_csv(OUTPUT_DIR / "Fact_AR_Invoices.csv", index=False)
df_payments.to_csv(OUTPUT_DIR / "Fact_AR_Payments.csv", index=False)

print(f"Data generation complete:")
print(f" - Dim_Customer: {len(df_customer)} records")
print(f" - Dim_Dispute_Reason: {len(df_dispute_reason)} records")
print(f" - Fact_AR_Invoices: {len(df_invoices)} records")
print(f" - Fact_AR_Payments: {len(df_payments)} records")
