-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record display: tv_shows.title
-- Sorted in ascending order by the show title
-- Use a maximum of two SELECT statement
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
    JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy"
)
ORDER BY tv_shows.title;

