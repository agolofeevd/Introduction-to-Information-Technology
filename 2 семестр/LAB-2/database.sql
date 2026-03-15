DROP TABLE IF EXISTS 'shop';
DROP INDEX IF EXISTS 'sqlite_autoindex_shop_1';
DROP TABLE IF EXISTS 'product';
DROP INDEX IF EXISTS 'sqlite_autoindex_product_1';
DROP TABLE IF EXISTS 'warehouse';
DROP INDEX IF EXISTS 'sqlite_autoindex_warehouse_1';
DROP TABLE IF EXISTS 'worker';
CREATE TABLE shop ( 
id INTEGER PRIMARY KEY, 
name VARCHAR(255) UNIQUE, 
balance FLOAT NOT NULL);
INSERT INTO 'shop' VALUES(1,'пятерочка',31);
INSERT INTO 'shop' VALUES(2,'перекресток',133);
null;
CREATE TABLE product ( 
id INTEGER PRIMARY KEY, 
name VARCHAR(255) UNIQUE, 
price FLOAT NOT NULL);
INSERT INTO 'product' VALUES(1,'молоко',100);
INSERT INTO 'product' VALUES(2,'хлеб',25);
null;
CREATE TABLE warehouse ( 
shop_id INTEGER REFERENCES shop (id), 
product_id INTEGER REFERENCES product (id), 
quantity INTEGER NOT NULL, 
PRIMARY KEY (shop_id, product_id));
INSERT INTO 'warehouse' VALUES(1,1,20);
INSERT INTO 'warehouse' VALUES(1,2,10);
INSERT INTO 'warehouse' VALUES(2,1,30);
null;
CREATE TABLE worker ( 
worker_id INTEGER PRIMARY KEY, 
shop_id INTEGER REFERENCES product (id), 
name VARCHAR(255), 
salary INTEGER NOT NULL, 
position VARCHAR(255));
INSERT INTO 'worker' VALUES(1,1,'Иванов Иван',75000,'Продавец-консультант');
INSERT INTO 'worker' VALUES(2,1,'Петрова Мария',82000,'Старший продавец');
INSERT INTO 'worker' VALUES(3,2,'Сидоров Петр',55000,'Продавец');
INSERT INTO 'worker' VALUES(4,2,'Козлова Елена',68000,'Товаровед');
INSERT INTO 'worker' VALUES(5,3,'Николаев Алексей',120000,'Директор магазина');
INSERT INTO 'worker' VALUES(6,3,'Морозова Ольга',62000,'Продавец');
INSERT INTO 'worker' VALUES(7,1,'Волков Денис',48000,'Грузчик');
INSERT INTO 'worker' VALUES(8,2,'Соколова Анна',71000,'Бухгалтер');
INSERT INTO 'worker' VALUES(9,3,'Зайцев Михаил',59000,'Продавец');
INSERT INTO 'worker' VALUES(10,4,'Орлова Татьяна',95000,'Управляющий');
