-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record display: tv_shows.title - rating sum
-- Sorted in descending order by the rating
-- Use only one SELECT statement
SELECT t.title, IFNULL(SUM(r.rate), 0) AS rating
FROM tv_shows AS t
LEFT JOIN tv_show_ratings AS r ON t.id =  r.show_id
GROUP BY t.title
ORDER BY rating DESC;

