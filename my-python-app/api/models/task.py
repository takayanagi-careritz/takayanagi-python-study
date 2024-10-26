from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    # 特別なアトリビュート、sqlalchemyが認識する
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    # relationshipでTaskインスタンスからそれに繋がるDoneインスタンスにアクセスできる
    # 双方向で参照する場合はback_populatesをつける
    done = relationship("Done", cascade="delete")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task")
