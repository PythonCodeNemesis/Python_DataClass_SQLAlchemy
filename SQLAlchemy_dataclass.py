from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

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
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

p = Person(name="John", age=30)
session.add(p)
session.commit()

all_persons = session.query(Person).all()
for user in all_persons:
    print(user.name, user.age)

p = Person(name="John2222", age=3000)
session.add(p)
session.commit()

all_persons = session.query(Person).all()
for user in all_persons:
    print(user.name, user.age)