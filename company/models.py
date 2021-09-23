from uuid import uuid4
from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(uuid4, primary_key=True, index=True)
    cnpj = Column(String, max_length=14, index=True)
    nome = Column(String, index=True)
    razao_social = Column(String, index=True)
    endereco = Column(Text, index=True)
    email = Column(String, index=True)
    telefone = Column(String, max_length=14, index=True)
