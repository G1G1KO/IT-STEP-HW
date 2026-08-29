-- თუ არ გაქვთ შექმნილი, შექმენით მონაცემთა ბაზა სახელად hw_26  და შეასრულეთ შემდეგი დავალებები:
CREATE DATABASE IF NOT EXISTS hw_26;
USE hw_26;

-- 1. დაწერეთ SQL, რომელიც შექმნის Authors ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE TABLE IF NOT EXISTS Authors(
    authorID INT PRIMARY KEY AUTO_INCREMENT,
    authorFirstname VARCHAR(50),
    authorLastname VARCHAR(50)
); 

-- 2. დაწერეთ SQL, რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE TABLE IF NOT EXISTS Books(
    bookID INT PRIMARY KEY AUTO_INCREMENT,
    bookName VARCHAR(50) NOT NULL,
    bookPrice FLOAT NOT NULL,
    authorID INT,
    Foreign Key (authorID) REFERENCES Authors(authorID)
);

-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO Authors (authorFirstname, authorLastname)
VALUES
('Michae', 'Jordan'),
('Lebron', 'James'),
('Cristiano', 'Ronaldo'),
('Blake', 'Griffin'),
('Luka', 'Doncic');

INSERT INTO Books (bookName, bookPrice, authorID)
VALUES
('Echoes', 9.99, 3),
('The Only End', 14.99, 1),
('The Chosen one', 20.00, 5),
('Cooking Fundamentals', 49.00, 4),
('One Love', 4.99, 2);

-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტული ჩანაწერის ერთ-ერთი ველის მნიშვნელობას
UPDATE Books
SET bookPrice = 34.99
WHERE bookName = 'One Love'
;
-- 5. დაწერეთ SQL, რომელიც დაბეჭდავს გაერთიანებულ ცხრილებს
SELECT *
FROM Authors
JOIN Books on Authors.authorID = Books.authorID
;
-- 6. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
DELETE FROM Books;

DELETE FROM Authors

-- 7. წაშალეთ Author და Books ცხრილები
DROP Table Books;

DROP TABLE Authors;