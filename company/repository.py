from app.database import SessionLocal

import schemas
import models


def create_company(db: SessionLocal, company: schemas.Company):
    db_company = models.Company(
        name=company.name,
        description=company.description,
        image=company.image,
        role=company.role,
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
