from fastapi import APIRouter

from company.schemas import Company


router_company = APIRouter()


@router_company.get("/company/")
def get_company():
    return "company app created!"


@router_company.post("/company/")
def post_company(company: Company):
    return company
