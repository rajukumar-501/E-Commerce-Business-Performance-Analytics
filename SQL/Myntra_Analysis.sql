SELECT COUNT(*) AS Total_Rows
FROM Myntra;


SELECT
    Order_ID,
    COUNT(*) AS Order_Count
FROM Myntra
GROUP BY Order_ID
HAVING COUNT(*) > 1;


SELECT
    SUM(CASE WHEN Order_ID IS NULL THEN 1 ELSE 0 END) AS Missing_Order_ID,
    SUM(CASE WHEN Order_Date IS NULL THEN 1 ELSE 0 END) AS Missing_Order_Date,
    SUM(CASE WHEN Category IS NULL THEN 1 ELSE 0 END) AS Missing_Category,
    SUM(CASE WHEN Brand IS NULL THEN 1 ELSE 0 END) AS Missing_Brand,
    SUM(CASE WHEN Product IS NULL THEN 1 ELSE 0 END) AS Missing_Product,
    SUM(CASE WHEN Revenue IS NULL THEN 1 ELSE 0 END) AS Missing_Revenue
FROM Myntra;


SELECT
    SUM(Revenue) AS Total_Revenue
FROM Myntra;


SELECT
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM Myntra;


SELECT
    SUM(Quantity) AS Total_Units_Sold
FROM Myntra;


SELECT
    ROUND(AVG(Rating), 2) AS Average_Rating
FROM Myntra;


SELECT
    SUM(Refund_Amount) AS Total_Refund
FROM Myntra;


SELECT
    SUM(Net_Revenue) AS Net_Revenue
FROM Myntra;


SELECT
    Category,
    SUM(Revenue) AS Revenue,
    SUM(Quantity) AS Units_Sold,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(AVG(Rating), 2) AS Average_Rating
FROM Myntra
GROUP BY Category
ORDER BY Revenue DESC;



SELECT
    Brand,
    SUM(Revenue) AS Revenue,
    SUM(Quantity) AS Units_Sold,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(AVG(Rating), 2) AS Average_Rating
FROM Myntra
GROUP BY Brand
ORDER BY Revenue DESC;


SELECT TOP 10
    Brand,
    SUM(Revenue) AS Revenue
FROM Myntra
GROUP BY Brand
ORDER BY Revenue DESC;


SELECT TOP 10
    Product,
    SUM(Quantity) AS Units_Sold,
    SUM(Revenue) AS Revenue,
    ROUND(AVG(Rating), 2) AS Average_Rating
FROM Myntra
GROUP BY Product
ORDER BY Revenue DESC;


SELECT
    Year,
    Month_Number,
    Month,
    SUM(Revenue) AS Revenue
FROM Myntra
GROUP BY
    Year,
    Month_Number,
    Month
ORDER BY
    Year,
    Month_Number;



SELECT
    Category,
    ROUND(AVG(Discount_Percent), 2) AS Average_Discount,
    SUM(Discount_Amount) AS Total_Discount,
    SUM(Revenue) AS Revenue
FROM Myntra
GROUP BY Category
ORDER BY Revenue DESC;



SELECT
    City,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Units_Sold,
    SUM(Revenue) AS Revenue
FROM Myntra
GROUP BY City
ORDER BY Revenue DESC;



SELECT
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Revenue) AS Revenue
FROM Myntra
GROUP BY Payment_Method
ORDER BY Revenue DESC;



SELECT
    Gender,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Quantity) AS Units_Sold,
    SUM(Revenue) AS Revenue,
    ROUND(AVG(Rating), 2) AS Average_Rating
FROM Myntra
GROUP BY Gender
ORDER BY Revenue DESC;



SELECT
    Order_Status,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Revenue) AS Revenue
FROM Myntra
GROUP BY Order_Status
ORDER BY Total_Orders DESC;


SELECT
    ROUND(
        SUM(Revenue) /
        NULLIF(COUNT(DISTINCT Order_ID), 0),
        2
    ) AS Average_Order_Value
FROM Myntra;