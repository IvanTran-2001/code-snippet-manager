from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from datetime import datetime

# Association table for many-to-many relationship between snippets and tags
snippet_tags = Table(
    "snippet_tags",
    Base.metadata,
    Column("snippet_id", Integer, ForeignKey("snippets.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    snippets = relationship("Snippet", back_populates="owner", cascade="all, delete-orphan")


class Snippet(Base):
    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    code = Column(Text, nullable=False)
    language = Column(String(50), nullable=False)  # Python, JavaScript, etc.
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    view_count = Column(Integer, default=0)
    is_public = Column(Integer, default=0)  # 0 = private, 1 = public

    owner = relationship("User", back_populates="snippets")
    tags = relationship("Tag", secondary=snippet_tags, back_populates="snippets")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    snippets = relationship("Snippet", secondary=snippet_tags, back_populates="tags")
