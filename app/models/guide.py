from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Guide(Base):
    __tablename__ = "guides"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    category = Column(String, index=True)        # e.g., Bleeding, Burn, Cardiac
    urgency = Column(String, index=True)         # e.g., Critical, Moderate, Mild
    summary = Column(Text)
    symptoms = Column(Text)       # JSON string: list of symptom strings
    steps = Column(Text)          # JSON string: ordered list of step strings
    donts = Column(Text)          # JSON string: list of "don't" strings
    estimated_time = Column(String)