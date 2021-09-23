from fastapi import APIRouter

router_helloworld = APIRouter()


@router_helloworld.get("/")
def get_helloworld():
    return {"Hello": "World"}
