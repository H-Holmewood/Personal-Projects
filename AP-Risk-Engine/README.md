P2P Operational Interrogation & Risk Dashboard
Project Overview

This project demonstrates a comprehensive data analysis of a £1.2M Accounts Payable ledger. The goal was to move beyond basic reporting to "interrogate" the data for actionable insights—specifically identifying financial risk, process bottlenecks, and opportunities for digital supplier migration.
Key Analytical Insights

    Risk-Based Spend Analysis (Pareto 80/20): Identified that 20% of suppliers account for over 80% of total spend. This allows the finance team to prioritize reconciliations for high-exposure vendors.

    Fraud & Leakage Prevention: Engineered a custom DAX logic to detect potential duplicate payments (flagging 3 instances in the current ledger), essential for preventing cash loss.

    Workflow Bottleneck Identification: Analyzed "Average Approval Lag" by department, revealing that IT and Logistics have the highest friction, directly impacting STP% (Straight-Through Processing).

    Digital Transformation Strategy: Categorized spend by "Ingestion Channel." Identified high-value suppliers still using "Paper" and "Email" to prioritize for EDI/Portal migration.

Technical Challenges & Solutions

    Data Recovery: Resolved a critical SQL database corruption (Error HY000) during development by executing a disaster recovery plan—rebuilding the environment from flat-file backups via Power Query.

    Dynamic Sorting: Overcame Power BI visual conflicts between cumulative DAX measures and categorical axis sorting to maintain a mathematically accurate Pareto curve.

    UX Design: Implemented Decoupled Interactions using Edit Interactions, allowing users to filter specific supplier lists without losing the global macro-context of the KPIs.

Tech Stack

    Power BI Desktop: Dashboarding & Visualization.

    DAX (Data Analysis Expressions): Complex cumulative totals, running averages, and duplicate detection.

    SQLite: Source data management.

    Power Query (M): ETL, data cleaning, and "Malformed Image" error recovery.
