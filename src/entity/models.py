from datetime import date
import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = 'todos'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), index=True)
    descriotion: Mapped[str] = mapped_column(String(250), index=True)
    completed: Mapped[bool] = mapped_column(default=False)
    create_at: Mapped[date] = mapped_column('create_at', DateTime, default=func.now(), nullable=True)
    update_at: Mapped[date] = mapped_column('update_at', DateTime, default=func.now, onupdate=func.now(), nullable=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=True)
    user: Mapped["User"] = relationship('User', backref='todos', lazy='joined')


class Role(enum.Enum):
    admin: str = 'admin'
    moderator: str = 'moderator'
    user: str = 'user'


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    refresh_token: Mapped[str] = mapped_column(String(255), nullable=True)
    create_at: Mapped[date] = mapped_column('create_at', DateTime, default=func.now())
    update_at: Mapped[date] = mapped_column('update_at', DateTime, default=func.now(), onupdate=func.now())
    role:Mapped[enum]=mapped_column('role',Enum(Role),default=Role.user,nullable=True)
