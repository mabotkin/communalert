CREATE DATABASE communalert;
CREATE TABLE
(
report_id int NOT NULL AUTO_INCREMENT,
user_id int NOT NULL,
latitude double NOT NULL,
longitude double NOT NULL,
report_time datetime NOT NULL,
report_type varchar(32) NOT NULL,
PRIMARY KEY(report_id)
);

