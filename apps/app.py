from flask import Flask, render_template, request, json, jsonify, url_for, redirect
from db_manipulate import *

app = Flask(__name__, template_folder='templates')
db_connection = connectDatabase()
cursor = db_connection.cursor()
resetUserLogin(cursor)


@app.route('/')
def enter():
    return redirect(url_for('login'))


# 登入頁面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userId = request.values['id']
        userPwd = request.values['password']
        print(userId, userPwd)
        loginAuthMsg = userLoginAuth(userId, userPwd, cursor)
        if loginAuthMsg == 'login successfully':
            return redirect(url_for('search', username=userId))
    return render_template('login.html')


# 查詢頁面
@app.route('/<username>/search', methods=['GET', 'POST'])
def search(username):
    if request.method == 'POST':
        on_days = []
        county = request.values['county']
        district = request.values['district']
        type = request.values['type']

        if request.form.get('mon'):
            on_days.append('星期一')
        if request.form.get('tue'):
            on_days.append('星期二')
        if request.form.get('wed'):
            on_days.append('星期三')
        if request.form.get('thr'):
            on_days.append('星期四')
        if request.form.get('fri'):
            on_days.append('星期五')
        if request.form.get('sat'):
            on_days.append('星期六')
        if request.form.get('sun'):
            on_days.append('星期日')

        print(county)
        print(district)
        print(type)
        print(on_days)

        return redirect(url_for('search', username=username))
    return render_template('search.html')


# 結果頁面
@app.route('/<username>/result')
def result(username):
    return render_template('result.html')


# 常用頁面
@app.route('/<username>/favorite')
def favorite(username):
    return render_template('favorite.html')


# 透過ajax把資料傳到flask api接口
@app.route('/result/submit', methods=['POST'])
@app.route('/favorite/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print(data)
    return jsonify({'message': '資料已成功接收'})


if __name__ == '__main__':
    app.debug = True
    app.run()
