# -*- coding: utf-8 -*-
#
# Copyright 2020 YouthIT
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""基于pymysql/mysqlclient的MySQL客户端
1. 优先使用pymysql模块，支持mysqlclient模块
2. 自动重连
3. 支持事务装饰器
"""

import time

try:
    import pymysql
    import pymysql.cursors as cursors
except ImportError:
    try:
        import MySQLdb as pymysql
        import MySQLdb.cursors as cursors
    except ImportError:
        raise("未找到pymysql/mysqlclient模块，请执行pip install pymysql命令")

version = "0.1"
version_info = (0, 1, 0, 0)

IntegrityError = pymysql.IntegrityError
OperationalError = pymysql.OperationalError

class Connection(object):
    """基于pymysql/mysqlclient的MySQL客户端"""

    def __init__(self, host="localhost", port=3306, db=None, user=None, passwd=None, max_idle_time=8*3600, 
                 connect_timeout=10, time_zone="+8:00", charset="utf8", sql_mode="TRADITIONAL", **kwargs):

        self.max_idle_time = float(max_idle_time)
        self._last_use_time = time.time()
        self._db = None
        self._db_args = dict(host=host, port=port, db=db, user=user, passwd=passwd, use_unicode=True, 
                        cursorclass=cursors.DictCursor, init_command=('SET time_zone = "%s"'%time_zone),
                        connect_timeout=connect_timeout, charset=charset, sql_mode=sql_mode, **kwargs)

        try:
            self.reconnect()
        except Exception:
            raise("Cannot connect to MySQL on %s", self._db_args['host'], exc_info=True)

    def __del__(self):
        self.close()

    def close(self):
        """关闭数据库连接"""

        if getattr(self, "_db", None) is not None:
            try:
                self._db.close()
            except:
                pass
            finally:
                self._db = None

    def reconnect(self):
        """数据库重连"""

        self.close()
        self._db = pymysql.connect(**self._db_args)
        self._db.autocommit(True)

    def _ensure_connected(self):
        """连接确认，如失效，则自动重连"""

        if self._db is None or (time.time()-self._last_use_time) > self.max_idle_time:
            self.reconnect()
        self._last_use_time = time.time()

    def _cursor(self):
        """创建游标"""

        self._ensure_connected()
        return self._db.cursor()

    def query(self, sql, args=None):
        """执行SQL语句
        args        - None或元组类型：单次执行；列表类型：批量执行（列表元素为元组类型）
        """

        try:
            if args:
                assert(isinstance(args, (list, tuple)))
        except AssertionError:
            self.close()
            raise AssertionError

        cursor = self._cursor()
        try:
            if isinstance(args, list):
                cursor.executemany(sql, args)
            else:
                cursor.execute(sql, args)
        except OperationalError:
            self.close()
            raise OperationalError
        except IntegrityError:
            self.close()
            raise IntegrityError
        else:
            op = sql.split()[0].upper()
            if op in ['UPDATE', 'DELETE']:
                return cursor.rowcount
            elif op == 'INSERT':
                return cursor.lastrowid
            else:
                return cursor.fetchall()
        finally:
            cursor.close()

    # 定义别名
    select = update = delete = insert = query

    def transaction(self, dml_func):
        """事务装饰器使用方法：

        db = Connection(host='locahost', port=3306, db='test')
        @db.transaction
        def some_DML_group(db, *args, **kwds):
            pass # DML(insert、update、delete)语句组合。如顺利执行，则commit，否则，rollback
        result = some_DML_group()
        """

        def wrapper(*args, **kwds):
            try:
                self._db.begin()
                dml_func(*args,**kwds)
                self._db.commit()
                return True
            except:
                self._db.rollback()
                return False