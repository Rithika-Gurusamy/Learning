from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    name : Mapped[str] = mapped_column()
    email : Mapped[str] = mapped_column()
    age : Mapped[int] = mapped_column()
    id : Mapped[int] = mapped_column(primary_key=True)