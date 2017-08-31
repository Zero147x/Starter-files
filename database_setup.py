import os
import sys
import psycopg2

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()





########insesrt at end of file############CHANGE DATABASE NAME################
engine = create_engine('postgresql://[username]:[password]@127.0.0.1/[Database name]')



Base.metadata.create_all(engine)
