from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
@dataclass
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(bind=engine)

p = Person(name="John", age=30)
session.add(p)
session.commit()

all_persons = session.query(Person).all()
print(all_persons)