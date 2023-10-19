-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Eaach record display: tv_genres.name - rating sum
-- Sorted in descending order by their rating
-- Use only one SELECT statement
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS tvg
       INNER JOIN `tv_show_genres` AS tvs
       ON tvs.`genre_id` = tvg.`id`

       INNER JOIN `tv_show_ratings` AS tvr
       ON tvr.`show_id` = tvs.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
