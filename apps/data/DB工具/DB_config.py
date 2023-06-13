POSTGRES = {
    'user': 'postgres',      # Postgre 使用者帳號
    'password': 'wu8313497',  # Postgre 使用者密碼
    'host': 'localhost',
    'port': 5432,            # Postgre 連線 port
    'createItem': [           # 需要新增的資料表，內容需要包含表所在的 DB、schema、table，以及表中有的 column 的資訊
        {
            'database': 'health_insurance_hospitals',
            'schema': 'public',
            'table': 'UserInfo',
            'tableColumn': {
                1: {
                    'name': 'user_id',
                    'dataType': 'VARCHAR',
                    'canNull': False,
                    'isPK': True
                },
                2: {
                    'name': 'user_password',
                    'dataType': 'VARCHAR',
                    'canNull': False,
                    'isPK': False
                },
                2: {
                    'name': 'is_login',
                    'dataType': 'BOOL',
                    'canNull': False,
                    'isPK': False
                }
            }
        }
    ]
}
