/*
Question 1: Total Orders Per Customer

Write a query to display the total number of orders placed by each customer, 
along with their name and the date they joined. Sort the results by the total number of orders in descending order.
*/

SELECT
COUNT(order_id) AS "Orders",
customers.customer_id AS "Customer ID",
customer_name AS "Name",
join_date AS "Date of join"
FROM orders
JOIN customers ON orders.customer_id=customers.customer_id
GROUP BY customers.customer_id
ORDER BY COUNT(order_id) DESC;


/*
Question 2: Rank Customers by Spending

For each customer, calculate their total spending (sum of the total amounts from the `Orders` table) 
and rank them by total spending within their respective country. 
Use a **window function** to rank the customers.
*/


SELECT
RANK() OVER(PARTITION BY country ORDER BY SUM(orderitems.price*orderitems.quantity) DESC) AS "Rank",
customer_name AS "Name",
SUM(orderitems.price*orderitems.quantity) AS "Spending",
country AS "Country"
FROM orders
JOIN customers ON orders.customer_id=customers.customer_id
JOIN orderitems ON orders.order_id=orderitems.order_id
GROUP BY customers.customer_id, country
ORDER BY SUM(orderitems.price*orderitems.quantity) DESC;