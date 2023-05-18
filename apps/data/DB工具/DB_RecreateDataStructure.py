import psycopg2 as pc2
from DB_config import POSTGRES # 資料庫連線的必要設定資訊

def getConn():
    conn = pc2.connect(
        user = POSTGRES['user'],
        password = POSTGRES['password'],
        host = POSTGRES['host'],
        port = POSTGRES['port']
    )
    return conn

def database_isExist(idx):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = '%(database)s'" % POSTGRES['createItem'][idx])
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return True if result is not None else False

def database_create(idx):
    conn = getConn()
    conn.autocommit = True # 先理解「事務：transaction」，這個動作確保未來創建 Database 的時候要在 transaction block 之外
    cursor = conn.cursor()
    try:
        # 需要特別注意，字典 values 欄位的文字需要特別在單引號內加雙引號，不然寫進資料庫的資料將會「對大小寫不敏感」，換句話說就是只會寫進小寫
        cursor.execute('CREATE DATABASE "%(database)s"' % POSTGRES['createItem'][idx])
    except:
        print("數據庫 %(database)s 創建失敗" % POSTGRES['createItem'][idx])
    else:
        print("數據庫 %(database)s 創建成功" % POSTGRES['createItem'][idx])

    cursor.close()
    conn.close()

def schema_exists(cursor, idx):
    # 特別注意，這查詢 schema 的時候要將名稱設置元 tuple，GPT 教我的，所以為什麼？我也不知道
    cursor.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = %s", (POSTGRES['createItem'][idx]["schema"],))
    result = cursor.fetchone()

    return True if result is not None else False

def create_schema(conn, idx):
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE SCHEMA "%(schema)s"' % POSTGRES['createItem'][idx])
    except:
        print("schema %(schema)s 創建失敗" % POSTGRES['createItem'][idx])
    else:
        print("schema %(schema)s 創建成功" % POSTGRES['createItem'][idx])
    conn.commit()

def table_exists(cursor, idx):
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = %s AND table_name = %s", (POSTGRES['createItem'][idx]["schema"], POSTGRES['createItem'][idx]["table"]))
    result = cursor.fetchone()

    return True if result is not None else False

def create_table(conn, idx):
    cursor = conn.cursor()

    try:
        # 給定一個 list 來保存 column 相關定義
        column_definitions = []
        # 給定一個 list 來保存 PK
        primary_key_columns = []

        # 迭代 POSTGRES 字典中的 tableColumn 項目
        for column in POSTGRES['createItem'][idx]["tableColumn"].values():
            column_name = column["name"]
            data_type = column["dataType"]
            can_null = "NULL" if column["canNull"] else "NOT NULL"
            is_PK = column["isPK"]
            
            # 將 column 相關定義添加到 list 中
            column_definitions.append(f'"{column_name}" {data_type} {can_null}')

            # 如果 isPK 為 True，將欄位名稱添加到 PK list
            if is_PK:
                primary_key_columns.append(column_name)
        
        # 用逗號將列定義連接在一起
        columns_string = ", ".join(column_definitions)

        # 用逗號將 PK 欄位連接在一起
        primary_key_string = ", ".join(primary_key_columns)
        
        # 合成 SQL 語法
        SQL_cmd = ('CREATE TABLE "%(schema)s"."%(table)s"('
                f"{columns_string}"
                f",PRIMARY KEY ({primary_key_string})"
            ')' % POSTGRES['createItem'][idx])

        #print(SQL_cmd)
        # 建立資料表，連欄位也一起建
        cursor.execute(SQL_cmd)
    except:
        print("資料表 %(table)s 創建失敗" % POSTGRES['createItem'][idx])
    else:
        print("資料表 %(table)s 創建成功" % POSTGRES['createItem'][idx])
    conn.commit()

if __name__ == '__main__':
    
    # 遍歷 DB_config 要重建的資料表 表項目
    for idx, createItem in enumerate(POSTGRES['createItem']):
        # 檢查資料庫是否存在
        if database_isExist(idx):
            print("數據庫 %(database)s 存在" % POSTGRES['createItem'][idx])
        else:
            print("數據庫 %(database)s 不存在，將開始創建數據庫" % POSTGRES['createItem'][idx])
            database_create(idx)
        
        
        # 連接到 PostgreSQL
        conn = pc2.connect(
            host = POSTGRES["host"],
            user = POSTGRES["user"],
            password = POSTGRES["password"],
            database = POSTGRES['createItem'][idx]["database"],
            port = POSTGRES['port']
        )
        cursor = conn.cursor()
        
        # 檢查 schema 是否存在
        if schema_exists(cursor, idx):
            print("schema %(schema)s 存在" % POSTGRES['createItem'][idx])
        else:
            print("schema %(schema)s 不存在，將開始創建 schema" % POSTGRES['createItem'][idx])
            create_schema(conn, idx)

        # 檢查 資料表 是否存在
        if table_exists(cursor, idx):
            print("資料表 %(table)s 存在" % POSTGRES['createItem'][idx])
        else:
            print("資料表 %(table)s 不存在，將開始創建資料表" % POSTGRES['createItem'][idx])
            create_table(conn, idx)

        # 提交更改並關閉連接
        cursor.close()
        conn.close()