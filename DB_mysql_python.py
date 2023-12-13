#mysql_python 연동: insert문 포매팅
import pymysql
conn = pymysql.connect(host="127.0.0.1", user="root", password="12345678")
cursor = conn.cursor()#커서생성
cursor.execute("SELECT user, host FROM mysql.user;")

row= cursor.fetchmany(2)
print(row)
row= cursor.fetchmany(2)
print(row)

#cursor.execute("CREATE DATABASE selfstudy;")#DB생성
cursor.execute("USE selfstudy;")
'''
sql1 = """CREATE TABLE TEST (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT, 
SEX CHAR(1),
INCOME FLOAT )"""#Table 생성


cursor.execute(sql1)


sql = """INSERT INTO TEST(FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES ('철수', '김', 23, '남', 2000)"""
cursor.execute(sql)
conn.commit()#기본 INSERT문
'''

"""
try :#성공
    
    sql2 = '''INSERT INTO selfstudy.TEST(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s', '%s', %d, '%s', %d );''' 

    cursor.execute(sql2 % ('영희', '이', 23, '여', 6000))
    conn.commit()
except:
    print("2가안됨")



    

try :#성공
    sql2 = '''INSERT INTO selfstudy.TEST(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s', '%s', %d, '%s', %d );'''% ('이름', '이', 23, '여', 6000)

    cursor.execute(sql2)
    conn.commit()

except:
    print("2가안됨")


    

try:#성공
    first_name = "수정"
    last_name = "최"
    age = 22
    sex = "여"
    income = 5500

    sql3 = f'''INSERT INTO selfstudy.TEST(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
    ("{first_name}", "{last_name}", {age}, "{sex}", {income});'''

    cursor.execute(sql3)
    conn.commit()

except:
    print("3이안됨")


    

try:#성공
    
    first_name2 = '수진'
    last_name2 = '최'
    age2 = 24
    sex2 = '여'
    income2 = 5500

    sql4= f'''INSERT INTO selfstudy.TEST(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
    ('{first_name2}', '{last_name2}', {age2}, '{sex2}', {income2});'''

    cursor.execute(sql4)
    conn.commit()
    
except:
    print("4가안됨")


    

try:#성공

    first_name3 = "수영"
    last_name3 = "최"
    age3 = 28
    sex3 = "여"
    income3 = 5500

    sql5 = '''INSERT INTO selfstudy.TEST(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
    ('{}', '{}', {}, '{}', {});'''.format(first_name3, last_name3, age3, sex3, income3)

    cursor.execute(sql5)
    conn.commit()

except:
    print("5가안됨")




try: #실패
    data = (('영이', '이', 29, '여', 6000),('영삼', '이', 29, '여', 6000))

    sql6= '''INSERT INTO selfstudy.TEST (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s', '%s', %d, '%s', %d);'''

    for i in iter(data):
        cursor.execute(sql6% i)
        conn.commit()
    
except:
    print("6이안됨")

    


try: #성공   
    data = ('영이', '이', 29, '여', 6000)

    sql7= '''INSERT INTO selfstudy.TEST (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s', '%s', %d, '%s', %d);'''
    cursor.execute(sql7% data)
    conn.commit()
    
except:
    print("7이안됨")




try:#실패

    data = ('영규', '이', 29, '여', 6000)

    sql8= '''INSERT INTO selfstudy.TEST (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s', '%s', %d, '%s', %d);'''
    cursor.execute(sql8,data)
    conn.commit()
    
except:
    print("8이안됨")
    

try:  #성공  
    data = (('영사', '이', 29, '여', 6000),('영삼', '이', 29, '여', 6000))

    sql9= '''INSERT INTO selfstudy.TEST (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('%s', '%s', %d, '%s', %d);'''

    for i in iter(data):
        cursor.execute(sql9% i)
        conn.commit()
        
except:
    print("9안됨")

try:#실패
    data = [('영오', '이', 29, '여', 6000),('영육', '이', 29, '여', 6000)]
    sql10= '''INSERT INTO selfstudy.TEST (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)VALUES (?,?,?,?,?);'''
    cursor.executemany('''INSERT INTO selfstudy.TEST
    (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)VALUES (?,?,?,?,?);''', data)

    conn.commit()

except:
    print("10안됨")
"""

cursor.execute("SELECT * FROM TEST;")
rows= cursor.fetchall()
for row in rows:
    print(row)



cursor.close()
conn.close()
