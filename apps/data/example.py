import csv

# 讀取檔案
file = open("./data/RegionalHospital.csv", 'r', encoding="utf-8")
reader = csv.reader(file)

# 初始資料
ids = []
names = []
addresses = []
phones = []
departments = []
times = []

# 跳過標題列
next(reader)

# 看診時間的資料是周一到周七上午->下午->晚上
def split_list(lst):
    n = len(lst)
    k = n // 3
    result = [lst[i:i+k] for i in range(0, n, k)]
    return result

# 儲存資料
for row in reader:
    ids.append(row[0])
    names.append(row[1])
    phones.append(row[3])
    addresses.append(row[4])
    departments.append(row[8])
    time_n = row[10].split("、")
    # print(type(row_n))
    # print(row_n)
    times.append(split_list(time_n))

# 整理看診時間
time_code = []
for index, time in enumerate(times):
    # time 是3*7的矩陣
    # print(time)

    time_list = []
    for j in range(7):
        tmp = ""
        for i in range(3):  # 從星期一開始
            # print(time[i][j])
            last_two = time[i][j][-2:]
            if last_two == "看診":
                tmp = tmp + "1" # 代表看診
            elif last_two == "休診":
                tmp = tmp + "0" # 代表休診

        time_list.append(tmp)
    
    time_code.append(time_list)

# print(len(time_code))
# print(len(ids))
# print(len(names))
# print(len(phones))
# print(len(addresses))
# print(len(departments))

# 建立字典
dictionary = {}   # 用dictionary["id"] = dict_v新增
for i in range(len(ids)):
    # 加入鍵與值到字典
    dict_v = {}
    dict_v["name"] = names[i]
    dict_v["phone"] = phones[i]
    dict_v["address"] = addresses[i]
    dict_v["department"] = departments[i]
    dict_v['type'] = "區域醫院"
    # 看診時間
    time_v = {}
    time_v["mon"] = time_code[i][0]
    time_v["tue"] = time_code[i][1]
    time_v["wed"] = time_code[i][2]
    time_v["thr"] = time_code[i][3]
    time_v["fri"] = time_code[i][4]
    time_v["sat"] = time_code[i][5]
    time_v["sun"] = time_code[i][6]
    dict_v["time"] = time_v
    # 加入到dict
    dictionary[ids[i]] = dict_v

file.close()

# 把字典寫入json檔
import json

json_object = json.dumps(dictionary, ensure_ascii=False)
outfile = open("./data/regional.json", "w", encoding="utf-8")
outfile.write(json_object)
outfile.close()