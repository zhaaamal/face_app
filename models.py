from ctypes.wintypes import OLESTR

from pydantic.color import Color
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    description = Column(Text)

    face_encodings = relationship("FaceEncoding", back_populates="person")
    photos = relationship("Photo", back_populates="person")


class FaceEncoding(Base):
    __tablename__ = 'face_encodings'

    id = Column(Integer, primary_key=True)
    encoding = Column(Text, nullable=False) # Сохраняем JSON/строку
    person_id = Column(Integer, ForeignKey('persons.id'))

    person = relationship("Person", back_populates="face_encodings")


class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    filepath = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))

    person = relationship("Person", back_populates="photos")










