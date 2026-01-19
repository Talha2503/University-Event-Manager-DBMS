CREATE DATABASE university_events;
USE university_events;


CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  email VARCHAR(100)
);


CREATE TABLE events (
  event_id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100),
  venue VARCHAR(100),
  event_date DATE
);

CREATE TABLE registrations (
  reg_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  event_id INT,
  reg_date DATE,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id)
);

CREATE TABLE feedback (
  feedback_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  event_id INT,
  rating INT,
  comments TEXT,
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id)
);



