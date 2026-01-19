-- Dashboard Queries

SELECT COUNT(*) FROM events;
SELECT COUNT(*) FROM users;

-- upcoming events
SELECT COUNT(*) FROM events WHERE event_date > CURDATE();

-- completed events
SELECT COUNT(*) FROM events WHERE event_date < CURDATE();


-- event status list ..Har event ko status assign karta hai:
SELECT title,
CASE
    WHEN event_date > CURDATE() THEN 'Upcoming'
    WHEN event_date = CURDATE() THEN 'Ongoing'
    ELSE 'Completed'
END AS status
FROM events
ORDER BY event_date;


-- top rated event graph
SELECT e.title, ROUND(AVG(f.rating),2)
FROM feedback f
JOIN events e ON f.event_id = e.event_id
GROUP BY e.title
ORDER BY AVG(f.rating) DESC;
-- -------------------------------------------------------


-- EVENTS MODULE QUERIES

-- load all events
SELECT * FROM events ORDER BY event_date;

-- search event
SELECT * FROM events
WHERE title LIKE %s OR venue LIKE %s
ORDER BY event_date;


-- sort by venue
SELECT * FROM events ORDER BY venue;


-- add event
INSERT INTO events(title, venue, event_date)
VALUES (%s, %s, %s);


-- update events
UPDATE events
SET title=%s, venue=%s, event_date=%s
WHERE event_id=%s;

-- delete events
DELETE FROM events WHERE event_id=%s;

-- -------------------------------------------------------

-- FEEDBACK MODULE QUERIES

-- submit feedback
INSERT INTO feedback(user_id, event_id, rating, comments)
VALUES (%s,%s,%s,%s);

-- view feedback
SELECT e.title, f.rating, f.comments, f.user_id
FROM feedback f
JOIN events e ON f.event_id = e.event_id
ORDER BY e.event_date DESC;


-- ave rating per event
SELECT e.title, ROUND(AVG(f.rating),2)
FROM feedback f
JOIN events e ON f.event_id = e.event_id
GROUP BY e.title
ORDER BY 2 DESC;

-- -------------------------------------------------------

-- USERS MODULE QUERIES


-- load  user
SELECT * FROM users ORDER BY user_id;

-- add user
INSERT INTO users(name,email) VALUES (%s,%s);

-- update user
UPDATE users
SET name=%s, email=%s
WHERE user_id=%s;

-- delete user
DELETE FROM users WHERE user_id=%s;

-- register user
INSERT INTO registrations(user_id,event_id)
VALUES (%s,%s);

-- -------------------------------------------------------

