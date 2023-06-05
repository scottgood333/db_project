import psycopg2
import json

HOSPITAL_GRADE_DICT = {}
HOSPITAL_GRADE_DICT["regional"] = "地區醫院"
HOSPITAL_GRADE_DICT["center"] = "醫學中心"
HOSPITAL_GRADE_DICT["district"] = "區域醫院"
HOSPITAL_GRADE_DICT["clinic"] = "診所"
HOSPITAL_GRADE_DICT["pharmacy"] = "藥局"


# connect to  database
def connectDatabase():
    connection = psycopg2.connect(database='health_insurance_hospitals',
                                  user='postgres',
                                  password='wu8313497',
                                  host='localhost',
                                  port='5432')
    connection.autocommit = True
    return connection


# authenticate user login
def userLoginAuth(userIdIn, userPwdIn, cursor):
    cursor.execute(f'SELECT * FROM user_info ')
    userInfos = cursor.fetchall()
    for userId, userPwd, userIsLogin in userInfos:
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


# make time dict for searching
def getOnTimeDict(on_time):
    time_dict = {}
    time_dict["mon"] = [0, 0, 0]
    time_dict["tue"] = [0, 0, 0]
    time_dict["wed"] = [0, 0, 0]
    time_dict["thr"] = [0, 0, 0]
    time_dict["fri"] = [0, 0, 0]
    time_dict["sat"] = [0, 0, 0]
    time_dict["sun"] = [0, 0, 0]

    for str in on_time.split("、"):
        if "星期一" in str:
            if "上午看診" in str:
                time_dict["mon"][0] = 1
            if "下午看診" in str:
                time_dict["mon"][1] = 1
            if "晚上看診" in str:
                time_dict["mon"][2] = 1
        elif "星期二" in str:
            if "上午看診" in str:
                time_dict["tue"][0] = 1
            if "下午看診" in str:
                time_dict["tue"][1] = 1
            if "晚上看診" in str:
                time_dict["tue"][2] = 1
        elif "星期三" in str:
            if "上午看診" in str:
                time_dict["wed"][0] = 1
            if "下午看診" in str:
                time_dict["wed"][1] = 1
            if "晚上看診" in str:
                time_dict["wed"][2] = 1
        elif "星期四" in str:
            if "上午看診" in str:
                time_dict["thr"][0] = 1
            if "下午看診" in str:
                time_dict["thr"][1] = 1
            if "晚上看診" in str:
                time_dict["thr"][2] = 1
        elif "星期五" in str:
            if "上午看診" in str:
                time_dict["fri"][0] = 1
            if "下午看診" in str:
                time_dict["fri"][1] = 1
            if "晚上看診" in str:
                time_dict["fri"][2] = 1
        elif "星期六" in str:
            if "上午看診" in str:
                time_dict["sat"][0] = 1
            if "下午看診" in str:
                time_dict["sat"][1] = 1
            if "晚上看診" in str:
                time_dict["sat"][2] = 1
        elif "星期日" in str:
            if "上午看診" in str:
                time_dict["sun"][0] = 1
            if "下午看診" in str:
                time_dict["sun"][1] = 1
            if "晚上看診" in str:
                time_dict["sun"][2] = 1
    return time_dict


# check if hospital is in user's favorites
def checkIsFavorite(username, sign_num, cursor):
    cursor.execute(
        f'SELECT user_id, hospital_sign_num FROM favorites WHERE user_id = \'{username}\' AND hospital_sign_num = \'{sign_num}\'')
    value = cursor.fetchall()
    if value:
        return 1
    return 0


# search
def searchHospital(username, county, district, type, on_days, cursor):
    try:
        cursor.execute(
            f'SELECT sign_num, name, address, phone_num, on_time, department FROM hospital_info WHERE city = \'{county}\' AND address LIKE %(district)s AND grade = \'{HOSPITAL_GRADE_DICT[type]}\' ', {'district': f'%{district}%'})
        hospital_infos = cursor.fetchall()

        # make dict
        hospital_info_dict = {}
        for sign_num, name, address, phone_num, on_time, department in hospital_infos:
            # print(hospital_infos)
            is_selected = False
            try:
                # check if selected day is on
                for str in on_time.split("、"):
                    for on_day in on_days:
                        if "看診" in str and on_day in str:
                            is_selected = True
                if is_selected:
                    hospital_info_dict[sign_num] = {}
                    hospital_info_dict[sign_num]["name"] = name
                    hospital_info_dict[sign_num]["address"] = address
                    hospital_info_dict[sign_num]["phone"] = phone_num
                    hospital_info_dict[sign_num]["type"] = HOSPITAL_GRADE_DICT[type]
                    hospital_info_dict[sign_num]["department"] = department
                    hospital_info_dict[sign_num]["time"] = getOnTimeDict(on_time)
                    hospital_info_dict[sign_num]["is_favorite"] = checkIsFavorite(username, sign_num, cursor)
            except AttributeError:
                continue
        # print(hospital_info_dict)
    except KeyError:
        return {'err': -1}

    return hospital_info_dict


# get favorites
def getFavorites(username, cursor):
    favorites = []
    cursor.execute(
        f'SELECT  hospital_sign_num UNIQUE FROM favorites WHERE user_id = \'{username}\'')
    favorite_sign_nums = cursor.fetchall()

    # make dict
    hospital_info_dict = {}
    for e in favorite_sign_nums:
        favorite_sign_num = e[0]
        print(favorite_sign_num)
        favorites.append(favorite_sign_num)

        cursor.execute(
            f'SELECT sign_num, name, address, phone_num, grade, on_time, department FROM hospital_info WHERE sign_num = \'{favorite_sign_num}\'')
        hospital_infos = cursor.fetchall()
        for sign_num, name, address, phone_num, grade, on_time, department in hospital_infos:
            hospital_info_dict[sign_num] = {}
            hospital_info_dict[sign_num]["name"] = name
            hospital_info_dict[sign_num]["address"] = address
            hospital_info_dict[sign_num]["phone"] = phone_num
            hospital_info_dict[sign_num]["type"] = grade
            hospital_info_dict[sign_num]["department"] = department
            hospital_info_dict[sign_num]["time"] = getOnTimeDict(on_time)

    return hospital_info_dict


# add to user's favorites
def addToFavorites(user_favorite_dict, cursor):
    try:
        username = user_favorite_dict["username"]
    except KeyError:
        user_favorite_dict["username"] = ""
        username = user_favorite_dict["username"]

    favorites = user_favorite_dict["favorites"]

    for favorite in favorites:
        cursor.execute(
            f'INSERT INTO favorites VALUES (\'{username}\', \'{favorite}\')')

    print(username)
    print(user_favorite_dict)


# update user's favorites
def upateFavorites(user_favorite_dict, cursor):
    try:
        username = user_favorite_dict["username"]
    except KeyError:
        user_favorite_dict["username"] = ""
        username = user_favorite_dict["username"]

    favorites = user_favorite_dict["favorites"]

    cursor.execute(
        f'DELETE  FROM favorites WHERE user_id = \'{username}\'')

    for favorite in favorites:
        cursor.execute(
            f'INSERT INTO favorites VALUES (\'{username}\', \'{favorite}\')')

    print(username)
    print(user_favorite_dict)


# testing functions
if __name__ == "__main__":
    connection = connectDatabase()
    # loginAuthMsg = userLoginAuth("F74086137", "wu8313497", connection.cursor())
    # resetUserLogin(connection.cursor())
    # print(loginAuthMsg)
    # searchHospital("臺南市", "臺南市中西區", "district", ["星期日", "星期二"], connection.cursor())
    # dict = {"username": "F74086137", "favorites": []}
    # upateFavorites(dict, cursor=connection.cursor())
    # getFavorites('F74086137', cursor=connection.cursor())
    # checkIsFavorite("F74086137", "3731170034", connection.cursor())
