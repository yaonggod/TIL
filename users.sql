-- 테이블 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터 추가
.mode csv

-- csv파일을 user테이블로
.import users.csv users

.headers on
.mode column

-- 잔고가 50만 이상인 사람들
SELECT last_name, first_name, balance FROM users WHERE balance >= 500000;
-- 잔고가 50만 이상인 사람들 10명만
SELECT last_name, first_name, balance FROM users WHERE balance >= 500000 LIMIT 10;
-- 잔고가 50만 이상이고 성이 이씨인 사람
SELECT last_name, first_name, balance FROM users WHERE balance >= 500000 AND last_name = '이';

-- 성이 이씨이고 잔고가 50만 이상인 사람의 수
SELECT COUNT(*) FROM users WHERE balance >= 500000 AND last_name = '이';
-- 전체 중에 가장 어린 사람의 나이
SELECT MIN(age) FROM users;
-- 잔고가 50만 이상인 사람 중 가장 어린 사람의 나이
SELECT MIN(age) FROM users WHERE balance >= 500000;
-- 경기도 사람 중 가장 나이가 많은 사람의 이름과 나이
SELECT MAX(age), last_name, first_name FROM users WHERE country = '경기도';
-- 경기도 사람의 평균 잔액
SELECT AVG(balance) FROM users WHERE country = '경기도';

-- 지역번호가 031인 사람의 수
SELECT COUNT(*) FROM users WHERE phone LIKE '031-%';
-- 용으로 끝나는 사람
SELECT COUNT(*) FROM users WHERE first_name LIKE '%용';
-- 전화번호가 0으로 끝나는 사람
SELECT COUNT(*) FROM users WHERE phone LIKE '%0';

-- 계좌 잔액 하위 10명
SELECT last_name, first_name, balance FROM users ORDER BY balance ASC LIMIT 10;
-- 계좌 잔액 상위 10명을 나이가 많은 순으로 보여줌
SELECT last_name, first_name, balance, age FROM users ORDER BY balance DESC, age DESC LIMIT 10;
-- 나이 상위 10명을 계좌 잔액이 많은 순으로 보여줌
SELECT last_name, first_name, balance, age FROM users ORDER BY age DESC, balance DESC LIMIT 10;