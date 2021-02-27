SELECT orderInfo.buyer_id, orderInfo.buy_date, library.book_name, library.price
FROM library 
RIGHT OUTER JOIN orderInfo
ON library.book_id = orderInfo.book_id
WHERE library.book_name = "Looking with Elice"
    OR date(orderInfo.buy_date) BETWEEN "2020-07-27" AND " 2020-07-31"
ORDER BY orderInfo.buy_date ASC
