from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/user/",methods=["POST"])
def login():
    name_list = ["张三"]
    pwd = ["123456"]
    if not request.json:
        return jsonify({"cood":"10001","msg":"请求类型错误","data":None})
    if not "name" in request.json or not "password" in request.json:
        return jsonify({"cood":"10002","msg":"请填写姓名和密码","data":None})
    name = request.json.get("name")
    password = request.json.get("password")
    if name in name_list and password in pwd:
        return jsonify({"cood":"200","msg":"登陆成功","data":name})
    else:
        return jsonify({"code":"10003","msg":"姓名或密码错误","data":None})

if __name__ == "__main__":
    app.run()