/*
Enter your query below.
Please append a semicolon ";" at the end of the query
cutomer중 invoice에 없는 사람, product중 invoice_item에 없는 물건들을 합쳐서 보여주시오.
*/

SELECT "customer" AS category, c.id, c.customer_name
FROM customer AS c
LEFT JOIN invoice AS i
ON c.id = i.customer_id
WHERE i.id is NULL
UNION
SELECT "product" AS category, p.id, p.product_name
FROM product AS p
LEFT JOIN invoice_item AS i
ON p.id = i.product_id
WHERE i.id is NULL;


/*
후기

*/