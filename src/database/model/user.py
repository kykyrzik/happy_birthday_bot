from typing import Set

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import BigInteger

from .base import Base


class User(Base):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    birthday_id: Mapped[Set["Birthday"]] = relationship(back_populates="user")
