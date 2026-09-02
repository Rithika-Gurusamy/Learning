from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    roll: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()