# 1. შექმენი მონაცემთა ბაზა lesson27_hw
CREATE DATABASE IF NOT EXISTS lesson27_hw;



# 2. მონაცემთა ბაზაში შექმენი ცხრილები შესაბამისი დიზაინითა და მონაცემებით
CREATE TABLE IF NOT EXISTS Migrations(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Distance INT NOT NULL,
    Days INT NOT NULL 
);


INSERT INTO Migrations (ID, Distance, Days)
VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52),
(11737, 1957, 92)
;


CREATE TABLE IF NOT EXISTS Sea_lions(
    ID INT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    species VARCHAR(50) NOT NULL,
    Foreign Key (ID) REFERENCES Migrations(ID)
);

INSERT INTO sea_lions (id, name, species) VALUES
(10484, 'Ayah', 'Zalophus californianus'),
(11728, 'Spot', 'Zalophus californianus'),
(11729, 'Tiger', 'Zalophus californianus'),
(11732, 'Mabel', 'Zalophus californianus'),
(11734, 'Rick', 'Zalophus californianus');



# 3. გამოიყენე ყველა სახის JOIN (JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN) და შეადარე შედეგები ერთმანეთს.
#    FULL JOIN-ში გამოიყენე UNION და UNION ALL

SELECT * FROM Migrations m 
JOIN Sea_lions s
ON m.ID = s.ID;

SELECT * FROM Migrations m 
LEFT JOIN Sea_lions s
ON m.ID = s.ID;

SELECT * FROM Migrations m 
RIGHT JOIN Sea_lions s
ON m.ID = s.ID;

SELECT * FROM Migrations m 
LEFT JOIN Sea_lions s 
ON m.ID = s.ID
UNION
SELECT * FROM Migrations m 
RIGHT JOIN Sea_lions s 
ON m.ID = s.ID;

SELECT * FROM Migrations m 
LEFT JOIN Sea_lions s 
ON m.ID = s.ID
UNION ALL
SELECT * FROM Migrations m 
RIGHT JOIN Sea_lions s 
ON m.ID = s.ID;