from sqlalchemy import Column, Integer, String,Boolean,ForeignKey
from sqlalchemy.sql.expression import null
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(Boolean, server_default="1", nullable=False)
    created_at= Column(TIMESTAMP(timezone=True), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable=False)

    #relationship fetch the user that belongs to a post
    owner = relationship("User")
class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, nullable=False)
    email= Column(String(50), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    created_at= Column(TIMESTAMP(timezone=True), nullable=False)
    phone_number=Column(String(50))
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True)

# run pip install passlib[bcrypt] to be able to hash password before saving them in database