import psycopg2


# connect to  database
def connectDatabase():
    connection = psycopg2.connect(database="health_insurance_hospitals",
                                  user="postgres",
                                  password="wu8313497",
                                  host="localhost",
                                  port="5432")
    connection.autocommit = True
    return connection


# authenticate user login
def userLoginAuth(userIdIn, userPwdIn, cursor):
    cursor.execute(f'SELECT * FROM user_info ')
    userInfos = cursor.fetchall()
    for userId, userPwd, userIsLogin, favorites in userInfos:
        if (userIdIn == userId):
            if (userPwdIn == userPwd):
                print(f'user:{userId} login successfully')
                cursor.execute(f'UPDATE user_info SET is_login = TRUE WHERE user_id = \'{userId}\';')
                return 'login successfully'
            else:
                return 'incorrect password'
    return 'non-existent user'


# reset login state when server restart
def resetUserLogin(cursor):
    cursor.execute(f'UPDATE user_info SET is_login = FALSE;')


# search
def searchHospital(county, district, type, on_days, cursor):
    hospital_grade_dict = {}
    hospital_grade_dict['regional'] = '地區醫院'
    hospital_grade_dict['center'] = '醫學中心'
    hospital_grade_dict['district'] = '區域醫院'
    hospital_grade_dict['clinic'] = '診所'
    hospital_grade_dict['pharmacy'] = '藥局'

    cursor.execute(
        f'SELECT sign_num, name, address, phone_num, on_time FROM hospital_info WHERE city = \'{county}\' AND address LIKE %(district)s AND grade = \'{hospital_grade_dict[type]}\' ', {'district': f'%{district}%'})
    hospital_infos = cursor.fetchall()
    for sign_num, name, address, phone_num, on_time in hospital_infos:
        print(sign_num)
        print(name)
        print(address)
        print(phone_num)
        for str in on_time.split('、'):
            for on_day in on_days:
                if '看診' in str and on_day in str:
                    print(str)


# testing functions
if __name__ == '__main__':
    connection = connectDatabase()
    # loginAuthMsg = userLoginAuth('F74086137', 'wu8313497', connection.cursor())
    # resetUserLogin(connection.cursor())
    # print(loginAuthMsg)
    searchHospital('臺南市', '臺南市中西區', 'clinic', ['星期一', '星期二'], connection.cursor())
