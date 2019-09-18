DROP DATABASE IF EXISTS my_petshop_gui2;
CREATE DATABASE my_petshop_gui2;
USE my_petshop_gui2;

CREATE TABLE pet_info(
	pet_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pet_type VARCHAR(20) NOT NULL,
    pet_subtype VARCHAR(30) NOT NULL,
    num_in_stock INT UNSIGNED,
    num_sold INT UNSIGNED,
    price FLOAT UNSIGNED
    );

INSERT INTO pet_info VALUES(NULL, "Dog", "American Bulldog", 5, 1, 34.99);
INSERT INTO pet_info VALUES(NULL, "Dog", "Bernedoodle", 4, 0, 31.99);
INSERT INTO pet_info VALUES(NULL, "Cat", "Abyssinian", 6, 3, 22.99);
INSERT INTO pet_info VALUES(NULL, "Cat", "Birman", 7, 2, 19.99);
INSERT INTO pet_info VALUES(NULL, "Dog", "Boerboel", 8, 7, 33.99);


CREATE TABLE transaction_info(
	tran_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	tran_date DATE NOT NULL,
	customer_name VARCHAR(40) NOT NULL,
	pet_id INT UNSIGNED NOT NULL,
	quantity INT UNSIGNED NOT NULL,
	total_price FLOAT UNSIGNED NOT NULL
	);
    
INSERT INTO transaction_info VALUES(NULL, "2018-02-10", "Jessica Davis", 1, 1, 68);
INSERT INTO transaction_info VALUES(NULL, "2018-02-11", "Megan Rodriguez", 5, 2, 67);
INSERT INTO transaction_info VALUES(NULL, "2018-02-12", "Ellie Miller", 3, 1, 43);
INSERT INTO transaction_info VALUES(NULL, "2018-02-13", "Charlotte Smith", 2, 2, 60);
INSERT INTO transaction_info VALUES(NULL, "2018-02-11", "Chloe Jones", 4, 1, 64);
INSERT INTO transaction_info VALUES(NULL, "2018-02-12", "Olivia Johnson", 2, 2, 29);
    
