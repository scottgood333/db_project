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
def searchHospital(city, county, type, on_day):


    # testing functions
if __name__ == '__main__':
    connection = connectDatabase()
    loginAuthMsg = userLoginAuth('F74086137', 'wu8313497', connection.cursor())
    # resetUserLogin(connection.cursor())
    print(loginAuthMsg)
