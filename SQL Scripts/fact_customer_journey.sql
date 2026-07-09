--SELECT * FROM dbo.customer_journey

-- Common Table Expression (CTE) to identify and tag duplicate records
WITH DuplicateRecords AS (
    SELECT 
        JourneyID,  
        CustomerID,  
        ProductID, 
        VisitDate,  
        Stage,  
        Action,  
        Duration,
        ROW_NUMBER() OVER(PARTITION BY CustomerID,ProductID,VisitDate, Stage, Action ORDER BY JourneyID) AS row_num
     FROM 
        dbo.customer_journey  
)

SELECT *
FROM DuplicateRecords
ORDER BY JourneyID

SELECT 
 JourneyID,  
    CustomerID,  
    ProductID,  
    VisitDate, 
    Stage,  
    Action,
    COALESCE(Duration, avg_duration) AS Duration  -- Replaces missing durations with the average duration for the corresponding date
  FROM 
    (SELECT JourneyID,  
            CustomerID,  
            ProductID, 
            VisitDate,  
            UPPER(Stage) AS Stage,  
            Action,  
            Duration,
            AVG(Duration) OVER(PARTITION BY VisitDate) AS avg_duration,
            ROW_NUMBER()  OVER(PARTITION BY CustomerID, ProductID, VisitDate, UPPER(Stage), Action ORDER BY JourneyID) As rn -- Assigns a row number to each row within the partition to identify duplicates
    FROM 
        dbo.customer_journey)t
    WHERE rn=1;-- Keeps only the first occurrence of each duplicate group identified in the subquery



