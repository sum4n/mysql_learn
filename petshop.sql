DROP DATABASE IF EXISTS sql_pet_shop;
CREATE DATABASE sql_pet_shop;
USE sql_pet_shop;

CREATE TABLE pet_type(
	pet_type_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pet_type_name CHAR(3) NOT NULL
    );
INSERT INTO pet_type VALUES(NULL, 'Dog');
INSERT INTO pet_type VALUES(NULL, 'Cat');

CREATE TABLE pet_subtype(
	pet_subtype_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pet_type_id INT UNSIGNED NOT NULL,
    pet_subtype_name VARCHAR(30) NOT NULL
    );
INSERT INTO pet_subtype VALUES(NULL, 1, 'American Bulldog');
INSERT INTO pet_subtype VALUES(NULL, 1, 'Bernedoodle');
INSERT INTO pet_subtype VALUES(NULL, 1, 'Chihuahua');
INSERT INTO pet_subtype VALUES(NULL, 2, 'Abyssinian');
INSERT INTO pet_subtype VALUES(NULL, 2, 'Birman');
INSERT INTO pet_subtype VALUES(NULL, 2, 'Ragdoll');
INSERT INTO pet_subtype VALUES(NULL, 1, 'Boerboel');
INSERT INTO pet_subtype VALUES(NULL, 1, 'Cursinu');
INSERT INTO pet_subtype VALUES(NULL, 2, 'Savanna');
INSERT INTO pet_subtype VALUES(NULL, 1, 'Shikoku');
 
CREATE TABLE pet_inventory(
	pet_inventory_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pet_type_id INT UNSIGNED NOT NULL,
    pet_subtype_id INT UNSIGNED NOT NULL,
    num_in_stock INT UNSIGNED NOT NULL,
    num_sold INT UNSIGNED,
    current_price_USD FLOAT UNSIGNED NOT NULL
    );
INSERT INTO pet_inventory VALUES(NULL, 1, 1, 12, 5, 34);
INSERT INTO pet_inventory VALUES(NULL, 1, 2, 5, 3, 36);
INSERT INTO pet_inventory VALUES(NULL, 1, 3, 5, 5, 33);
INSERT INTO pet_inventory VALUES(NULL, 2, 4, 11, 3, 20);
INSERT INTO pet_inventory VALUES(NULL, 2, 5, 5, 1, 18);
INSERT INTO pet_inventory VALUES(NULL, 2, 6, 4, 2, 23);
INSERT INTO pet_inventory VALUES(NULL, 1, 7, 10, 8, 28);
INSERT INTO pet_inventory VALUES(NULL, 1, 8, 12, 4, 38);
INSERT INTO pet_inventory VALUES(NULL, 2, 9, 11, 8, 14);
INSERT INTO pet_inventory VALUES(NULL, 1, 10, 14, 3, 22);
 
 
CREATE TABLE transactions(
	transaction_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(30) NOT NULL,
    pet_type_id INT UNSIGNED NOT NULL,
    pet_subtype_id INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    total_price FLOAT UNSIGNED NOT NULL,
    transaction_date DATE NOT NULL
    );
INSERT INTO transactions VALUES(NULL, 'Carol Hogan', 2, 4, 1, 20, '2018-02-09');
INSERT INTO transactions VALUES(NULL, 'Marry Allen', 2, 6, 2, 46, '2018-05-18');
INSERT INTO transactions VALUES(NULL, 'Sandra Sanford', 1, 10, 1, 22, '2019-01-19');
INSERT INTO transactions VALUES(NULL, 'Miles Lexie', 1, 8, 2, 76, '2019-01-26');
INSERT INTO transactions VALUES(NULL, 'Linda Richmond', 2, 6, 3, 69, '2019-02-10');