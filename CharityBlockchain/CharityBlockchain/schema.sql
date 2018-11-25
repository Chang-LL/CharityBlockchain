DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS fund;
DROP TABLE IF EXISTS deal;
DROP TABLE IF EXISTS project;
CREATE TABLE user(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	BlockId INT,
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	email TEXT,
	phone INT,
	account float,
	account_type INT 
	);
-- test user
INSERT INTO user (username,password,account_type,account) 
	VALUES('0234','pbkdf2:sha256:50000$ToX9F3JM$b6f046592e879e5fb9392093342e71058c43c5b85d17c60588d5de7be9f95f75',0,10000);
INSERT INTO user (username,password,account_type) 
	VALUES('1234','pbkdf2:sha256:50000$ToX9F3JM$b6f046592e879e5fb9392093342e71058c43c5b85d17c60588d5de7be9f95f75',1);
INSERT INTO user (username,password,account_type) 
	VALUES('2234','pbkdf2:sha256:50000$ToX9F3JM$b6f046592e879e5fb9392093342e71058c43c5b85d17c60588d5de7be9f95f75',2);
INSERT INTO user (username,password,account_type) 
	VALUES('3234','pbkdf2:sha256:50000$ToX9F3JM$b6f046592e879e5fb9392093342e71058c43c5b85d17c60588d5de7be9f95f75',3);
INSERT INTO user (username,password,account_type) 
	VALUES('finish','pbkdf2:sha256:50000$ToX9F3JM$b6f046592e879e5fb9392093342e71058c43c5b85d17c60588d5de7be9f95f75',3);
			
CREATE TABLE deal(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	from_id INT,
	to_id INT ,
	project_id INT,
	account FLOAT,
	hash TEXT,
	tranDate DATE,
    foreign key(from_id) REFERENCES user(id), 
    foreign key(to_id) REFERENCES user(id),
	foreign key(project_id) REFERENCES project(id)
	);

CREATE TABLE project(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	now_money float,
	want_money float,
	createDate DATE,
	info TEXT
	);
insert into project(name,now_money,createDate,info)
	values ('mainFound',0,DATE(),'Project A,100 books');
insert into project(name,now_money,createDate,info)
	values ('aFound',0,DATE(),'Project B,100 desks');
insert into project(name,now_money,createDate,info)
	values ('cFound',0,DATE(),'Project C,100 chairs');
	insert into project(name,now_money,createDate,info)
	values ('dFound',0,DATE(),'Project D,100 computers');