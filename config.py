DEBUG = True

ADMINS = frozenset(['chrhyman@gmail.com'])
SECRET_KEY = '3r3i0bkn%437941ua07k419244w'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format(
    "wugs", "sqlpassword", "wugs.mysql.pythonanywhere-services.com",
    "wugs$users")
SQLALCHEMY_POOL_RECYCLE = 299