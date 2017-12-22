from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# create user
# user = User(name="Nessa", id=1)
# Create dummy categories

category = Category(name="Air Sports", id=2)
session.add(category)
session.commit()


category2 = Category(name="Beach Sports", id=4)
session.add(category2)
session.commit()

category3 = Category(name="Board Sports", id=6)
session.add(category3)
session.commit()

category4 = Category(name="Land Sports", id=8)
session.add(category4)
session.commit()

category5 = Category(name="Mind Sports", id=10)
session.add(category5)
session.commit()

category6 = Category(name="Ice Sports", id=12)
session.add(category6)
session.commit()
print("added category")


#create dummy items
item1 = Item(name="Card Games", id=1, description="a nice game", category_id=10, user_id=1)
session.add(item1)
session.commit()

item2 = Item(name="Football", id=2, description="a popular game played within 90 mins", category_id=8, user_id=1)
session.add(item2)
session.commit()

print("added items")

