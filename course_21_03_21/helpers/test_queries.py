from sqlalchemy.orm import sessionmaker
from course_21_03_21.helpers.models import Restaurant
from course_21_03_21.helpers.models import engine

Session = sessionmaker(engine)
session = Session()

rest = Restaurant(name='test_1', identifier_id='1232344')

session.add(rest)

session.commit()
print(session.query(Restaurant.name, Restaurant.identifier_id).all())
