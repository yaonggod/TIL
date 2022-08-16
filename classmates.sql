-- column 정보 표시
sqlite> .headers on

-- 표처럼 보이는 기능
sqlite> .mode column

-- 테이블 생성
-- NOT NULL은 값이 꼭 존재해야함
CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 테이블에 하나의 행 삽입하기
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '대전');

-- 테이블에 여러 행 삽입하기
INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

-- 테이블 목록 조회
.tables

-- 테이블 스키마 조회
.schema classmates

-- SELECT : 특정 테이블의 레코드(행) 정보 반환, rowid는 PK 없는 경우 자동으로 생성되는 PK
SELECT * FROM classmates;
SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   23   대전
-- 2      홍길동   30   서울
-- 3      김철수   30   제주
-- 4      이호영   26   인천
-- 5      박민희   29   대구
-- 6      최혜영   28   전주

-- 테이블 삭제
DROP TABLE classmates

-- 특정 컬럼만 보이기
SELECT rowid, age FROM classmates;
-- rowid  age
-- -----  ---
-- 1      23
-- 2      30
-- 3      30
-- 4      26
-- 5      29
-- 6      28

-- 상위 몇 개만 보여주기
SELECT rowid, * FROM classmates LIMIT 2;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   23   대전
-- 2      홍길동   30   서울

-- LIMIT 4 OFFSET 1 = 2번째 행부터 4개 행을 출력
SELECT rowid, * FROM classmates LIMIT 4 OFFSET 1;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 2      홍길동   30   서울
-- 3      김철수   30   제주
-- 4      이호영   26   인천
-- 5      박민희   29   대구

-- 조건에 해당하는 행만 출력
SELECT rowid, * FROM classmates WHERE age >= 30;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 2      홍길동   30   서울
-- 3      김철수   30   제주

-- 조건에 해당하는 행의 개수를 세기
SELECT COUNT (*) FROM classmates WHERE age >= 30;
-- COUNT (*)
-- ---------
-- 2

-- 조회 결과에서 중복 행을 제거
SELECT DISTINCT name FROM classmates;
-- name
-- ----
-- 홍길동
-- 김철수
-- 이호영
-- 박민희
-- 최혜영

-- 수정
UPDATE classmates SET age = 60 WHERE rowid = 1;
SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   60   대전
-- 2      홍길동   30   서울
-- 3      김철수   30   제주
-- 4      이호영   26   인천
-- 5      박민희   29   대구
-- 6      최혜영   28   전주

-- 삭제 -> 기존 rowid 그대로 보존
DELETE FROM classmates WHERE rowid = 3;
SELECT rowid, * FROM classmates;
-- rowid  name  age  address
-- -----  ----  ---  -------
-- 1      홍길동   60   대전
-- 2      홍길동   30   서울
-- 4      이호영   26   인천
-- 5      박민희   29   대구
-- 6      최혜영   28   전주