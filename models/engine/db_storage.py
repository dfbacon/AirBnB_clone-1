from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBStorage():
    """ """
    __engine = None
    __session = None

    def init(self):
        self.uname = os.environment["HBNB_MYSQL_USER"]
        self.upass = os.environment["HBNB_MYSQL_PWD"]
        self.host = os.environment["HBNB_MYSQL_HOST"]
        self.dbname = os.environment["HBNB_MYSQL_DB"]
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(self.uname, self.upass,
                                              self.host, self.dbname))

        self.__Session = sessionmaker()
        self.__Session.configure(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = self.__Session()

    def all(self, cls=None):
        
