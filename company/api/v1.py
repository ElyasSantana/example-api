from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from company.schemas import Company
from company.repository import create_company

from app.database import SessionLocal


router_company = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_company.get("/company/")
def get_company():
    return "company app created!"


@router_company.post("/company/")
def post_company(company: Company, db: Session = Depends(get_db)):
    response = create_company(db, company)
    print(f"Dados {response}")
    return company
