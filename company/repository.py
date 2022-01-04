from app.database import SessionLocal

from company import schemas
from company import models


def create_company(db: SessionLocal, company: schemas.Company):
    db_company = models.Company(
        cnpj=company.cnpj,
        razao_social=company.razao_social,
        endereco=company.endereco,
        email=company.email,
        telefone=company.telefone,
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
