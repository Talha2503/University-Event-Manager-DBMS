-- Events
INSERT INTO events(title, venue, event_date) VALUES
('AI Seminar', 'Auditorium 1', '2026-01-20'),
('Coding Workshop', 'Lab 3', '2026-01-25'),
('Tech Talk', 'Auditorium 2', '2026-02-01'),
('Hackathon', 'Lab 5', '2026-02-10');

-- Users
INSERT INTO users(name, email) VALUES
('M Usman', 'usman@gmail.com'),
('Talha Bhutto', 'talha@gmail.com'),
('Abdul Samad', 'absamad@yahoo.com'),
('Faisal Haroon', 'faisal@gmail.com');


-- Registrations
INSERT INTO registrations(user_id, event_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(1, 4),
(2, 4);

-- Feedback
INSERT INTO feedback(user_id, event_id, rating, comments) VALUES
(1, 1, 5, 'Amazing seminar!'),
(2, 1, 4, 'Very informative.'),
(3, 2, 5, 'Loved the coding workshop.'),
(4, 3, 3, 'Could be better.'),
(1, 4, 4, 'Fun hackathon!'),
(2, 4, 5, 'Excellent organization.');
