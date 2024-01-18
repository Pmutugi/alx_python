'''imported modules'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
'''class states'''
class States(Base):
    '''state class setting from the imports'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False) 