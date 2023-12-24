# 파일 이름을 hello.py로 저장
from flask import Flask, request
app = Flask(__name__) # 현재 파일의 이름을 가지고 Flask 웹 앱 인스턴스를 생성
@app.route('/') # 사용자가 웹사이트의 루트 URL에 접근할 때 실행될 함수를 정의
def hello_world():
    client_ip = request.remote_addr
    print("Request from", client_ip)
    return 'Hello, World! Your IP is: {}'.format(client_ip)


if __name__ == '__main__':
    app.run() # 웹 서버를 실행
# python IDLE 환경에서 위 프로그램 실행
# 웹 브라우저에서 http://localhost:5000/ 입력
