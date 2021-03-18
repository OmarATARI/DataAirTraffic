"""Database engine & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgresql://pxl:password@postgres/airtraffic',
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()