--SELECT NAME
--FROM SYS.TABLES

--SELECT *
--FROM DBO.PRODUCTS;

-- CATEGORIZING THE PRODUCTS INTO PRICE CATEGORIES: LOW, MEDIUM, OR HIGH

SELECT *,
    CASE
        WHEN Price < 50 THEN 'Low'  -- If the price is less than 50, categorize as 'Low'
        WHEN Price BETWEEN 50 AND 200 THEN 'Medium'  -- If the price is between 50 and 200 (inclusive), categorize as 'Medium'
        ELSE 'High'  -- If the price is greater than 200, categorize as 'High'
    END AS PriceCategory  -- Names the new column as PriceCategory

FROM 
    dbo.products;