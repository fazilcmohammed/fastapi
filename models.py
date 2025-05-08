from blog.database import Base
from sqlalchemy import Column, String, Integer

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, Index=True)
    title = Column(String)
    body = Column(String)