import json                                                                 # data를 json형식으로 변환하기 위한 모듈
import requests                                                             # data를 전송하기 위한 모듈

dict_data = {'number':1, 'address':'daejeon','name':'lee'}                  # data 타입은 dictionary 형식
json_data = json.dumps(dict_data, indent=4, ensure_ascii=False)             # dictionary를 json으로 변환

print(json_data)

url = "http://192.168.219.100:5000/data"                                    # 전송될 서버의 주소

headers = {'Content-Type':'application/json', 'Accept':'application/json'}  # 전송되는 데이터가 json임을 알림
send_data = requests.post(url, data=json_data, headers=headers)             # POST 방식으로 데이터를 전송

print(send_data.status_code)                                                # 데이터가 성공적으로 전송되었는지 확인
                                                                            # 200 이면 > 성공, 이외 숫자 > 실패
