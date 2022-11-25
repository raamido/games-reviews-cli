from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os.path import isfile

if not isfile('reviews.sqlite'):
    open('reviews.sqlite', 'x').close()


engine = create_engine('sqlite:///reviews.sqlite', echo=False)

session = sessionmaker(bind=engine)()

Base = declarative_base()


class Review(Base):
    __tablename__ = "Reviews"

    id = Column(Integer, primary_key=True)
    game_name = Column(String(50))
    rate = Column(Integer)
    review = Column(String(200))


Base.metadata.create_all(engine)
