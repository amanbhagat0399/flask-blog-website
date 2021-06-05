

class Config():
    SECRET_KEY= '9a5c76d9e4fb1761e1d7b9232f081f5d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME = 'amanbhagat0399@gmail.com'
    MAIL_PASSWORD  = 'ulwutseodmqhdopo'