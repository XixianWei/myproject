-- Section 4: SQL Challenge [25 marks]

-- 4.1 Write (and execute) syntax to create the following tables:
CREATE TABLE movie_info (
    Movie_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(255),
    Movie_Length TIME,
    Age_Rating VARCHAR(10)
);
CREATE TABLE screens (
    Screen_ID INT PRIMARY KEY,
    Four_K BOOLEAN
);
CREATE TABLE showings (
    Showing_ID INT PRIMARY KEY,
    Movie_ID INT,
    Screen_ID INT,
    Start_Time TIME,
    Available_Seats INT,
    FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
    FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

-- 4.2 Write a query to return the name and time of all movies 
-- that play after 12:00 given there is at least 1 available seat. 
-- Display the results in time order.
SELECT movie_info.movie_name, showings.start_time
FROM movie_info
JOIN showings ON movie_info.movie_ID = showings.movie_ID
WHERE showings.start_time > '12:00:00' AND showings.available_seats > 0
ORDER BY showings.start_time;

-- 4.3 Return the name of the movie with the most showings.
SELECT movie_info.movie_name
FROM movie_info
JOIN showings ON movie_info.movie_ID = showings.movie_ID
GROUP BY movie_info.movie_name
ORDER BY COUNT(showings.showing_ID) DESC
LIMIT 1;

