import sqlite3 # sqlite3는 표준 라이브러리에 포함되어 있음. 따로 pip 설치 없음
conn = sqlite3.connect("test_db.db") # 데이터베이스 연결
cursor = conn.cursor()
# 테이블 생성
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, name TEXT)")

# 데이터 삽입
cursor.execute("INSERT INTO example (name) VALUES ('SQLite test');")
cursor.execute("INSERT INTO example (name) VALUES ('Hello World.');")
conn.commit() # 변경사항 저장

# 데이터 조회
cursor.execute("SELECT * FROM example")
rows = cursor.fetchall() # fetchone(), fetchmany()
for row in rows:
    print(row) # fetch의 결과는 tuple
    
# 데이터베이스 연결 종료
cursor.close()
conn.close()
'''


import sqlite3
conn = sqlite3.connect('test_db.db') # 데이터베이스 연결
cur = conn.cursor()

# 고객 정보 테이블 생성
cur.execute("""
CREATE TABLE IF NOT EXISTS customer_tbl (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
address TEXT
)
""")
      
# 10개의 데이터 준비
customers = [
('김철수', 28, '서울'),
('이영희', 32, '부산'),
('박지원', 45, '대전'),
('최유리', 23, '인천'),
('윤현수', 55, '광주'),
('김태영', 35, '대구'),
('정민우', 42, '울산'),
('박소연', 26, '서울'),
('이수진', 31, '부산'),
('홍길동', 29, '서울')
]

cur.executemany("""INSERT INTO customer_tbl (name, age, address)
VALUES (?, ?, ?)
""", customers)
conn.commit()

# 나이 속성에 기반하여 데이터 삭제
age_to_delete = 45
cur.execute("DELETE FROM customer_tbl WHERE age = ?", 
(age_to_delete,))
conn.commit()

# 데이터 정보 업데이트
customer_id_to_update = 2
new_address = '제주'
cur.execute("UPDATE customer_tbl SET address = ? WHERE id = ?", 
(new_address, customer_id_to_update))
conn.commit()


# 데이터 조회
cur.execute("SELECT * FROM customer_tbl")
rows = cur.fetchall()
for row in rows:
    print(row)
# 테이블 내용 전체 백업
with open('test_db_backup.sql', 'w') as f:
    for line in conn.iterdump():
        f.write(f'{line}\n')
conn.close()
