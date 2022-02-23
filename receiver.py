from flask import Flask, request        # flask 실행 모듈, 데이터를 수신을 위한 request 모듈
import json                             # 수신받은 데이터를 json file로 변환하기 위한 모듈

app = Flask(__name__)
@app.route("/data", methods=["POST"])   # url을 불러 처리하는 명령어

def data_receiver():
    data = request.get_json()           # json형식으로 넘어온 data를 읽어들임
    json_data = json.dumps(data)        # 읽어온 데이터는 dictionary 형식으로 변환되므로 다시 json형식으로 변환
    
    print(json_data)
    
    if data == "none":                  # 만약 data가 없으면 웹 페이지에 fail을 표시
        return 'fail'
    else:
        return 'success'                # 만약 data가 있으면 웹 페이지에 success를 표시

if __name__ == "__main__":              # 현재 python file에서 실행 할 때만 실행되게 함
    app.run(host="192.168.219.100", port="5000", debug=True)
