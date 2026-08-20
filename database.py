from sqlalchemy import create_engine
DATABASE_URL = "postgresql://postgres:peaceandpeace@localhost:5432/my_practice_db"
engine = create_engine(DATABASE_URL)
with engine.connect() as connection:
    print("database connected")