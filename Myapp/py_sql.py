import pymysql


class py_sql:

    def py_mysql(db_config, sql_content):
        conn = pymysql.connect(
            host=db_config.db_host,
            port=db_config.db_port,
            user=db_config.db_user,
            password=db_config.db_password,
            database=db_config.db_database
        )
        cur = conn.cursor()
        cur.execute(sql_content)
        data = cur.fetchall()  # 获取结果集全部
        cur.close()
        conn.close()
        return data
