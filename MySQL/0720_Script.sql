use dx0717

-- SELECT는 트랜잭션과 관계 없음
SELECT * FROM DEPT

-- DEPT 테이블에 데이터 1개 삽입: 트랜잭션 생성
INSERT INTO DEPT(DEPTNO,DNAME,LOC) VALUES(60, '회계', '서울');

-- ROLLBACK 수행하여 트랜잭션 시작 전으로 복구
ROLLBACK;

-- DEPT 복사된 DEPTCOPY 생성
CREATE TABLE DEPTCOPY
AS SELECT * FROM DEPT; 


-- DEPT 테이블에 데이터 1개 삽입: 트랜잭션 생성
INSERT INTO DEPT(DEPTNO,DNAME,LOC) VALUES(50, '회계', '서울');

-- ROLLBACK 수행하여 트랜잭션 시작(데이터 삽입) 전으로 복구
ROLLBACK;


COMMIT




-- VIEW
-- 조인으로 인해 많은 데이터 저장 됨
SELECT *
FROM EMP,DEPT
WHERE EMP.DEPTNO =DEPT.DEPTNO AND JOB='CLERK';



-- 인라인 뷰로 미리 필터링하여 메모리 부담 줄일 수 있음
SELECT *
FROM (SELECT * FROM EMP WHERE JOB='CLERK') TEMP ,DEPT
WHERE TEMP.DEPTNO =DEPT.DEPTNO;


-- 일반 VIEW 만들기 
CREATE VIEW SAMPLE
AS
SELECT EMPNO,SAL,ENAME
FROM EMP;

-- VIEW를 테이블처럼 사용 가능
SELECT *
FROM EMP;

-- VIEW에 데이터 삽입
INSERT INTO SAMPLE() VALUES(7777,5000,'EUNHA');

DESC EMP

-- VIEW 구조 확인
DESC SAMPLE

-- 임시 테이블 생상
CREATE TEMPORARY TABLE TEMPTB(
	NAME CHAR(20)
);


-- CTE: SQL 수행 중에만 일시적으로 메모리 공간 할당 받아 사용하는 테이블
-- CTE 구문은 가장 먼저 수행 됨
-- 인라인 뷰로 수행 가능해 보이나, 인라인 뷰는 서브 쿼리보다 늦게 수행되므로 불가능
WITH TEMP AS 
(SELECT NAME, SALARY,SCORE FROM tStaff WHERE DEPART='영업부' AND GENDER='남')

SELECT *
FROM TEMP
WHERE SALARY>=(SELECT AVG(SALARY) FROM TEMP);

SELECT *
FROM usertbl;

-- DELIMITER는 프로시저 종료를 알리기 위한 기호 설정
-- DBeaver에서 수행할때는 SQL 스크립트 실행으로 
DELIMITER //
CREATE PROCEDURE PROC1(USID CHAR(15),
						USERNAME VARCHAR(20),
						BDAY INT(11),
						ADDR CHAR(100),
						PHONE CHAR(11),
						DT DATE)
		BEGIN
			INSERT INTO usertbl
			VALUES(USID,USERNAME, BDAY, ADDR, PHONE,DT);
		END //
DELIMITER ;

DROP PROCEDURE PROC1

CALL PROC1('EUNHA','은하',1016,'서울','240905705','2023-07-20');

SELECT * FROM usertbl


-- trigger 수행 위한 테이블 생성
CREATE TABLE EMP1(
	EMPNO INT PRIMARY KEY,
	ENAME VARCHAR(30) NOT NULL,
	JOB VARCHAR(100)
);

CREATE TABLE SAL1(
	SALNO INT PRIMARY KEY AUTO_INCREMENT,
	SAL FLOAT(7,2),
	EMPNO INT REFERENCES EMP1(EMPNO) ON DELETE CASCADE
);


-- EMP1 테이블에 데이터 추가 할 시 SAL1에도 데이터 자동으로 추가되는 트리거 생성
DELIMITER //
CREATE TRIGGER EMP_SAL_ADD_TRIG
AFTER INSERT ON EMP1
FOR EACH ROW
BEGIN
	INSERT INTO SAL1(SAL,EMPNO) VALUES(100,NEW.EMPNO); -- NEW 또는 OLD 사용 가능
END //
DELIMITER ;

INSERT INTO EMP1 VALUES(1,'EUNHA','STUDENT')


SELECT * FROM SAL1

DROP TRIGGER EMP_SAL_ADD_TRIG


COMMIT

SHOW INDEX FROM tStaff

SELECT * FROM INFORMATION_SCHEMA.INNODB_FT_DEFAULT_STOPWORD





commit

show tables

use dx0717

SELECT * FROM DEPT ;
SELECT * FROM FILETB 


-- 파일 저장 테이블 생성
CREATE TABLE FILETB(
	FILENAME VARCHAR(100),
	FILECONT longblob
);

-- 파이썬 프로젝트에 이미지 파일 추가하기









