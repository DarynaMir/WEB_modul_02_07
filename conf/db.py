import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# Path to the config file
file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')

# Creating a ConfigParser object
config = configparser.ConfigParser()

# Reading the config file
config.read(file_config)

# Retrieving database connection parameters from the config file
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
db = config.get('DEV_DB', 'DB_NAME')

# Constructing the URI
URI = f'postgresql://{user}:{password}@{domain}:{port}/{db}'
print (URI)

engine = create_engine(URI, echo=True, pool_size=5, max_overflow=0)

DBSession = sessionmaker(bind=engine)
session = DBSession()


