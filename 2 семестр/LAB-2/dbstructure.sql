CREATE TABLE shop ( 
id INTEGER PRIMARY KEY, 
name VARCHAR(255) UNIQUE, 
balance FLOAT NOT NULL);
null;
CREATE TABLE product ( 
id INTEGER PRIMARY KEY, 
name VARCHAR(255) UNIQUE, 
price FLOAT NOT NULL);
null;
CREATE TABLE warehouse ( 
shop_id INTEGER REFERENCES shop (id), 
product_id INTEGER REFERENCES product (id), 
quantity INTEGER NOT NULL, 
PRIMARY KEY (shop_id, product_id));
null;
CREATE TABLE worker ( 
worker_id INTEGER PRIMARY KEY, 
shop_id INTEGER REFERENCES product (id), 
name VARCHAR(255), 
salary INTEGER NOT NULL, 
position VARCHAR(255));
