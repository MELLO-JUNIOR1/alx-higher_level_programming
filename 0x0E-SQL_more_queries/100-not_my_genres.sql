-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record display: tv_genres.name
-- Sorted in ascending order by the genre name
-- Use a maximum of two SELECT statement
SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER"
)
ORDER BY tv_genres.name;
