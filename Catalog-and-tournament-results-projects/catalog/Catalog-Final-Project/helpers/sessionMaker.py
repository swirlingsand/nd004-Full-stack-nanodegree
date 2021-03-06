"""

Helper function that returns a session object

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base


def newSession():
    engine = create_engine('sqlite:///catalog.db')
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
