from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import setting

# 实例化app
app = Flask(__name__)

# 连接数据库，实例化数据库连接会话
database_key = '{0}://{1}:{2}{3}/{4}'.format(setting.DATABASE_TYPE, setting.USER, setting.PASSWORD, setting.URL,
                                             setting.DATABASE_NAME)
engine = create_engine(database_key, echo=True)
DBSession = sessionmaker(bind=engine)

from app.controller import index
