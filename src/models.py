from __future__ import annotations

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, declarative_base, Mapped
from eralchemy2 import render_er

Base = declarative_base()

class UserPlanetFavorite(Base):
    __tablename__ = "user_planet_favorites"

    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    planet_id = Column(Integer, ForeignKey("planets.id"), primary_key=True)

class UserCharacterFavorite(Base):
    __tablename__ = "user_character_favorites"

    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    favorite_planets: Mapped[list['Planet']] = relationship("Planet", secondary="user_planet_favorites")
    favorite_characters: Mapped[list['Character']] = relationship("Character", secondary="user_character_favorites")

class Planet(Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String, nullable=False)
    favorited_by: Mapped[list['User']] = relationship("User", secondary="user_planet_favorites")

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    favorited_by: Mapped[list['User']] = relationship("User", secondary="user_character_favorites")

render_er(Base, "diagram.png")
