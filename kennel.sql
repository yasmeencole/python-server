-- This is a text file to hold the SQL commands to interact with the database.

CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`location_id` INTEGER,
	`customer_id` INTEGER NOT NULL,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);

CREATE TABLE `Customer` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)

);

CREATE TABLE `Location` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL
);

INSERT INTO `Animal` VALUES (null, "Harry", "Pitbull", "Admitted", 1, 4);
INSERT INTO `Animal` VALUES (null, "Jax", "Beagle", "Admitted", 1, 2);
INSERT INTO `Animal` VALUES (null, "Blue", "Siamese", "Admitted", 2, 1);
INSERT INTO `Animal` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);


INSERT INTO `Customer` VALUES (null, "Mary", "201 Created St", "mary@gmail.com", "password");
INSERT INTO `Customer` VALUES (null, "Eve", "500 Internal Error Blvd", "eve@gmail.com", "password");
INSERT INTO `Customer` VALUES (null, "Grey", "301 Redirect Ave", "grey@gmail.com", "password");

INSERT INTO `Employee` VALUES (null, "Kasey", "35498 Madison Ave", 1);
INSERT INTO `Employee` VALUES (null, "Ebony", "100 Main St", 1);
INSERT INTO `Employee` VALUES (null, "Tia", "404 Unknown Ct", 2);

INSERT INTO `Location` VALUES (null, 'Nashville East', "35498 Madison Ave");
INSERT INTO `Location` VALUES (null, 'Nashville South', "101 Penn Ave");
INSERT INTO `Location` VALUES (null, 'Nashville North', "64 Washington Heights");

SELECT
    a.id,
    a.name,
    a.breed,
    a.status,
    a.location_id,
    a.customer_id
FROM animal a
WHERE a.id = 3

SELECT
    c.id,
    c.name,
    c.address,
    c.email,
    c.password
FROM customer c
WHERE c.id = 3

SELECT
    e.id,
    e.name,
    e.address,
    e.email,
    e.password
FROM employee e
WHERE e.id = 3

SELECT
    l.id,
    l.name,
    l.address
FROM location l
WHERE l.id = 3