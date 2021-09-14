from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_helloworld():
    return {"Hello": "World"}
