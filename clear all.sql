-- 1: Disable foreign key check
SET FOREIGN_KEY_CHECKS = 0;

-- 2: Clear child tables first
TRUNCATE TABLE registrations;
TRUNCATE TABLE feedback;

-- 3: Clear parent tables
TRUNCATE TABLE users;
TRUNCATE TABLE events;

-- 4: Reset AUTO_INCREMENT
ALTER TABLE users AUTO_INCREMENT = 1;
ALTER TABLE events AUTO_INCREMENT = 1;
ALTER TABLE registrations AUTO_INCREMENT = 1;
ALTER TABLE feedback AUTO_INCREMENT = 1;

-- 5: Enable foreign key check
SET FOREIGN_KEY_CHECKS = 1;
