from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    roll: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"),unique=True)

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column()
    hashed_password: Mapped[str] = mapped_column()

