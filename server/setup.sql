CREATE USER 'communalert'@'localhost' IDENTIFIED BY 'communalert';
CREATE DATABASE communalert;
GRANT ALL ON communalert.* TO 'communalert'@'localhost';
USE communalert;
CREATE TABLE reports
(
report_id int NOT NULL AUTO_INCREMENT,
user_id int NOT NULL,
latitude double NOT NULL,
longitude double NOT NULL,
report_time timestamp DEFAULT CURRENT_TIMESTAMP,
report_type varchar(32) NOT NULL,
PRIMARY KEY(report_id)
);

