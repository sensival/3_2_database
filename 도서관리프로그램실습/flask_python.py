# pip install flask
# pip install waitress
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient.Then 여기에서 python 버전과 window 버전에 맞게 다운로드
# python 3.6.5 / 64bit ---> mysqlclient-1.4.6-cp36-cp36m-win_amd64.whl
# pip install mysqlclient-1.4.6-cp36-cp36m-win_amd64.whl
# pip install flask_mysqldb 
# templates 폴더 생성하여 html 파일 넣어 두기


from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from waitress import serve
app = Flask(__name__)

# MariaDB 연결 설정
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search']
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM book_tbl WHERE title LIKE '%{search_query}%'")
    data = cursor.fetchall()
    cursor.close()
    return render_template('search_results.html', data=data)


@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    publisher = request.form['publisher']
    price = request.form['price']
    stock = request.form['stock']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO book_tbl (title, author, publisher, price, stock) VALUES (%s, %s, %s, %s, %s)', (title, author, publisher, price, stock))
    mysql.connection.commit()
    cursor.close()


if __name__ == '__main__':
    # app.run(debug=True)
    port = 5000
    print("Server is ready: http://ip:5000")
    serve(app, host="0.0.0.0", port=port)
