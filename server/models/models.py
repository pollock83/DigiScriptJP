from sqlalchemy import Column, String, Float, Integer, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
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
    edited_at = Column(DateTime())
    first_act_id = Column(Integer, ForeignKey('act.id'))

    # Relationships
    first_act = relationship('Act', uselist=False, foreign_keys=[first_act_id])

    cast_list = relationship("Cast")
    character_list = relationship('Character')
    act_list = relationship('Act', primaryjoin=lambda: Show.id == Act.show_id)
    scene_list = relationship('Scene')
    cue_type_list = relationship('CueType')


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
    first_scene_id = Column(Integer, ForeignKey('scene.id'))
    previous_act_id = Column(Integer, ForeignKey('act.id'))

    first_scene = relationship('Scene', uselist=False, foreign_keys=[first_scene_id])
    previous_act = relationship('Act', uselist=False, remote_side=[id],
                                backref=backref('next_act', uselist=False))


class Scene(db.Model):
    __tablename__ = 'scene'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey('shows.id'))
    act_id = Column(Integer, ForeignKey('act.id'))
    name = Column(String)
    previous_scene_id = Column(Integer, ForeignKey('scene.id'))

    act = relationship('Act', uselist=False, backref=backref('scene_list'),
                       foreign_keys=[act_id])
    previous_scene = relationship('Scene', uselist=False, remote_side=[id],
                                  backref=backref('next_scene', uselist=False))


class CueType(db.Model):
    __tablename__ = 'cuetypes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey('shows.id'))

    prefix = Column(String(5))
    description = Column(String(100))
    colour = Column(String())
