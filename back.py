from flask import Flask,request,jsonify
import requests
from oai import ai

database = [("캡스톤 디자인 및 AI 해커톤 경진대회","https://www.skku.edu/skku/campus/skk_comm/notice01.do?mode=view&articleNo=109355&article.offset=0&articleLimit=10&srSearchVal=%ED%95%B4%EC%BB%A4%ED%86%A4")]
app = Flask(__name__)



@app.route("/")
def home():
    print("Hello")
    return "HelloWorld"

#강의추천
@app.route("/recommend",methods = ['POST'])
def recommend():
    payload = request.get_json()

    #str
    input_prom = payload['input_prom']
    
    #str
    outprom = ai(inprom = input_prom)


    ans = {"outprom":outprom}
    return jsonify(ans)

#시간표 작성
@app.route("/schedule",methods = ['POST'])
def schedule():

    payload = request.get_json()
    condtion = payload['condtion'] #과목수 필수 파라미터
    outprom = ai(inprom = condtion)

    print(database2[0])
    ans = {"outprom":outprom}
    return jsonify(ans)

#관련 행상 추천
@app.route("/event",methods = ['POST'])
def event():
    info = database.pop()
    ans = {"name":info[0],"link":info[1]}
    return jsonify(ans)






    


if __name__ == "__main__":
    app.run(debug=True)