CREATE DATABASE flaskdb;
USE flaskdb;

CREATE TABLE book_tbl (
id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(100) NOT NULL,
author VARCHAR(50) NOT NULL,
publisher VARCHAR(50) NOT NULL,
price INT NOT NULL,
stock INT NOT NULL
);

INSERT INTO book_tbl (title, author, publisher, price, stock) 
VALUES
('빅데이터의 기술과 활용', '김철수', '테크출판사', 15000, 10),
('파이썬 프로그래밍', '박영민', '코딩출판사', 23000, 20),
('인공지능 개론', '이영희', '미래출판사', 32000, 5),
('데이터베이스 기초', '최지수', '데이터출판사', 26000, 15),
('컴퓨터 구조와 원리', '장예린', '하드웨어출판사', 28000, 8),
('자바 웹 프로그래밍', '윤성환', '웹출판사', 33000, 12),
('리눅스 서버 관리', '송태현', '서버출판사', 27000, 7),
('알고리즘 문제해결 전략', '이수진', '프로그래밍출판사', 35000, 5),
('머신러닝 입문', '강민준', 'AI출판사', 30000, 10),
('자료구조와 함께하는 코딩', '김지은', '학습출판사', 29000, 20);