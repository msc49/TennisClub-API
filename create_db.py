from database import Base, engine
from models import Player

print('Creating Database........')

Base.metadata.create_all(engine)