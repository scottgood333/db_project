from flask import Flask, render_template, request, json, jsonify, url_for, redirect, flash
from db_manipulate import *
import json


app = Flask(__name__, template_folder='templates')
app.secret_key = "7414"
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
        if loginAuthMsg == 'incorrect password':  # 之後再加入flash
            print("輸入的密碼有誤！")
            return redirect(url_for('login'))
        if loginAuthMsg == 'non-existent user':  # 之後再加入flash
            print("不存在這個使用者！")
            return redirect(url_for('login'))
    return render_template('login.html')


# 查詢頁面
@app.route('/<username>/search', methods=['GET', 'POST'])
def search(username):
    if request.method == 'POST':
        return redirect(url_for('result', username=username), code=307)
    return render_template('search.html', username=username)


# 結果頁面
@app.route('/<username>/result', methods=['GET', 'POST'])
def result(username):
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

        hospital_info_dict = searchHospital(username=username, county=county,
                                            district=district, type=type, on_days=on_days, cursor=cursor)
        if hospital_info_dict == {}:
            # print(dict)
            message = '沒有符合條件的結果！'
            flash(message)
            return redirect(url_for('search', username=username))
        if hospital_info_dict == {'err': -1}:
            # print(dict)
            message = '請確實選擇篩選條件！'
            flash(message)
            return redirect(url_for('search', username=username))

    return render_template('result.html',  username=username, dictionary=hospital_info_dict)


# 常用頁面
@ app.route('/<username>/favorite')
def favorite(username):
    favorite_hospital_info_dict = getFavorites(username, cursor)
    return render_template('favorite.html', username=username, dictionary=favorite_hospital_info_dict)


# 透過ajax把資料傳到flask api接口
@app.route('/result/submit', methods=['POST'])
def resultSubmit():
    data = request.get_json()
    print(data)
    addToFavorites(data, cursor)
    return jsonify({'message': '資料已成功接收'})


@app.route('/favorite/submit', methods=['POST'])
def favoriteSubmit():
    data = request.get_json()
    print(data)
    upateFavorites(data, cursor)
    return jsonify({'message': '資料已成功接收'})


if __name__ == '__main__':
    app.debug = True
    app.run()
