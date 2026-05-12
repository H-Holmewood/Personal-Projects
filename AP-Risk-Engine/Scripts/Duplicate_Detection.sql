WITH CleanInvoices AS (
    SELECT SupplierID,
        InvoiceNumber,
        UPPER(
            REPLACE(
                REPLACE(REPLACE(InvoiceNumber, '-', ''), '.', ''),
                ' ',
                ''
            )
        ) AS NormalizedInv,
        Amount,
        Date
    FROM Raw_Invoices
)
SELECT c1.SupplierID,
    c1.InvoiceNumber AS Duplicate_A,
    c2.InvoiceNumber AS Duplicate_B,
    c1.Amount,
    c1.Date
FROM CleanInvoices c1
    JOIN CleanInvoices c2 ON c1.NormalizedInv = c2.NormalizedInv
    AND c1.SupplierID = c2.SupplierID
    AND c1.InvoiceNumber < c2.InvoiceNumber
ORDER BY c1.Date DESC;
ALTER TABLE Raw_Invoices
ADD COLUMN ApprovalDate DATE;
UPDATE Raw_Invoices
SET ApprovalDate = DATE(Date, '+2 days')
WHERE InvoiceID % 3 = 0;
-- Fast approvals
UPDATE Raw_Invoices
SET ApprovalDate = DATE(Date, '+14 days')
WHERE InvoiceID % 3 = 1;