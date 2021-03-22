import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, backref

DB_NAME = 'restaurant.db'
base_path = os.getcwd()
print(f'{base_path}/course_21_03_21/helpers/{DB_NAME}')
engine = create_engine(f'sqlite:///{base_path}/{DB_NAME}', echo=True)

Base = declarative_base()

user_scraping_table = Table('user_scraping',
                            Base.metadata,
                            Column('user_id', String),
                            Column('service_id', String))


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False)
    services = relationship("ScrapingService", secondary=user_scraping_table,  back_populates="user")

class ScrapingService(Base):
    __tablename__ = 'scrapingservice'
    service_id = Column(Integer, primary_key=True)
    name = Column(String)
    base_url = Column(String, unique=True)
    restaurants = relationship("Restaurant", backref="scrapingservice")
    users = relationship("User", secondary=user_scraping_table, back_populates='scrapingservice')

class Restaurant(Base):
    __tablename__ = 'restaurant'
    restaurant_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image_url = Column(String)
    open_hours = Column(String)
    identifier_id = Column(String, nullable=False, unique=True)
    service_id = Column(Integer, ForeignKey("scrapingservice.service_id"))

metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)


