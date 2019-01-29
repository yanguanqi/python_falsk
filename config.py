import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    print("Config(object)")
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOGGING_MODE = os.environ.get('LOGGING_MODE') or 'None' or 'FILE'

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.aliyun.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USER_TLS = os.environ.get('MAIL_USER_TLS') or '1'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'yangaunqi@aliyun.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    POSTS_PER_PAGE = 3
