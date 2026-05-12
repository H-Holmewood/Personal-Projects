SELECT date,
    regionname,
    flatprice,
    AVG(flatprice) OVER (
        PARTITION BY regionname
        ORDER BY date ROWS BETWEEN 11 PRECEDING AND CURRENT ROW
    ) AS rrolling_12pt_avg
FROM property_prices
WHERE regionname = 'Leicester'
ORDER BY date DESC;
SELECT STRFTIME('%Y', date) AS Year,
    AVG(flatprice) AS Avg_Annual_Flat_Price
FROM property_prices
GROUP BY Year,
    regionname
ORDER BY Year ASC;