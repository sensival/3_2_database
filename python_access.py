import pyodbc
import os
from comtypes.client import CreateObject
db_file = r"C:\Users\wogns\OneDrive\바탕 화면\3-2강의자료\DB\customer_db.accdb"
# Access 데이터베이스 파일 경로 설정
# 데이터베이스 파일(customer.accdb)이 없으면 생성
if not os.path.exists(db_file):
    access_app = CreateObject("Access.Application")
    access_app.NewCurrentDatabase(db_file)
    access_app.Quit()
    print(f"accdb 파일 생성: {db_file}")

# ODBC 연결 문자열
conn_str = (
    r"Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};"
    r"DBQ={};".format(db_file)
)
# 데이터베이스 연결
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# 테이블이 존재하는지 확인하고 삭제
table_name = "customer_tbl"
try:
    cursor.execute(f"SELECT * FROM {table_name}")
    cursor.execute(f"DROP TABLE {table_name}")
    conn.commit()
except pyodbc.Error as e:
    print(f"테이블 {table_name}이(가) 존재하지 않습니다.")

cursor.execute("""
CREATE TABLE customer_tbl (
ID AUTOINCREMENT PRIMARY KEY,
name VARCHAR(50),
age INT,
address VARCHAR(100)
)
""")
conn.commit()

# 2. 테이블에 5개의 INSERT 문을 사용하여 삽입
customers = [
("홍길동", 30, "서울시 종로구"),
("이몽룡", 25, "서울시 강남구"),
("조자룡", 23, "서울시 서초구"),
("이영희", 28, "서울시 동작구"),
("김철수", 25, "서울시 용산구"),
]
for customer in customers:
    cursor.execute("INSERT INTO customer_tbl (name, age, address) VALUES (?, ?, ?)", customer)
conn.commit()

# 3. 1개의 데이터를 나이 속성에 기반하여 삭제
cursor.execute("DELETE FROM customer_tbl WHERE age = ?", 30)
conn.commit()
                   
# 4. 1개의 데이터 정보를 업데이트
cursor.execute("UPDATE customer_tbl SET address = ? WHERE name = ?", ("서울시 마포구", "이몽룡"))
conn.commit()
                   
# 5. SELECT 문으로 데이터를 조회
cursor.execute("SELECT * FROM customer_tbl")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 6. 테이블 내용 전체를 백업 (Access 데이터베이스 파일 복사)
import shutil
shutil.copyfile(db_file, r"customer_db_backup.accdb")
                   
# 연결 종료
cursor.close()
conn.close()
