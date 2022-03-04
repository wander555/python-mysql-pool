# -*- coding:utf-8 -*-
from python_mysql_config import MyPymysqlPool

if __name__ == '__main__':
    mysql = MyPymysqlPool("notdbMysql")
    sqlAll = "select * from my_db.wallpaper;"
    result = mysql.getMany(sqlAll, 2)
    print(result)
    mysql.dispose()
