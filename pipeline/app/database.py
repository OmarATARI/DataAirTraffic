"""Database engine & session creation."""
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models import Base
import time

flag = True
while flag:
  try:
    engine = create_engine(
        'postgresql://pxl:password@postgres:5432/airtraffic',
        echo=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    print('ok')
    flag = False
  except exc.OperationalError:
    print('Waiting for database...')
    time.sleep(1)
  else:
    break

# engine = create_engine(
#     'postgresql://pxl:password@127.0.0.1:5432/airtraffic',
#     echo=True,
#     pool_pre_ping=True
# )