from sqlalchemy import Column, String, Float, Integer, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from tornado_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Session(db.Model):
    __tablename__ = 'sessions'

    internal_id = Column(String(255), primary_key=True)
    remote_ip = Column(String(255))
    last_ping = Column(Float())
    last_pong = Column(Float())


class Show(db.Model):
    __tablename__ = 'shows'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    start_date = Column(Date())
    end_date = Column(Date())
    created_at = Column(DateTime())

    # Relationships
    cast_list = relationship("Cast")
    character_list = relationship('Character')
    act_list = relationship('Act')


class Cast(db.Model):
    __tablename__ = 'cast'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    first_name = Column(String)
    last_name = Column(String)

    # Relationships
    character_list = relationship('Character', back_populates='cast_member')


class Character(db.Model):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    played_by = Column(Integer, ForeignKey('cast.id'))
    name = Column(String)
    description = Column(String)

    cast_member = relationship("Cast", back_populates='character_list')


class Act(db.Model):
    __tablename__ = 'act'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    name = Column(String)
    interval_after = Column(Boolean)
