#!/usr/bin/env pytho

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Sport, Item, Base

engine = create_engine('sqlite:///sportcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
			 picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create sports equipment

# SOCCER EQUIPMENT
soccer = Sport(name="Soccer")
session.add(soccer)
session.commit()

soccerCleats = Item(name="Soccer Cleats", sport=soccer, user=User1)
session.add(soccerCleats)
session.commit()

shinguards = Item(name="Shinguards", sport=soccer, user=User1)
session.add(shinguards)
session.commit()

soccerBall = Item(name="Soccer Ball", sport=soccer, user=User1)
session.add(soccerBall)
session.commit()

soccerUniform = Item(name="Soccer Uniform", sport=soccer, user=User1)
session.add(soccerUniform)
session.commit()


# BASKETBALL EQUIPMENT
basketball = Sport(name="Basketball")
session.add(basketball)
session.commit()

basketballShoes = Item(name="Basketball Shoes", sport=basketball, user=User1)
session.add(basketballShoes)
session.commit()

basketballBall = Item(name="Basketball", sport=basketball, user=User1)
session.add(basketballBall)
session.commit()

basketballUniform = Item(name="Basketball Uniform", sport=basketball, user=User1)
session.add(basketballUniform)
session.commit()

headBand = Item(name="Headband", sport=basketball, user=User1)
session.add(headBand)
session.commit()


# FOOTBALL EQUIPMENT
football = Sport(name="Football")
session.add(basketball)
session.commit()

footballCleats = Item(name="Football Cleats", sport=football, user=User1)
session.add(footballCleats)
session.commit()

footballBall = Item(name="Football", sport=football, user=User1)
session.add(footballBall)
session.commit()

footballPads = Item(name="Football Pads", sport=football, user=User1)
session.add(footballPads)
session.commit()

footballUniform = Item(name="Football Uniform", sport=football, user=User1)
session.add(footballUniform)
session.commit()


# BASEBALL EQUIPMENT
baseball = Sport(name="Baseball")
session.add(basketball)
session.commit()

baseballCleats = Item(name="Baseball Cleats", sport=baseball, user=User1)
session.add(baseballCleats)
session.commit()

bat = Item(name="Bat", sport=baseball, user=User1)
session.add(bat)
session.commit()

baseballBall = Item(name="Baseball", sport=baseball, user=User1)
session.add(baseballBall)
session.commit()

hat = Item(name="Hat", sport=baseball, user=User1)
session.add(hat)
session.commit()

baseballUniform = Item(name="Baseball Uniform", sport=baseball, user=User1)
session.add(baseballUniform)
session.commit()


# HOCKEY EQUIPMENT
hockey = Sport(name="Hockey")
session.add(basketball)
session.commit()

iceSkates = Item(name="Ice Skates", sport=hockey, user=User1)
session.add(iceSkates)
session.commit()

hockeyStick = Item(name="Hockey Stick", sport=hockey, user=User1)
session.add(hockeyStick)
session.commit()

hockeyPads = Item(name="Hockey Pads", sport=hockey, user=User1)
session.add(hockeyPads)
session.commit()

hockeyUniform = Item(name="Hockey Uniform", sport=hockey, user=User1)
session.add(hockeyUniform)
session.commit()
