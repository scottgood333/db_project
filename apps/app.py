from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)


# 登入頁面
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

# 查詢頁面
@app.route('/search', methods=['GET','POST'])
def search():
    return render_template('search.html')

# 結果頁面
@app.route('/result')
def result():
    return render_template('result.html')

# 常用頁面
@app.route('/favorite')
def favorite():
    return render_template('favorite.html')

# 透過ajax把資料傳到flask api接口
@app.route('/result/submit', methods=['POST'])
@app.route('/favorite/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print(data)
    return jsonify({'message': '資料已成功接收'})

