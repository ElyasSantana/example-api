import re
from typing import Union
from uuid import UUID
from pydantic import BaseModel, validator


class Company(BaseModel):
    # id: int
    cnpj: str
    nome: str
    razao_social: str
    endereco: str
    email: str
    telefone: str

    @validator("email")
    def validate_email(cls, email):
        """Validate email value."""
        regex = r"[^ @]+@[^ @]+\.[^ @]+"
        if not re.match(regex, email):
            raise ValueError("Email inválido!")

        return email

    class Config:
        orm_mode = True
