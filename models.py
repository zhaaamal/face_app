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

