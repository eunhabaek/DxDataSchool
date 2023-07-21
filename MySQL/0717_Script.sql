-- db 목록 확인 --
show databases;

-- db 생성 --
create database dx0717;

-- db 삭제 --
DROP database dx0717;

-- db 사용 선택 --
use dx0717;

-- 샘플데이터 만들기--
CREATE TABLE tCity
(
	name CHAR(10) PRIMARY KEY,
	area INT NULL ,
	popu INT NULL ,
	metro CHAR(1) NOT NULL,
	region CHAR(6) NOT NULL
);

INSERT INTO tCity VALUES ('서울',605,974,'y','경기');
INSERT INTO tCity VALUES ('부산',765,342,'y','경상');
INSERT INTO tCity VALUES ('오산',42,21,'n','경기');
INSERT INTO tCity VALUES ('청주',940,83,'n','충청');
INSERT INTO tCity VALUES ('전주',205,65,'n','전라');
INSERT INTO tCity VALUES ('순천',910,27,'n','전라');
INSERT INTO tCity VALUES ('춘천',1116,27,'n','강원');
INSERT INTO tCity VALUES ('홍천',1819,7,'n','강원');

SELECT * FROM tCity;

CREATE TABLE tStaff
(
	name CHAR (15) PRIMARY KEY,
	depart CHAR (10) NOT NULL,
	gender CHAR(3) NOT NULL,
	joindate DATE NOT NULL,
	grade CHAR(10) NOT NULL,
	salary INT NOT NULL,
	score DECIMAL(5,2) NULL
);

INSERT INTO tStaff VALUES ('김유신','총무부','남','2000-2-3','이사',420,88.8);
INSERT INTO tStaff VALUES ('유관순','영업부','여','2009-3-1','과장',380,NULL);
INSERT INTO tStaff VALUES ('안중근','인사과','남','2012-5-5','대리',256,76.5);
INSERT INTO tStaff VALUES ('윤봉길','영업부','남','2015-8-15','과장',350,71.25);
INSERT INTO tStaff VALUES ('강감찬','영업부','남','2018-10-9','사원',320,56.0);
INSERT INTO tStaff VALUES ('정몽주','총무부','남','2010-9-16','대리',370,89.5);
INSERT INTO tStaff VALUES ('허난설헌','인사과','여','2020-1-5','사원',285,44.5);
INSERT INTO tStaff VALUES ('신사임당','영업부','여','2013-6-19','부장',400,92.0);
INSERT INTO tStaff VALUES ('성삼문','영업부','남','2014-6-8','대리',285,87.75);
INSERT INTO tStaff VALUES ('논개','인사과','여','2010-9-16','대리',340,46.2);
INSERT INTO tStaff VALUES ('황진이','인사과','여','2012-5-5','사원',275,52.5);
INSERT INTO tStaff VALUES ('이율곡','총무부','남','2016-3-8','과장',385,65.4);
INSERT INTO tStaff VALUES ('이사부','총무부','남','2000-2-3','대리',375,50);
INSERT INTO tStaff VALUES ('안창호','영업부','남','2015-8-15','사원',370,74.2);
INSERT INTO tStaff VALUES ('을지문덕','영업부','남','2019-6-29','사원',330,NULL);
INSERT INTO tStaff VALUES ('정약용','총무부','남','2020-3-14','과장',380,69.8);
INSERT INTO tStaff VALUES ('홍길동','인사과','남','2019-8-8','차장',380,77.7);
INSERT INTO tStaff VALUES ('대조영','총무부','남','2020-7-7','차장',290,49.9);
INSERT INTO tStaff VALUES ('장보고','인사과','남','2005-4-1','부장',440,58.3);
INSERT INTO tStaff VALUES ('선덕여왕','인사과','여','2017-8-3','사원',315,45.1);

SELECT * FROM tStaff;

DESC tStaff;

DESC tCity;

CREATE TABLE DEPT(
	DEPTNO INT(2),
	DNAME VARCHAR(14) ,
	LOC VARCHAR(13),
	CONSTRAINT PK_DEPT PRIMARY KEY(DEPTNO)
);


CREATE TABLE EMP(
	EMPNO INT(4),
	ENAME VARCHAR(10),
	JOB VARCHAR(9),
	MGR INT(4),
	HIREDATE DATE,
	SAL FLOAT(7,2),
	COMM FLOAT(7,2),
	DEPTNO INT(2),
	CONSTRAINT PK_EMP PRIMARY KEY(EMPNO),
	CONSTRAINT FK_DEPTNO FOREIGN KEY(DEPTNO) REFERENCES DEPT(DEPTNO)
);

INSERT INTO DEPT VALUES(10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES(30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES(40,'OPERATIONS','BOSTON');

INSERT INTO EMP VALUES
(7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20);
INSERT INTO EMP VALUES
(7499,'ALLEN','SALESMAN',7698,'1981-2-20',1600,300,30);
INSERT INTO EMP VALUES
(7521,'WARD','SALESMAN',7698,'1981-2-22',1250,500,30);
INSERT INTO EMP VALUES
(7566,'JONES','MANAGER',7839,'1981-4-2',2975,NULL,20);
INSERT INTO EMP VALUES
(7654,'MARTIN','SALESMAN',7698,'1981-9-28',1250,1400,30);
INSERT INTO EMP VALUES
(7698,'BLAKE','MANAGER',7839,'1981-5-1',2850,NULL,30);
INSERT INTO EMP VALUES
(7782,'CLARK','MANAGER',7839,'1981-6-9',2450,NULL,10);
INSERT INTO EMP VALUES
(7788,'SCOTT','ANALYST',7566,'1987-7-13',3000,NULL,20);
INSERT INTO EMP VALUES
(7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,10);
INSERT INTO EMP VALUES
(7844,'TURNER','SALESMAN',7698,'1981-9-8',1500,0,30);
INSERT INTO EMP VALUES
(7876,'ADAMS','CLERK',7788,'1987-7-13',1100,NULL,20);
INSERT INTO EMP VALUES
(7900,'JAMES','CLERK',7698,'1981-12-3',950,NULL,30);
INSERT INTO EMP VALUES
(7902,'FORD','ANALYST',7566,'1981-12-3',3000,NULL,20);
INSERT INTO EMP VALUES
(7934,'MILLER','CLERK',7782,'1982-1-23',1300,NULL,10);

CREATE TABLE SALGRADE
      ( GRADE INT,
	LOSAL INT,
	HISAL INT );
INSERT INTO SALGRADE VALUES (1,700,1200);
INSERT INTO SALGRADE VALUES (2,1201,1400);
INSERT INTO SALGRADE VALUES (3,1401,2000);
INSERT INTO SALGRADE VALUES (4,2001,3000);
INSERT INTO SALGRADE VALUES (5,3001,9999);

COMMIT;

SELECT * FROM DEPT;

SELECT * FROM EMP;

SELECT * FROM SALGRADE;


-- 회원테이블 --
create table usertbl(
userid char(15) not null primary key,
name varchar(20) not null,
birthyear int not null, 
addr char(100),
mobile char(11),
mdate date)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 구매테이블 --
create table buytbl(
num int auto_increment primary key,
userid char(8) not null,
productname char(10),
groupname char(10),
price int not null,
amount int not null,
foreign key (userid) references usertbl(userid) on delete cascade)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- 데이터 삽입 --
insert into usertbl values('kty', '김태연',1989,'전주','01011111111', '1989-3-9');
insert into usertbl values('bsj', '배수지',1994,'광주','01022222222', '1994-10-10');
insert into usertbl values('ksh', '김설현',1995,'부천','01033333333', '1995-1-3');
insert into usertbl values('bjh', '배주현',1991,'대구','01044444444', '1991-3-29');
insert into usertbl values('ghr', '구하라',1991,'광주','01055555555', '1991-1-13');
insert into usertbl values('san', '산다라박',1984,'부산','01066666666', '1984-11-12');
insert into usertbl values('jsm', '전소미',2001,'캐나다','01077777777', '2001-3-9');
insert into usertbl values('lhl', '이효리',1979,'서울','01088888888', '1979-5-10');
insert into usertbl values('iyou', '아이유',1993,'서울','01099999999', '1993-5-19');
insert into usertbl values('ailee', '에일리',1989,'미국','01000000000', '1989-5-30');

commit;

insert into buytbl values(null, 'kty', '운동화', '잡화', 30, 2);
insert into buytbl values(null, 'kty', '노트북', '전자', 1000, 1);
insert into buytbl values(null, 'jsm', '운동화', '잡화', 30, 1);
insert into buytbl values(null, 'lhl', '모니터', '전자', 200, 1);
insert into buytbl values(null, 'bsj', '모니터', '전자', 200, 1);
insert into buytbl values(null, 'kty', '청바지', '잡화', 100, 1);
insert into buytbl values(null, 'lhl', '책', '서적', 15, 2);
insert into buytbl values(null, 'iyou', '책', '서적', 15, 7);
insert into buytbl values(null, 'iyou', '컴퓨터', '전자', 500, 1);
insert into buytbl values(null, 'bsj', '노트북', '전자', 1000, 1);
insert into buytbl values(null, 'bjh', '메모리', '전자', 50, 4);
insert into buytbl values(null, 'ailee', '운동화', '잡화', 30, 2);
insert into buytbl values(null, 'ghr', '운동화', '잡화', 30, 1);

commit;


-- table 목록 확인 --
show tables;

-- select로 테이블 데이터 전체 확인 --
select *
from tCity;

-- table 구조 확인 --
DESC tCity;

-- select로 테이블 데이터 확인 --
select region, name, area
from tCity;

-- 컬럼명 별칭 예시 --
SELECT region AS 지역, name AS 도시명, area AS 면적
FROM tCity;

-- 컬럼 연산식 예시 --
SELECT round(popu*10000/area) AS 인구밀도
FROM tCity;

-- 단순 연산식 --
SELECT 2*3;

-- 컬럼 연결 조회 → CONCAT 함수 이용 --
SELECT CONCAT(name,":", area) AS 지역정보
FROM tCity;

-- Distinct 사용하여 중복 제거 --
SELECT DISTINCT region
FROM tCity;

-- GROUP BY 사용하여 중복 제거  --
SELECT region
FROM tCity
GROUP BY region;

-- 인구 수로 내림차순 --
SELECT *
FROM tCity
ORDER BY popu DESC 

-- Index와 별칭 사용 --
SELECT region AS 지역, name AS 이름, area, popu
FROM tCity
ORDER BY 지역, 3 DESC  -- 컬럼명의 별칭과 인덱스 사용 --

-- WHERE 예시 --
SELECT *
FROM tCity
WHERE BINARY(metro) ='y';

-- score가 null인 테이블 모두 조회 --
SELECT *
FROM tStaff
WHERE score IS NULL -- = NULL 사용 시 조회 불가 --


-- 인구 100 이상, area 700이상 조회 --
SELECT *
FROM tCity
WHERE popu >=100 AND area >=700 


-- score가 >=60 또는 salary <500인 테이블 모두 조회 --
SELECT *
FROM tStaff
WHERE salary<500 OR score >=60 ;



-- LIKE 예시--
-- name에 천 포함되는 행 조회 -- 
SELECT * 
FROM tCity
WHERE name LIKE '%천%'


-- EMP 테이블에서 ename에 L이 2개 이상 포함된 데이터 조회 -- 
SELECT * 
FROM EMP
WHERE ENAME LIKE '%L%L%'


-- 와일드 카드 문자열 검색 --
WHERE sale LIKE '%30#%%' ESCAPE '#'
 

-- 입사일이 10월인 사원의 데이터 조회 --
SELECT * 
FROM tStaff
WHERE joindate LIKE '_____10%'


-- joindate가 2018인 데이터 조회 1--
SELECT * 
FROM tStaff
WHERE joindate LIKE '2018%'


-- BETWEEN 예시-- 
-- 인구가 50-100 사이 데이터 조회 --
SELECT * 
FROM tCity
WHERE popu BETWEEN 50 AND 100


-- joindate가 2018인 데이터 조회 2--
SELECT * 
FROM tStaff
WHERE joindate BETWEEN '2018-01-01' AND '2018-12-31'

-- IN 예시 --
-- region이 경상 혹은 경기인 경우만 조회 --
SELECT * 
FROM tCity
WHERE region IN('경상','경기')

-- 행 개수 제한 --
SELECT * 
FROM tCity
ORDER BY area DESC
LIMIT 1, 3

-- 행 개수 제한 --
SELECT * 
FROM tCity
ORDER BY area DESC
LIMIT 3
OFFSET 1


-- salary가 12-16위 까지 조회 --
SELECT * 
FROM tStaff
ORDER BY salary DESC
LIMIT 11,5


-- name과 score 조회하고 score는 일의 자리에서 반올림하여 정수로 표현 --
SELECT name,ROUND(score,0) as score
FROM tStaff

-- 입사년도가 1981년인 데이터 조회 --
SELECT *
FROM EMP
WHERE SUBSTRING(HIREDATE,1,4)='1981'

-- 사원명 'E'로 끝나는 데이터 조회 --
SELECT *
FROM EMP
WHERE SUBSTRING(ENAME,-1,1)='E'

-- 근무일 계산하기 --
SELECT ENAME, (CURRENT_DATE()- HIREDATE) AS 근무일
FROM EMP;





